import streamlit as st
import tempfile
from helper import filter_resumes_by_skills, extract_text_from_pdf
from client import generate_summary


# Streamlit web app
st.title("AI-Powered Resume Screening Tool with RAG")
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
            relevant_resumes = filter_resumes_by_skills(resumes, skills)
            summary = generate_summary(relevant_resumes, skills)

            st.subheader("Top Candidates Names")
            st.text_area("Candidates", summary, height=300)
        else:
            st.error("No valid resumes found.")
