import requests


# optional; defaults to `os.environ['OPENAI_API_KEY']`
api_key = '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'

# The API endpoint for GPT-4 completions
url = "	https://api.openai.com/v1/chat/completions"

# Headers including your API key for authentication
headers = {
    "Authorization": f"Bearer {api_key}",
    "OpenAI-Organization": "org-yui7Ie8osHV9jytpHdWaIdRv",
    "Content-Type": "application/json"
}

# Data payload with your prompt
data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hi, how do I output all files in a directory using Python?"},
    ],
    "max_tokens": 1000
}

# Sending a POST request to the API
response = requests.post(url, json=data, headers=headers)

# Checking if the request was successful
if response.status_code == 200:
    print(response.json())
else:
    print("Error:", response.status_code, response.text)