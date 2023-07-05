import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')
max_tokens = 2000
temperature = 0.7

def get_completion(model, function_definitions, messages):
    if (model is None):
        raise Exception('Completion requested with missing model parameter')

    if (function_definitions is None):
            raise Exception('Completion requested with missing functions parameter')
    
    if (messages is None):
        raise Exception('Completion requested with blank messages parameter')  

    completion = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        functions = function_definitions,
        max_tokens = max_tokens,
        temperature = temperature
    )
    
    return completion
