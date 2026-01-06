import os
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from tavily import TavilyClient
import wikipedia


def arxiv_search_tool(query: str, max_results: int = 5) -> list[dict]:
    """
    Search arXiv for academic papers matching the query.
    
    Args:
        query: Search query string
        max_results: Maximum number of results to return
        
    Returns:
        List of paper dictionaries with title, authors, published, summary, url, link_pdf
    """
    base_url = "http://export.arxiv.org/api/query"
    params = {
        "search_query": f"all:{query}",
        "start": 0,
        "max_results": max_results,
        "sortBy": "relevance",
        "sortOrder": "descending"
    }
    
    url = f"{base_url}?{urllib.parse.urlencode(params)}"
    
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            data = response.read().decode("utf-8")
        
        root = ET.fromstring(data)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        
        results = []
        for entry in root.findall("atom:entry", ns):
            title = entry.find("atom:title", ns)
            summary = entry.find("atom:summary", ns)
            published = entry.find("atom:published", ns)
            
            authors = []
            for author in entry.findall("atom:author", ns):
                name = author.find("atom:name", ns)
                if name is not None and name.text:
                    authors.append(name.text)
            
            links = entry.findall("atom:link", ns)
            url_link = ""
            pdf_link = ""
            for link in links:
                if link.get("type") == "text/html":
                    url_link = link.get("href", "")
                elif link.get("title") == "pdf":
                    pdf_link = link.get("href", "")
                elif link.get("rel") == "alternate":
                    url_link = link.get("href", "")
            
            results.append({
                "title": title.text.strip() if title is not None and title.text else "",
                "authors": authors,
                "published": published.text if published is not None and published.text else "",
                "summary": summary.text.strip() if summary is not None and summary.text else "",
                "url": url_link,
                "link_pdf": pdf_link
            })
        
        return results
    
    except Exception as e:
        return [{"error": str(e)}]


def tavily_search_tool(query: str, max_results: int = 5, include_images: bool = False) -> list[dict]:
    """
    Search the web using Tavily API.
    
    Args:
        query: Search query string
        max_results: Maximum number of results to return
        include_images: Whether to include image URLs in results
        
    Returns:
        List of result dictionaries with title, content, url
    """
    api_key = os.environ.get("TAVILY_API_KEY")
    if not api_key:
        return [{"error": "TAVILY_API_KEY not set in environment"}]
    
    try:
        client = TavilyClient(api_key=api_key)
        response = client.search(
            query=query,
            max_results=max_results,
            include_images=include_images
        )
        
        results = []
        for item in response.get("results", []):
            result = {
                "title": item.get("title", ""),
                "content": item.get("content", ""),
                "url": item.get("url", "")
            }
            if include_images and "images" in item:
                result["images"] = item["images"]
            results.append(result)
        
        return results
    
    except Exception as e:
        return [{"error": str(e)}]


def wikipedia_search_tool(query: str) -> dict:
    """
    Search Wikipedia and retrieve a summary.
    
    Args:
        query: Search query string
        
    Returns:
        Dictionary with title, summary, and url
    """
    try:
        page = wikipedia.page(query, auto_suggest=True)
        return {
            "title": page.title,
            "summary": page.summary,
            "url": page.url
        }
    except wikipedia.DisambiguationError as e:
        try:
            page = wikipedia.page(e.options[0])
            return {
                "title": page.title,
                "summary": page.summary,
                "url": page.url
            }
        except Exception as inner_e:
            return {"error": str(inner_e)}
    except wikipedia.PageError:
        return {"error": f"No Wikipedia page found for '{query}'"}
    except Exception as e:
        return {"error": str(e)}
