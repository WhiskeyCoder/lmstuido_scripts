import openai


def extract_content(response):
    if 'content' in response:
        return response['content']
    else:
        return None

def gen_with_lmstudio(input_to_send):
    openai.api_base = "http://localhost:1234/v1"
    openai.api_key = ""
    # we are not using a system prompt here as we are using a Preset to shape the response we want
    completion = openai.ChatCompletion.create(
        model="local-model",
        messages=[
            {"role": "user", "content": input_to_send}
        ]
    )

    assistant_response = completion.choices[0].message
    content = extract_content(assistant_response)
    return content


input_to_send = "What content you want the Ai to work on" 
llm_response = gen_with_lmstudio(input_to_send)
print(llm_response)
