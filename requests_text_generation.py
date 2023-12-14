import json
import requests


input_to_send = "what do you want to ask"
INSTRUCTIONS = "how do you want the AI to respond" 

url = "http://localhost:1234/v1/chat/completions"
headers = {
    "Content-Type": "application/json"
}
payload = {
    "messages": [
          {
            "role": "user",
            "content": f"### Instruction: {INSTRUCTIONS} {input_to_send}.\n### Response: "
        }
    ],
    "stop": ["### Instruction:"],
    "temperature": 0.7,
    "max_tokens": -1,
    "stream": False
}
response = requests.post(url, headers=headers, data=json.dumps(payload))
if response.status_code == 200:
    result = response.json()
    generated_message = result['choices'][0]['message']['content']
    print(f"LLM message: {generated_message}")
    return generated_message
else:
    print("Error:", response.status_code, response.text)
