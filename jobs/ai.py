import re
import pdfplumber
import google.generativeai as genai
from decouple import config


# Get the API key from the .env file
API_KEY = config('GOOGLE_API_KEY')

# Pass the key to configure the Google API
genai.configure(api_key=API_KEY)


# ========================================= Extracting Text from PDF (resume) ==================================

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file using pdfplumber."""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return ""

# ========================================= Ranking the Resume ==================================

def rank_resume(resume_text, job_description): 
    """Rank the resume using the job description with AI (Google Gemini)."""
    
    # Prepare the detailed prompt for comparison
    prompt = f"""
    Please compare the following resume with the job description and provide a score from 1 to 10 based on how well the resume matches the requirements of the job:

    Job Description:
    {job_description}

    Resume:
    {resume_text}

    Please consider the following criteria:
    - Does the resume match the required skills and qualifications listed in the job description?
    - Does the experience mentioned in the resume align with the job responsibilities?
    - Does the educational background in the resume meet the job requirements?

    Provide a score from 1 to 10 and explain the reasoning behind the score based on the above criteria.
    """

    try:
        # Initialize the AI model (ensure the correct model name is used)
        model = genai.GenerativeModel("gemini-pro")
        
        # Generate the AI response based on the prompt
        response = model.generate_content(prompt)

        # Clean up the response text and extract only the "numeric" rank score using regex
        rank_score_text = response.text.strip()

        # Use regex to extract the score from the "response"
        match = re.search(r"Score:\s*(\d+)/10", rank_score_text)  # match "Score: 7/10" or similar
        
        if match:
            return match.group(1)  # Return the numeric score as a string (e.g., "7")
        else:
            return "0"  # If no score format matched, return 0
        
    except Exception as e:
        print(f"Error during resume ranking: {e}")
        return "0"
