import fitz
from PIL import Image
import pytesseract
from src.report_utils import clean_text, normalize_aliases

def extract_report_text(uploaded_file):
    """
    Extract text from PDF or image medical reports.
    """

    file_name = uploaded_file.name.lower()

    # ------------------------
    # PDF Report
    # ------------------------
    if file_name.endswith(".pdf"):

        pdf = fitz.open(
            stream=uploaded_file.read(),
            filetype="pdf"
        )

        text = ""

        for page in pdf:
            text += page.get_text()

        pdf.close()

        text = clean_text(text)
        text = normalize_aliases(text)

        return text

    # ------------------------
    # Image Report
    # ------------------------
    elif file_name.endswith((".png", ".jpg", ".jpeg")):

        image = Image.open(uploaded_file)

        text = pytesseract.image_to_string(image)

        text = clean_text(text)
        text = normalize_aliases(text)

        return text

    return ""