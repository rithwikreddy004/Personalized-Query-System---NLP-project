# website_content.py
import requests
from bs4 import BeautifulSoup
from youtube_transcripts import fetch_youtube_transcript

def fetch_website_content(url):
    """Fetch and return the text content from the provided URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensure we notice bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        content = ' '.join([p.get_text() for p in paragraphs])
        return content
    
    except requests.RequestException as e:
        return f"Error fetching website content: {e}"

def create_context_from_urls(urls):
    """Create a combined context from multiple URLs."""
    context = ""
    for url in urls:
        if "youtube.com" in url:
            context += fetch_youtube_transcript(url) + "\n\n"
        else:
            context += fetch_website_content(url) + "\n\n"
    return context
