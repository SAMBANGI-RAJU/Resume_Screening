# AI-Powered Resume Screening Tool with Groq

## Overview
This project is a web application built using **Streamlit** that enables users to screen resumes and identify the top candidates based on the required skills. Users can upload multiple PDF resumes, specify required skills, and indicate the number of top candidates to display. The tool uses AI to analyze resumes and generate a summary of the most relevant candidates.

## Features
- Upload multiple PDF resumes.
- Input required skills for candidate screening.
- Specify the number of top candidates to retrieve.
- View a summarized list of the top candidates based on the provided skills.

## Project Structure
- `app.py`: Main file that contains the Streamlit app.
- `helper.py`: Contains the `filter_resumes_by_skills` and `extract_text_from_pdf` functions.
- `client.py`: Contains the `generate_summary` function.

## Prerequisites
Ensure you have the following Python libraries installed:

- **Streamlit**: `pip install streamlit`
- **PyPDF2** or **pdfplumber** (optional for PDF extraction): `pip install pypdf2 pdfplumber`
- Any other custom dependencies (`helper.py` and `client.py` must be available).

## How to Run the Application
1. Clone the repository or download the project files.
2. Ensure the `helper.py` and `client.py` modules are implemented and available in the project directory.
3. Install the required Python packages using the following command:
   ```bash
   pip install streamlit pypdf2 pdfplumber
   ```
4. Run the Streamlit app with the command:
   ```bash
   streamlit run app.py
   ```

## Usage
1. Open the web application in your browser after starting Streamlit.
2. Upload PDF resumes using the file uploader.
3. Enter the required skills separated by commas in the input field.
4. Enter the number of top resumes to display.
5. Click the **Run Screening** button.
6. View the list of top candidates and their summarized details in the text area.

## Code Explanation
- **`uploaded_files`**: Handles multiple PDF file uploads.
- **`skills`**: Captures required skills from user input and splits them into a list.
- **`k`**: Number of resumes to display.
- **`extract_text_from_pdf`**: Extracts text from PDF files.
- **`filter_resumes_by_skills`**: Filters the resumes based on matching skills.
- **`generate_summary`**: Generates a summary of the filtered resumes.

## Example Workflow
1. User uploads three PDF resumes.
2. Enters required skills (e.g., "Python, Data Analysis").
3. Specifies `k = 2` to show the top 2 matching candidates.
4. The app processes the files, extracts text, filters resumes, and displays the summarized top candidates.

## Notes
- Ensure all uploaded resumes are in a readable PDF format.
- The `filter_resumes_by_skills` and `generate_summary` functions should be appropriately defined in the `helper.py` and `client.py` modules.
- If you encounter issues with PDF extraction, consider using an alternative library like `pdfplumber` or adjusting the `extract_text_from_pdf` logic.

## License
This project is licensed under the MIT License.

## Acknowledgments
- Special thanks to the developers of **Streamlit** for providing an easy way to build web apps.
- Libraries used: `Streamlit`, `PyPDF2`, `pdfplumber`.

