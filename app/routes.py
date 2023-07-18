from flask import Flask, render_template, request, jsonify
from services.chatbot import get_chatbot
from app import app
from models.message import Message

import tiktoken

chatbot = get_chatbot()
chat_history: list[Message] = []

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/get", methods=['POST'])
def get_bot_response() -> str:
    user_text = request.form['msg']
    input_message = Message('user', user_text)

    # Check if user's message by itself exceeds the token limit
    max_token_limit = chatbot.get_token_limit()
    num_tokens = chatbot.count_tokens([input_message])
    if num_tokens > max_token_limit:
        user_text = "<User's text exceeded the maximum token limit.>"

    # Append the user message to the chat history
    chat_history.append(input_message)

    # Check token count of messages before getting completion
    while chatbot.count_tokens(chat_history) > max_token_limit:
        chat_history.pop(0)

    # Get the completion from the ChatBot
    completion = chatbot.get_completion(chat_history)

    # Get the response, if any, and print it
    # Append the reponse to the chat history
    response = None
    try:
        response = completion.choices[0].message.content
    except AttributeError:
        response = None

    if response:
        chat_history.append(Message('assistant', response))

    return jsonify({'msg': response})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
