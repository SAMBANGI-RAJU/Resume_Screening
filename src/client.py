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

# def generate_summary(resumes, skills, api, model="llama3-8b-8192"):
#     """Generate a summary of the top resumes using the Groq API, returning only names."""
#     if not resumes:
#         return "No relevant information found in the resumes."

#     candidate_names = [resume["file_name"] for resume in resumes]  # Assume file name has candidate's name
#     context = "\n".join([resume["text"] for resume in resumes])

#     prompt = (
#         f"You are an AI-powered hiring assistant tasked with finding the most suitable candidates from the following resumes. "
#         f"Each resume is represented by its full text, and your job is to provide the names of the top candidates who best match the following required skills: {', '.join(skills)}. "
#         f"Extract and list only the names and email Ids based on the highest similarity in skills without any additional context."
#     )

#     client = Groq(api_key=api)
#     response = client.chat.completions.create(
#         messages=[{"role": "user", "content": f"Context: {context} Prompt: {prompt}"}],
#         model=model,
#         stream=False,
#     )

#     summary = response.choices[0].message.content
#     return summary


def generate_summary(resumes, skills, api,k, model="llama3-8b-8192"):
    """Generate a structured JSON summary of the top resumes using the Groq API."""
    if not resumes:
        return "No relevant information found in the resumes."

    context = "\n".join([resume["text"] for resume in resumes])

    # Updated prompt for generating the JSON format summary
    prompt = (
        f"You are an AI-powered hiring assistant tasked with finding the most suitable candidates from the provided resumes. "
        f"Each resume is represented by its full text, and your job is to extract and summarize the most relevant information "
        f"for candidates who best match the following required skills: {', '.join(skills)}. "
        f"Give the {k} candiates from the resumes."
        f"The summary must be in the following JSON format:\n\n"
        f"[\n"
        f"    {{\n"
        f'        "name": "Candidate Name",\n'
        f'        "email": "Candidate Email",\n'
        f'        "skills": "Skill(s)",\n'
        f'        "projects": [\n'
        f'            "Project 1",\n'
        f'            "Project 2",\n'
        f'            "Project 3"\n'
        f"        ]\n"
        f"    }},\n"
        f"    ...\n"
        f"]\n\n"
        f"Only include candidates with the highest similarity in skills. Do not include any additional context or explanation. "
        f"Here is the full text of the resumes:\n\n{context}"
    )

    # Initialize the Groq client and send the request
    client = Groq(api_key=api)
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model=model,
        stream=False,
    )

    # Extract the JSON content from the response
    summary = response.choices[0].message.content.strip()
    print(summary)
    return summary
