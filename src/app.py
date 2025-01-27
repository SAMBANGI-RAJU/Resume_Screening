# # import streamlit as st
# # import tempfile
# # from helper import filter_resumes_by_skills, extract_text_from_pdf
# # from client import generate_summary


# # # Streamlit web app
# # st.title("AI-Powered Resume Screening Tool with Groq")
# # st.write("Upload resumes and enter required skills to find top candidates.")

# # uploaded_files = st.file_uploader(
# #     "Upload PDF resumes", type="pdf", accept_multiple_files=True
# # )
# # skills = st.text_input("Enter required skills (separated by commas)").split(",")
# # skills = [skill.strip() for skill in skills if skill.strip()]

# # k = st.text_input("Enter the Number of resumes :")

# # api = st.text_input("Enter the Groq's API KEY:")

# # if st.button("Run Screening"):
# #     if not uploaded_files or not skills:
# #         st.warning("Please upload resumes and enter required skills.")
# #     else:
# #         resumes = []
# #         for uploaded_file in uploaded_files:
# #             with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
# #                 temp_file.write(uploaded_file.read())
# #                 try:
# #                     text = extract_text_from_pdf(temp_file.name)
# #                     if text.strip():
# #                         resumes.append({"text": text, "file_name": uploaded_file.name})
# #                     else:
# #                         st.warning(
# #                             f"Skipped empty or unreadable resume: {uploaded_file.name}"
# #                         )
# #                 except Exception as e:
# #                     st.error(f"Error processing {uploaded_file.name}: {e}")

# #         if resumes:
# #             relevant_resumes = filter_resumes_by_skills(resumes, skills, int(k))
# #             summary = generate_summary(relevant_resumes, skills, api)

# #             st.subheader("Top Candidates Names")
# #             st.text_area("Candidates", summary, height=300)
# #         else:
# #             st.error("No valid resumes found.")


# import streamlit as st
# import tempfile
# from helper import filter_resumes_by_skills, extract_text_from_pdf
# from client import generate_summary
# import re
# import json
# # Streamlit web app
# st.title("✨ AI-Powered Resume Screening Tool with Groq")
# st.write("Upload resumes and enter required skills to find top candidates.")

# uploaded_files = st.file_uploader(
#     "Upload PDF resumes", type="pdf", accept_multiple_files=True
# )
# skills = st.text_input("Enter required skills (separated by commas)").split(",")
# skills = [skill.strip() for skill in skills if skill.strip()]

# k = st.text_input("Enter the Number of Candidates:")
# api = st.text_input("Enter the Groq's API KEY:")

# if st.button("Run Screening"):
#     if not uploaded_files or not skills:
#         st.warning("Please upload resumes and enter required skills.")
#     else:
#         resumes = []
#         for uploaded_file in uploaded_files:
#             with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
#                 temp_file.write(uploaded_file.read())
#                 try:
#                     text = extract_text_from_pdf(temp_file.name)
#                     if text.strip():
#                         resumes.append({"text": text, "file_name": uploaded_file.name})
#                     else:
#                         st.warning(
#                             f"Skipped empty or unreadable resume: {uploaded_file.name}"
#                         )
#                 except Exception as e:
#                     st.error(f"Error processing {uploaded_file.name}: {e}")

#         if resumes:
#             relevant_resumes,similarit_scores,indices = filter_resumes_by_skills(resumes, skills, int(k))
#             # print(similarit_scores)
#             # print(relevant_resumes)
#             summary = generate_summary(relevant_resumes, skills, api)

#             st.subheader("✨ Top Candidates")
#             match = re.search(r'\[.*\]', summary, re.DOTALL)

#             if match:
#                 candidates_json = match.group(0)

#                 # Parse the JSON string into a Python list
#                 candidates = json.loads(candidates_json)
#                 print("========================")
#                 print(candidates)
#                 print("============================")
#                 st.subheader("Top Candidates Who Match the Required Skills (Python)")

