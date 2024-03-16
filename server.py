from flask import Flask, request, jsonify, send_file
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
from gtts import gTTS
from googletrans import Translator
import os

def extract_video_id(youtube_link):
    parsed_url = urlparse(youtube_link)
    query_params = parse_qs(parsed_url.query)
    
    video_id = query_params.get('v', [''])[0]
    
    return video_id

app = Flask(__name__)

@app.route('/answer', methods=['GET'])
def get_answer():
    url = request.args.get('url')
    question = request.args.get('question')

    try:
        video_id = extract_video_id(url)
        transcript = get_transcript(video_id)
        hindi_text = translate_to_hindi(transcript)
        audio_file = tts_hi(hindi_text)
        return jsonify({"audio_url": audio_file})
    except Exception as e:
        return jsonify({"error": str(e)})

def get_transcript(video_id):
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    transcript = ' '.join([d['text'] for d in transcript_list])
    return transcript

def translate_to_hindi(text):
    translator = Translator()
    translation = translator.translate(text, src='en', dest='hi')
    return translation.text

def tts_hi(hindi_text):
    language = 'hi'
    output_file = "output.mp3"
    myobj = gTTS(text=hindi_text, lang=language, slow=False)
    myobj.save(output_file)
    return output_file

if __name__ == '__main__':
    app.run(debug=True)
