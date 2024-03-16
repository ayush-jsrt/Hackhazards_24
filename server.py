from flask import Flask, render_template, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    text = data['text']
    target_language = data['target_language']
    translated_text = translate_text_internal(text, target_language)
    return jsonify({'translated_text': translated_text})

def translate_text_internal(text, target_language='en'):
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

if __name__ == '__main__':
    app.run(debug=True)
