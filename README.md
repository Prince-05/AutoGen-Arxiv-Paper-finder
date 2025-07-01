# Arxiv Literature Review Bot using AutoGen

This project is a research automation pipeline that uses [AutoGen](https://github.com/microsoft/autogen) agents and OpenAI's `gpt-4o` to conduct a concise literature review on any topic using arXiv. It features two collaborating agents:

1. **Arxiv Search Agent** - Crafts optimized queries and fetches relevant academic papers from arXiv.
2. **Summarizer Agent** - Generates a literature review in Markdown format from the search results.

The agents communicate in a team using a `RoundRobinGroupChat`, allowing autonomous task execution and collaboration.

---

## Features

- 🔍 **arXiv Search Integration** - Automatically queries arXiv using keywords.
- 🧠 **Multi-Agent Collaboration** - Two assistant agents interact in a round-robin fashion.
- 📄 **Markdown Summary** - Generates clean, structured summaries suitable for notes or reports.
- 🌐 **Streamlit Web UI** - User-friendly interface for input and viewing results.
- 🔄 **Async Execution** - Utilizes `asyncio` for non-blocking operation.

---

## How It Works

1. The `arxiv_search_agent` generates a relevant query and uses a custom tool (`arxiv_search`) to retrieve papers.
2. The `summarizer_agent` receives the selected papers and writes a Markdown-formatted literature review.
3. Communication happens over a structured loop using `RoundRobinGroupChat`.
4. The whole pipeline is accessible via a Streamlit interface hosted on Streamlit Cloud.

---

## Project Structure

```bash
.
├── autogen_agentchat/          # AutoGen agent definitions
├── autogen_ext/models/openai/ # OpenAI GPT model clients
├── main.py                    # Backend script for async execution
├── app.py                     # Streamlit UI application
├── requirements.txt           # Python dependencies
├── .env.example               # Example environment variable file
```

---

## Requirements

Install all dependencies using:
```bash
pip install -r requirements.txt
```

Dependencies include:
- `openai`
- `autogen`
- `arxiv`
- `streamlit`

---

## Environment Setup

Make sure your OpenAI API key is set in the environment. You can do this in one of two ways:

### Option 1: Export directly
```bash
export OPEN_API_KEY="your-api-key-here"
```

### Option 2: Use a `.env` file
Create a `.env` file in your project root by copying the provided example:
```bash
cp .env.example .env
```
Edit the `.env` file and replace the placeholder with your actual API key.

---

## Running Locally

Start the Streamlit app using:
```bash
streamlit run app.py
```

---

## Hosted Version

Visit the live hosted app: [Streamlit Cloud App URL](https://your-app-name.streamlit.app)

---

## Output Format

A typical review will look like:

```markdown
### Literature Review: Autogen

This report summarizes the recent progress on the topic of Autogen...

- **[Paper Title](PDF_URL)**
  - *Authors:* Author1, Author2
  - *Problem:* ...
  - *Contribution:* ...

... (5 papers)

**Takeaway:** The field of Autogen is rapidly advancing...
```

---

## Demo Screenshots

### Streamlit UI: Search Query Input

![Demo 1 Placeholder](path/to/demo1.png)

### Streamlit UI: Literature Summary Output

![Demo 2 Placeholder](path/to/demo2.png)

---

## Acknowledgements

- [Microsoft AutoGen](https://github.com/microsoft/autogen)
- [arXiv API](https://arxiv.org/help/api/index)
- OpenAI `gpt-4o` for intelligent summarization
- [Streamlit](https://streamlit.io/) for interactive UI

---

## License

MIT License

---

## Future Enhancements

- Add support for citation formats (BibTeX, APA)
- Add export options for PDF/HTML
- Extend UI with charts (e.g., paper trends by year)
- Add semantic clustering of papers
