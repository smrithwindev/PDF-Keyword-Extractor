YAKE Keyword Extractor - Streamlit App

 Project Overview:
 
This Streamlit-based application enables users to extract keywords from PDF documents using the YAKE (Yet Another Keyword Extractor) algorithm.
It supports multiple languages, displays the extracted keywords, and allows users to download them as a neatly formatted PDF report.

 Features
 
- Upload any PDF file (max size ~200MB).
- Select from multiple languages for more accurate keyword extraction.
- View the extracted keywords in real-time.
- Download the keywords as a clean, professional PDF report.
- Built with Python, Streamlit, YAKE, and FPDF.
  
 How to Run
1. Clone this repository to your machine.
2. Create a virtual environment (recommended).
3. Install the required dependencies with `pip install -r requirements.txt`.
4. Run the app using the following command:
   streamlit run app.py
   
   Folder Structure

   - app.py                  # Main Streamlit application
   - requirements.txt        # Dependencies
   - README.md               # Project documentation
   - .gitignore              # Files and folders to ignore during git versioning

  Requirements
- Python 3.7+
- streamlit
- yake
- fpdf
- pymupdf (fitz)

