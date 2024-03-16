from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/answer', methods=['GET'])
def get_answer():
    url = request.args.get('url')
    question = request.args.get('question')

    # Here you can perform any processing or call external APIs to get the answer
    # For demonstration purposes, we'll just return a mock answer
    answer = "This is a mock answer for question: '{}' with URL: '{}'".format(question, url)

    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
