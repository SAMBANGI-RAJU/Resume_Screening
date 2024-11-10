import streamlit as st
import os
from groq import Groq
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import tempfile
import json
# Set up Groq API
client = Groq(api_key="")


def extract_text_from_pdf(file):
    """Extract text from a PDF file."""
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def filter_resumes_by_skills(resumes, skills, top_k=5):
    """Filter resumes based on relevant skills using TF-IDF and cosine similarity."""
    if not resumes:
        return []

    query = " ".join(skills)
    corpus = [query] + [resume["text"] for resume in resumes]
    vectorizer = TfidfVectorizer().fit_transform(corpus)
    vectors = vectorizer.toarray()
    cosine_matrix = cosine_similarity(vectors)

    similarity_scores = cosine_matrix[0][1:]  # Exclude the query itself
    ranked_indices = np.argsort(similarity_scores)[-top_k:]  # Get top-k matches
    relevant_resumes = [resumes[idx] for idx in ranked_indices]

    return relevant_resumes


def generate_summary(resumes, skills, model="llama3-8b-8192"):
    """Generate a summary of the top resumes using the Groq API, but only return the names."""
    if not resumes:
        return "No relevant information found in the resumes."

    # Extract the candidate names from the resumes
    candidate_names = [
        resume["file_name"] for resume in resumes
    ]  # Assuming the file name contains the candidate's name

    context = " ".join([resume["text"] for resume in resumes])
    query = (
        "Summarize the top candidate names based on the following skills, but only return the names: "
        + ", ".join(skills)
    )
    
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": f"Context: {context} Query: {query}"}],
        model=model,
        stream=False,
    )
    # with open("response.json",'w') as file:
    #     json.dump(response,file)

    print(response)
    # We assume the response only contains names (parse if necessary)
    names = response.choices[0].message.content
    return names


# Streamlit web app
st.title("AI-Powered Resume Screening Tool")
st.write("Upload resumes and enter required skills to find top candidates.")

uploaded_files = st.file_uploader(
    "Upload PDF resumes", type="pdf", accept_multiple_files=True
)
skills = st.text_input("Enter required skills (separated by commas)").split(",")
skills = [skill.strip() for skill in skills if skill.strip()]

if st.button("Run Screening"):
    if not uploaded_files or not skills:
        st.warning("Please upload resumes and enter required skills.")
    else:
        # Load and extract text from uploaded resumes
        resumes = []
        for uploaded_file in uploaded_files:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
                temp_file.write(uploaded_file.read())
                try:
                    text = extract_text_from_pdf(temp_file.name)
                    if text.strip():
                        resumes.append({"text": text, "file_name": uploaded_file.name})
                    else:
                        st.warning(
                            f"Skipped empty or unreadable resume: {uploaded_file.name}"
                        )
                except Exception as e:
                    st.error(f"Error processing {uploaded_file.name}: {e}")

        if resumes:
            # Step 2: Filter resumes based on specified skills
            relevant_resumes = filter_resumes_by_skills(resumes, skills)

            # Step 3: Generate a summary of the top resumes (candidate names)
            summary = generate_summary(relevant_resumes, skills)

            st.subheader("Top Candidates Names")
            st.text_area("Candidates", summary, height=300)
        else:
            st.error("No valid resumes found.")
