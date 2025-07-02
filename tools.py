# tools.py
import arxiv
from typing import List, Dict

def arxiv_search(query: str, max_results: int = 5) -> List[Dict]:
    client = arxiv.Client()
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance,
    )
    papers = []
    for result in client.results(search):
        papers.append({
            "title": result.title,
            "authors": [a.name for a in result.authors],
            "published": result.published.strftime("%Y-%m-%d"),
            "summary": result.summary,
            "pdf_url": result.pdf_url,
        })
    return papers
