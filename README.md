# Live Text Translator - A Full-Stack Application

A full-stack web application that provides instant, real-time text translation between dozens of languages, featuring a clean user interface and intelligent text-to-speech. This is a personal project built to demonstrate full-stack development skills.

---

## Features

- **Live Text Translation:** Instantly translates text as you type, powered by a Python and Flask backend.
- **Intelligent Text-to-Speech:** Allows you to listen to the translated output. The speaker button intelligently disables itself if the user's browser does not have a voice pack for the selected language.
- **Multi-Language Support:** A dynamically populated dropdown menu provides a comprehensive list of available languages.
- **Modern UI:** A clean, responsive, two-panel interface built with Tailwind CSS for an intuitive user experience.

---

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, Tailwind CSS, JavaScript (Fetch API, Web Speech API)
- **Translation Engine:** `deep-translator` library

---

## Setup & Installation

1.  **Prerequisites:**
    - Python 3.8+

2.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/Live-Translator-App.git](https://github.com/your-username/Live-Translator-App.git)
    cd Live-Translator-App
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
