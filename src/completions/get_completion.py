import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')
model = 'gpt-3.5-turbo'
max_tokens = 2000
temperature = 0.7

def get_completion(prompt):
    completion = openai.ChatCompletion.create(
        model = model,
        messages = [ 
            { "role": "system", "content": "You are a helpful assistant who speaks in cockney slang." },
            { "role": "user", "content": prompt }
        ],
        max_tokens = max_tokens,
        temperature = temperature
    )
    message = completion.choices[0].message.content
    return message