#                 for i, candidate in enumerate(candidates, start=1):
#                     # Ensure skills are formatted correctly
#                     skills = candidate['skills'].replace(',', ', ')  # Add space after commas for better readability

#                     # Ensure projects are listed correctly
#                     projects_list = ''.join([f"<li>{project}</li>" for project in candidate['projects']])

#                     print("===========================")
#                     print(projects_list)
#                     print(skills)
#                     print("====================")
#                     # Display candidate details in styled divs
#                     st.markdown(
#                         f"""
#                         <div style="border: 2px solid #4CAF50; border-radius: 12px; padding: 20px; margin-bottom: 15px; background-color: #f9f9f9; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);">
#                             <h3 style="color: #2b6cb0;">{i}. {candidate['name']}</h3>
#                             <p><b>Email:</b> <a href="mailto:{candidate['email']}" style="text-decoration: none; color: #4CAF50;">{candidate['email']}</a></p>
#                             <p><b>Skills:</b> {skills}</p>
#                             <p><b>Projects:</b></p>
#                             <ul>
#                                 {projects_list}
#                             </ul>
#                         </div>
#                         """,
#                         unsafe_allow_html=True,
#                     )

#                 st.info("Note: The evaluation is based solely on the resumes provided and may not be exhaustive or comprehensive.")

#             else:
#                 st.error("Failed to extract candidate data.")

#         else:
#             st.error("No valid resumes found.")


# import streamlit as st
# import tempfile
# from helper import filter_resumes_by_skills, extract_text_from_pdf
# from client import generate_summary
# import re
# import json

# # Streamlit web app
# st.title("✨ AI-Powered Resume Screening Tool with Groq")
# st.write("Upload resumes and enter required skills to find top candidates.")

# uploaded_files = st.file_uploader(
#     "Upload PDF resumes", type="pdf", accept_multiple_files=True
# )
# skills = st.text_input("Enter required skills (separated by commas)").split(",")
# skills = [skill.strip() for skill in skills if skill.strip()]

# k = st.text_input("Enter the Number of Candidates:")
# api = st.text_input("Enter the Groq's API KEY:")

# if st.button("Run Screening"):
#     if not uploaded_files or not skills:
#         st.warning("Please upload resumes and enter required skills.")
#     else:
#         resumes = []
#         for uploaded_file in uploaded_files:
#             with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
#                 temp_file.write(uploaded_file.read())
#                 try:
#                     text = extract_text_from_pdf(temp_file.name)
#                     if text.strip():
#                         resumes.append({"text": text, "file_name": uploaded_file.name})
#                     else:
#                         st.warning(
#                             f"Skipped empty or unreadable resume: {uploaded_file.name}"
#                         )
#                 except Exception as e:
#                     st.error(f"Error processing {uploaded_file.name}: {e}")

#         if resumes:
#             relevant_resumes, similarit_scores, indices = filter_resumes_by_skills(
#                 resumes, skills, int(k)
#             )
#             summary = generate_summary(relevant_resumes, skills, api,k)

#             st.subheader("✨ Top Candidates")

#             # Regex to extract the JSON array containing candidates
#             match = re.search(r"\[.*\]", summary, re.DOTALL)
#             if match:
#                 candidates_json = match.group(0)
#                 candidates = json.loads(
#                     candidates_json
#                 )  # Convert JSON string to list of candidates

#                 # Ensure candidates list is not empty
#                 if candidates:
#                     st.subheader(
#                         "Top Candidates Who Match the Required Skills (Python)"
#                     )

#                     for i, candidate in enumerate(candidates, start=1):
#                         # Formatting skills and projects for display
#                         skills_str = ", ".join(
#                             [skill.strip() for skill in candidate["skills"].split(",")]
#                         )
#                         projects_list = "".join(
#                             [
#                                 f"<li>{project}</li>"
#                                 for project in candidate.get("projects", [])
#                             ]
#                         )

