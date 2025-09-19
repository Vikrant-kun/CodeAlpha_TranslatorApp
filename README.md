# Universal Translator - CodeAlpha Internship Project

A full-stack web application that translates text and documents (DOCX, PDF, Images) in real-time, featuring a live preview for formatted documents.

---

## Features

- **Live Text Translation:** Instant translation as you type.
- **Text-to-Speech:** Listen to the translated output in the selected language.
- **Advanced Document Translation:**
  - Upload `.docx`, `.pdf`, and image files (`.png`, `.jpg`).
  - **Live Preview for DOCX:** Generates a translated HTML preview that preserves headings, paragraphs, and lists.
  - **Side-by-Side Preview for PDF/Images:** Displays the original file next to the extracted and translated text for context.
- **Multi-Language Support:** Dynamically populated dropdown with dozens of languages.
- **Modern UI:** A clean, tabbed interface built with Tailwind CSS.

---

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, Tailwind CSS, JavaScript (Fetch API)
- **Translation Engine:** `deep-translator` library
- **File Processing:**
  - **DOCX:** `mammoth`, `python-docx`
  - **PDF:** `PyPDF2`
  - **Images (OCR):** `pytesseract`, `Pillow`

---

## Setup & Installation

1.  **Prerequisites:**
    - Python 3.8+
    - Tesseract OCR Engine

2.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/CodeAlpha_TranslatorApp.git](https://github.com/your-username/CodeAlpha_TranslatorApp.git)
    cd CodeAlpha_TranslatorApp
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    
4.  **Run the application:**
    ```bash
    python app.py
    ```
    The application will be available at `http://127.0.0.1:5000`.
