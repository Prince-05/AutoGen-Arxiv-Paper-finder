# agents.py
import os
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.models.openai import OpenAIChatCompletionClient
from tools import arxiv_search

# Init OpenAI model client
openai_brain = OpenAIChatCompletionClient(
    model="gpt4o",
    api_key=os.getenv("OPEN_API_KEY")
)

# Define agents
arxiv_researcher_agent = AssistantAgent(
    name='arxiv_search_agent',
    description='Create arXiv queries and retrieves candidate papers',
    model_client=openai_brain,
    tools=[arxiv_search],
    system_message=(
        "Given a user topic, think of the best arXiv query. When the tool "
        "returns, choose exactly the number of papers requested and pass "
        "them as concise JSON to the summarizer."
    ),
)

summarizer_agent = AssistantAgent(
    name='summarizer_agent',
    description='An agent which summarizes the result',
    model_client=openai_brain,
    system_message=(
        "You are an expert researcher. When you receive a JSON list of papers, "
        "write a literature-review style report in Markdown:\n"
        "1. Start with a 2-3 sentence introduction of the topic.\n"
        "2. Then include one bullet per paper with: title (as Markdown link), "
        "authors, the specific problem tackled, and its key contribution.\n"
        "3. Close with a single sentence takeaway."
    ),
)

# GroupChat team definition
def create_team():
    return RoundRobinGroupChat(
        participants=[arxiv_researcher_agent, summarizer_agent],
        max_turns=2
    )
