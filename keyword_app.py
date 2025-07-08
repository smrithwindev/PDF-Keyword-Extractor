import streamlit as st
import yake
import fitz  # PyMuPDF
from fpdf import FPDF
import tempfile
import os

# Set up the Streamlit app
st.set_page_config(page_title="Keyword Extractor", layout="centered")
st.title("🔍 PDF Keyword Extractor using YAKE")
st.write("Upload a PDF file, select a language, and extract keywords as a downloadable PDF report.")

# Language selection (placed BEFORE file upload)
lang_display_map = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Dutch": "nl",
    "Hindi": "hi"
}

selected_display_language = st.selectbox("🌐 Choose a language for keyword extraction:", list(lang_display_map.keys()))
selected_lang_code = lang_display_map[selected_display_language]

st.info(f"🔎 Keywords will be extracted in: **{selected_display_language}**")

# File upload
uploaded_file = st.file_uploader("📤 Upload a PDF file", type=["pdf"])

if uploaded_file:
    # Save uploaded file to a temp location
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_path = temp_file.name

    # Extract text from PDF using PyMuPDF
    with fitz.open(temp_path) as doc:
        text = ""
        for page in doc:
            text += page.get_text()

    if text.strip():
        st.subheader("📄 Extracted Text (First 1000 characters):")
        st.write(text[:1000] + "...")

        # YAKE Keyword Extraction
        st.subheader("🧠 Extracting Keywords...")
        kw_extractor = yake.KeywordExtractor(lan=selected_lang_code, n=4, top=20)
        keywords = kw_extractor.extract_keywords(text)

        st.success("✅ Top Extracted Keywords:")
        for kw, score in keywords:
            st.write(f"- {kw} (Score: {score:.4f})")

        # Generate PDF (without scores)
        st.subheader("📄 Download Keywords as PDF")

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Extracted Keywords", ln=True, align="C")
        pdf.ln(10)
        for kw, _ in keywords:
            pdf.cell(200, 10, txt=f"- {kw}", ln=True)

        output_pdf_path = os.path.join(tempfile.gettempdir(), "keywords_output.pdf")
        pdf.output(output_pdf_path)

        with open(output_pdf_path, "rb") as f:
            st.download_button("⬇️ Download PDF", f, file_name="keywords.pdf", mime="application/pdf")

    else:
        st.warning("⚠️ No text found in the uploaded PDF.")
