import requests

url = "https://api.d-id.com/talks"

payload = {
    "script": {
        "type": "text",
        "subtitles": "false",
        "provider": {
            "type": "microsoft",
            "voice_id": "en-US-JennyNeural"
        },
        "ssml": "false",
        "input": "Hello"
    },
    "config": {
        "fluent": "false",
        "pad_audio": "0.0"
    },
    "source_url": "https://miro.medium.com/v2/resize:fit:720/format:webp/1*6IghMWWnb6DIGdc8lIubOQ.png"
}
headers = {
    "accept": "application/json",
    "x-api-key-external": "ZHp6LmJhYWNAZ21haWwuY29t:K8YUR5Qrf5O3tSJFlkbJD",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)