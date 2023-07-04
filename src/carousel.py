import sys

from interpreter import get_interpreter

interpreter = get_interpreter()
chat_history = []

def exit_application():
    print("Exiting...")
    sys.exit()

def get_user_input():
    return input("User: ")

def preparse_user_input(user_input):
    if user_input.lower() == 'exit':
        exit_application()
    return user_input

while True:
    # Get user input
    user_input = get_user_input()

    # Perform pre-parsing
    preparsed_input = preparse_user_input(user_input)

    # Build messages including chat history & the new message
    # Append the user message to the chat history
    # TODO: Crop (or better yet: summarize) the history when it gets too long (#4)
    system_message = [{'role': 'system', 'content': interpreter.get_system_message()}]
    chat_history.append({'role': 'user', 'content': preparsed_input})
    messages = system_message + chat_history

    # Get the completion from the Interpreter
    completion = interpreter.get_completion(messages)

    # Check for functions, if any, and execute them
    # TODO: make the interpreter execute its own functions (#5)
    # TODO: add function results to the chat history (#6)
    function_call = None
    try:
        function_call = completion.choices[0].message.function_call
    except AttributeError:
        function_call = None

    if (function_call is not None):
        print("Function call: " + function_call.name)
        if (function_call.name == 'exit_application'):
            print("Exiting...")
            break
    
    # Get the response, if any, and print it
    # Append the reponse to the chat history
    response = None
    try:
        response = completion.choices[0].message.content
    except AttributeError:
        response = None
    
    if (response is not None):
        print("AI:", response)
        chat_history.append({'role': 'assistant', 'content': response})
