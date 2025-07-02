# app.py

import streamlit as st
import asyncio
import os
from agents import create_team

# Async runner
async def run_task(task: str) -> str:
    team = create_team()
    final_output = ""
    async for msg in team.run_stream(task=task):
        final_output += str(msg) + "\n"
    return final_output

# UI
st.set_page_config(page_title="Arxiv Literature Review", layout="wide")
st.title("📚 Arxiv Literature Review Bot")
st.markdown("Provide a research topic and number of papers. Let the agents handle the rest.")

topic = st.text_input("Enter a research topic:", value="Autogen")
num_papers = st.slider("Number of papers to retrieve", 1, 10, 5)

if st.button("Run Literature Review"):
    if not os.getenv("OPEN_API_KEY"):
        st.error("❌ Missing OpenAI API key. Please set it in your environment or .env file.")
    else:
        with st.spinner("🤖 Agents are working..."):
            task = f"Conduct a literature review on the topic - {topic} and return exactly {num_papers} papers."
            output = asyncio.run(run_task(task))
            st.markdown("### ✍️ Literature Review")
            st.markdown(output)
