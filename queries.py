# queries.py
from groq import Groq
import os
# Initialize Groq client
client = Groq()
#client = Groq(api_key=os.getenv("GROQ_API_KEY"))

#client = Groq(api_key="")

#model="llama3-8b-8192"
def query_model(context, query):
    """Query the Groq model with the given context and user query."""
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": f"Context: {context}\n\nQuery: {query}"
                }
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )
        
        response_text = ""
        for chunk in completion:
            response_text += chunk.choices[0].delta.content or ""
        
        return response_text
    
    except Exception as e:
        return f"Error querying the model: {e}"
