import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up the Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_book_title_suggestion(idea, language):
    # Prompt to generate a book title based on the idea
    prompt = f"The user has an idea: '{idea}' in {language}. Suggest a book title in {language}."

    # Make the API call to get the completion
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a creative assistant."},
            {"role": "user", "content": prompt},
        ],
        model="llama3-8b-8192",  # You can change this model as needed
    )

    # Return the generated title
    return chat_completion.choices[0].message.content

def main():
    st.title("Book Title Generator")
    st.subheader("Get a unique book title based on your idea!")

    # User input for idea in English and their language
    idea = st.text_area("Describe your idea (in English and your language):")
    language = st.text_input("Which language is your idea in?")

    if st.button("Generate Book Title"):
        if idea and language:
            with st.spinner("Generating your book title..."):
                title = get_book_title_suggestion(idea, language)
                st.success(f"Suggested Book Title: {title}")
        else:
            st.error("Please fill in both fields.")

if __name__ == "__main__":
    main()


