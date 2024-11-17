""" this file contains the model Groq"""

from groq import Groq

# Set up Groq API

# def generate_summary(resumes, skills, api,model="llama3-8b-8192"):
#     """Generate a summary of the top resumes using the Groq API, returning only names."""
#     if not resumes:
#         return "No relevant information found in the resumes."

#     candidate_names = [
#         resume["file_name"] for resume in resumes
#     ]  # Assume file name has candidate's name
#     context = " ".join([resume["text"] for resume in resumes])
#     query = (
#         "Summarize the top candidate names based on the following skills, but only return the names: "
#         + ", ".join(skills)
#     )

#     client = Groq(api_key=api)
#     response = client.chat.completions.create(
#         messages=[{"role": "user", "content": f"Context: {context} Query: {query}"}],
#         model=model,
#         stream=False,
#     )

#     names = response.choices[0].message.content
#     return names

def generate_summary(resumes, skills, api, model="llama3-8b-8192"):
    """Generate a summary of the top resumes using the Groq API, returning only names."""
    if not resumes:
        return "No relevant information found in the resumes."

    candidate_names = [resume["file_name"] for resume in resumes]  # Assume file name has candidate's name
    context = "\n".join([resume["text"] for resume in resumes])

    prompt = (
        f"You are an AI-powered hiring assistant tasked with finding the most suitable candidates from the following resumes. "
        f"Each resume is represented by its full text, and your job is to provide the names of the top candidates who best match the following required skills: {', '.join(skills)}. "
        f"Extract and list only the names and email Ids based on the highest similarity in skills without any additional context."
    )

    client = Groq(api_key=api)
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": f"Context: {context} Prompt: {prompt}"}],
        model=model,
        stream=False,
    )

    names = response.choices[0].message.content
    return names