# frontend.py
import streamlit as st
from queries import query_model
from youtube_transcripts import fetch_youtube_transcript
from website_content import fetch_website_content, create_context_from_urls

# Streamlit UI
st.set_page_config(page_title="Query System", page_icon=":mag_right:", layout="wide", initial_sidebar_state="expanded")

# Apply dark theme using Streamlit's config.toml
st.markdown(
    """
    <style>
    .css-1e2k5b7 {background-color: #1e1e1e;} 
    .css-ffhzg2 {background-color: #2e2e2e; color: #ffffff;} 
    .css-16y4i7v {color: #c4c4c4;}
    .css-1l8bfp6 {color: #ffffff; background-color: #333333; border: 1px solid #444444;}
    </style>
    """,
    unsafe_allow_html=True
)

# Main Title
st.title("🔍 Query System with Context from Links")

# Sidebar for links input
st.sidebar.header("Provide Links")
st.sidebar.markdown("Paste up to 5 links below to create context for your queries.")
urls = []
for i in range(1, 6):
    url = st.sidebar.text_input(f"Link {i}", "")
    if url:
        urls.append(url)

# Create context from provided links
if urls:
    context = create_context_from_urls(urls)
    st.sidebar.success("Links fetched successfully.")
else:
    context = ""

# Center search bar for the initial query
st.header("Ask Your Query")
query = st.text_input("Enter your query here:")

# Placeholder for the response and follow-up query
if query:
    if context:
        answer = query_model(context, query)
        st.write("**Answer:**")
        st.write(answer)
    else:
        st.warning("Please provide links in the sidebar to generate context.")


