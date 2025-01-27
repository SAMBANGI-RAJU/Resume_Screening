""" This is the file for the Helpers function """

from PyPDF2 import PdfReader
import numpy as np
from sentence_transformers import SentenceTransformer, util


# Load a SentenceTransformer model for embedding extraction
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def extract_text_from_pdf(file):
    """Extract text from a PDF file."""
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def embed_texts(texts):
    """Generate embeddings for a list of texts."""
    return embedding_model.encode(texts, convert_to_tensor=True)


def filter_resumes_by_skills(resumes, skills, top_k):
    """Filter resumes based on relevant skills using embeddings and similarity search."""
    if not resumes:
        return []

    query_embedding = embed_texts([" ".join(skills)])
    resume_texts = [resume["text"] for resume in resumes]
    resume_embeddings = embed_texts(resume_texts)

    # Compute cosine similarity between query and resume embeddings
    similarity_scores = util.pytorch_cos_sim(query_embedding, resume_embeddings)[0]
    top_indices = np.argsort(similarity_scores.numpy())[-top_k - 1 :][::-1]

    relevant_resumes = [resumes[idx] for idx in top_indices]
    # print(top_indices)
    return relevant_resumes,similarity_scores,list(top_indices)