#                         # Display candidate details in styled divs
#                         st.markdown(
#                             f"""
#                             <div style="border: 2px solid #4CAF50; border-radius: 6px; padding: 10px; margin-bottom: 5px; background-color: #f9f9f9; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);">
#                                 <h3 style="color: #2b6cb0;">{i}. {candidate['name']}</h3>
#                                 <p><b>Email:</b> <a href="mailto:{candidate['email']}" style="text-decoration: none; color: #4CAF50;">{candidate['email']}</a></p>
#                                 <p><b>Skills:</b> {skills_str}</p>
#                                 <p><b>Projects:</b></p>
#                                 <ul>
#                                     {projects_list}
#                                 </ul>
#                             </div>
#                             """,
#                             unsafe_allow_html=True,
#                         )
#                 else:
#                     st.error("No valid candidate data found.")
#             else:
#                 st.error("Failed to extract candidate data.")
#         else:
#             st.error("No valid resumes found.")

# st.info(
#     "Note: The evaluation is based solely on the resumes provided and may not be exhaustive or comprehensive."
# )



import streamlit as st
import tempfile
from helper import filter_resumes_by_skills, extract_text_from_pdf
from client import generate_summary
import re
import json

# Streamlit web app
st.title("✨ AI-Powered Resume Screening Tool with Groq")
st.write("Upload resumes and enter required skills to find top candidates.")

uploaded_files = st.file_uploader(
    "Upload PDF resumes", type="pdf", accept_multiple_files=True
)
skills = st.text_input("Enter required skills (separated by commas)").split(",")
skills = [skill.strip() for skill in skills if skill.strip()]

k = st.text_input("Enter the Number of Candidates:")
api = st.text_input("Enter the Groq's API KEY:")

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
            relevant_resumes, similarit_scores, indices = filter_resumes_by_skills(
                resumes, skills, int(k)
            )
            summary = generate_summary(relevant_resumes, skills, api, k)

            st.subheader("✨ Top Candidates")

            # Regex to extract the JSON array containing candidates
            match = re.search(r"\[.*\]", summary, re.DOTALL)
            if match:
                candidates_json = match.group(0)
                candidates = json.loads(candidates_json)  # Convert JSON string to list of candidates

                if candidates:
                    st.subheader("Top Candidates Who Match the Required Skills (Python)")

                    for i, candidate in enumerate(candidates, start=1):
                        # Debugging output for candidate data
                        st.write(f"Candidate {i}: {candidate}")  # Debug line to check the structure of candidate data

                        # Ensure skills and projects fields are properly formatted
                        skills_str = ", ".join([skill.strip() for skill in candidate["skills"].split(",")]) if "skills" in candidate else "N/A"
                        projects_list = "".join([f"<li>{project}</li>" for project in candidate.get("projects", [])]) if "projects" in candidate else "<li>No projects listed</li>"

                        # Display candidate details in styled divs
                        st.markdown(
                            f"""
                            <div style="border: 2px solid #4CAF50; border-radius: 6px; padding: 10px; margin-bottom: 5px; background-color: #f9f9f9; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);">
                                <h3 style="color: #2b6cb0;">{i}. {candidate['name']}</h3>
                                <p><b>Email:</b> <a href="mailto:{candidate['email']}" style="text-decoration: none; color: #4CAF50;">{candidate['email']}</a></p>
                                <p><b>Skills:</b> {skills_str}</p>
                                <p><b>Projects:</b></p>
                                <ul>
                                    {projects_list}
                                </ul>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )
                else:
                    st.error("No valid candidate data found.")
            else:
                st.error("Failed to extract candidate data.")
        else:
            st.error("No valid resumes found.")

st.info(
    "Note: The evaluation is based solely on the resumes provided and may not be exhaustive or comprehensive."
)
