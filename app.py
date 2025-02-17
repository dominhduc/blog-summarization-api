from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    summary = summarizer(data['text'], max_length=50, min_length=25, do_sample=False)
    return jsonify(summary[0])

@app.route('/')
def home():
    return "Welcome to the Summarization API"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
