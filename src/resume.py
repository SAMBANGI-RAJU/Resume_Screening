import os
from groq import Groq
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import glob
import json
# Set up Groq API
client = Groq(api_key="")

# Specify the folder where resumes are stored
data_folder = r"C:\Users\samba\OneDrive\Desktop\Gen AI\resume screening\resumes"

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def load_resumes(data_folder=data_folder):
    """Load and extract text from all PDF files in the data folder."""
    resumes = []
    file_paths = glob.glob(os.path.join(data_folder, "*.pdf"))
    if not file_paths:
        print("No PDF files found in the specified folder. Check the path and file extensions.")
    else:
        print(f"Found PDF files: {file_paths}")
    
    for file_path in file_paths:
        try:
            text = extract_text_from_pdf(file_path)
            if text.strip():  # Ensure non-empty text
                resumes.append({"text": text, "file_path": file_path})
            else:
                print(f"Skipped empty or unreadable resume: {file_path}")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    
    return resumes

def filter_resumes_by_skills(resumes, skills, top_k=5):
    """Filter resumes based on relevant skills using TF-IDF and cosine similarity."""
    if not resumes:
        print("No resumes loaded.")
        return []
    
    query = " ".join(skills)  # Combine required skills as a single query
    corpus = [query] + [resume["text"] for resume in resumes]
    vectorizer = TfidfVectorizer().fit_transform(corpus)
    vectors = vectorizer.toarray()
    cosine_matrix = cosine_similarity(vectors)
    
    similarity_scores = cosine_matrix[0][1:]  # Exclude the query itself
    ranked_indices = np.argsort(similarity_scores)[-top_k:]  # Get top-k matches
    relevant_resumes = [resumes[idx] for idx in ranked_indices]
    
    return relevant_resumes

def generate_summary(resumes, skills, model="llama3-8b-8192"):
    """Generate a summary of the top resumes using the Groq API."""
    if not resumes:
        return "No relevant information found in the resumes."
    
    context = " ".join([resume["text"] for resume in resumes])
    query = "Summarize top candidate resumes based on the following skills: " + ", ".join(skills)
    
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": f"Context: {context} Query: {query}"}],
        model=model,
        stream=False,
    )
    # print("===================")
    # print(response)
    with open("response.json",'w') as file:
        json.dump(response)
    return response.choices[0].message.content

def resume_screening_pipeline(data_folder, skills):
    """Run the full resume screening pipeline."""
    # Step 1: Load resumes from the folder
    resumes = load_resumes(data_folder)
    if not resumes:
        return "No resumes were loaded. Please check the folder path and file contents."
    
    # Step 2: Filter resumes based on specified skills
    relevant_resumes = filter_resumes_by_skills(resumes, skills)
    
    # Step 3: Generate a summary of the top resumes
    summary = generate_summary(relevant_resumes, skills)
    
    return summary

def interactive_screening_interface(data_folder=data_folder):
    """Interactive interface for running the resume screening tool."""
    print("Welcome to the AI-powered Resume Screening Tool!")
    skills = input("Enter required skills (separated by commas): ").split(",")
    skills = [skill.strip() for skill in skills]  # Clean up whitespace
    
    # Run the screening pipeline
    summary = resume_screening_pipeline(data_folder, skills)
    
    # Display the summary of top candidates
    print("\nTop Candidates Summary:")
    print(summary)

if __name__ == "__main__":
    interactive_screening_interface()
