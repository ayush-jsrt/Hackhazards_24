from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

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

    answer = "This is a mock answer for question: '{}' with URL: '{}'".format(question, get_transcript(extract_video_id(url)))
    return jsonify({"answer": answer})

def get_transcript(video_id):
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    transcript = ' '.join([d['text'] for d in transcript_list])
    return transcript

if __name__ == '__main__':
    app.run(debug=True)
