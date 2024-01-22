from flask import Flask, request, jsonify , render_template
import requests
import os   
from flask import send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


api_key = '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'

@app.route('/api/get_ai_snippets', methods=['GET'])
def get_ai_snippets():
    query = request.args.get('query')
    gptv = request.args.get('gptv')
    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "openai-organization": "org-yui7Ie8osHV9jytpHdWaIdRv",
                "Content-Type": "application/json"
            },
            json={
                "model": gptv,
                "messages": [
                    {"role": "system", "content": "genius"},
                    {"role": "user", "content": query},
                ],
                "max_tokens": 1000
            }
        )
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)