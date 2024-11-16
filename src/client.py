""" this file contains the model Groq"""

from groq import Groq

# Set up Groq API
client = Groq(api_key="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")


def generate_summary(resumes, skills, model="llama3-8b-8192"):
    """Generate a summary of the top resumes using the Groq API, returning only names."""
    if not resumes:
        return "No relevant information found in the resumes."

    candidate_names = [
        resume["file_name"] for resume in resumes
    ]  # Assume file name has candidate's name
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

    names = response.choices[0].message.content
    return names
