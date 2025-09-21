import os
from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator
from deep_translator.constants import GOOGLE_LANGUAGES_TO_CODES

def get_languages():
    return {code: name.title() for name, code in GOOGLE_LANGUAGES_TO_CODES.items()}

def real_translate(text, target_lang, source_lang='auto'):
    if not text or not text.strip():
        return ""
    try:
        return GoogleTranslator(source=source_lang, target=target_lang).translate(text)
    except Exception as e:
        print(f"Translation error with deep-translator: {e}")
        return "Error: Translation failed."

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", languages=get_languages())

@app.route("/translate-text", methods=["POST"])
def translate_text_route():
    data = request.get_json()
    text = data.get('text', '')
    source = data.get('source_language', 'auto')
    target = data.get('target_language', 'en')
    translated_text = real_translate(text, target, source)
    return jsonify({'translated_text': translated_text})

if __name__ == "__main__":
    app.run(debug=True)

