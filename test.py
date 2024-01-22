import requests
import json

# Your OpenAI API key (placeholder for demonstration)
api_key = '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'

# Use 'engine' to specify the model
engine = 'gpt-4-1106-preview'

# Endpoint URL for the completion endpoint
url = f'https://api.openai.com/v1/engines/{engine}/completions'

# Data to send, including your prompt
data = {
    "prompt": "Here is my prompt. Continue the story: ",
    "max_tokens": 150,
    "temperature": 0.7,
}

# Headers including your API key
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

# Make the POST request
response = requests.post(url, headers=headers, json=data)

# Print the response
print(response.json())
