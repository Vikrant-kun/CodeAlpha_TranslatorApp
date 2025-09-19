Live Text Translator - A Full-Stack Personal Project
A full-stack web application that provides instant, real-time text translation between dozens of languages, featuring a clean user interface and intelligent text-to-speech. This project was built to demonstrate skills in backend development with Python, frontend interactivity with JavaScript, and API integration.

Features
Live Text Translation: Instantly translates text as you type, powered by a Python and Flask backend.

Intelligent Text-to-Speech: Allows users to listen to the translated output. The speaker button intelligently checks the user's browser for available voice packs and disables itself if a voice is not available for the selected language, preventing errors.

Multi-Language Support: A dynamically populated dropdown menu provides a comprehensive list of available languages for translation.

Modern UI: A clean, responsive, two-panel interface built with Tailwind CSS for an intuitive and professional user experience.

Tech Stack
Backend: Python, Flask

Frontend: HTML, Tailwind CSS, JavaScript (Fetch API, Web Speech API)

Translation Engine: deep-translator library

Setup & Installation
Prerequisites:

Python 3.8+

Clone the repository:

git clone [https://github.com/your-username/Live-Translator-App.git](https://github.com/Vikrant-kun/Live-Translator-App.git)
cd Live-Translator-App

Install dependencies:

pip install -r requirements.txt

Run the application:

python app.py

The application will be available at http://127.0.0.1:5000.
