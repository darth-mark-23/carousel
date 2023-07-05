from flask import Flask, render_template, request, jsonify
from services.interpreter import get_interpreter
from app import app

interpreter = get_interpreter()
chat_history = []

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/get", methods=['POST'])
def get_bot_response():
    user_text = request.form['msg']

    # Perform pre-parsing
    if user_text.lower() == 'exit':
        return jsonify({'msg': 'Exiting...'})

    # Append the user message to the chat history
    system_message = [{'role': 'system', 'content': interpreter.get_system_message()}]
    chat_history.append({'role': 'user', 'content': user_text})
    messages = system_message + chat_history

    # Get the completion from the Interpreter
    completion = interpreter.get_completion(messages)

    # Get the response, if any, and print it
    # Append the reponse to the chat history
    response = None
    try:
        response = completion.choices[0].message.content
    except AttributeError:
        response = None

    if response:
        chat_history.append({'role': 'assistant', 'content': response})

    return jsonify({'msg': response})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
