from flask import Flask, render_template, request, jsonify
from app import app
from models.bot import Message, FunctionCall
from services.chatbot import ChatBot

chatbot = ChatBot()
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
    response: str = None
    try:
        response = completion.choices[0].message.content
    except AttributeError:
        response = None

    if response:
        chat_history.append(Message('assistant', response))

    function_call: FunctionCall = None
    try:
        function_call_name = completion.choices[0].message.function_call.name
        function_call_arguments = completion.choices[0].message.function_call.arguments
        function_call = FunctionCall(function_call_name, function_call_arguments)
    except (AttributeError, IndexError):
        function_call = None

    if function_call:
        chat_history.append(Message('assistant', f"Called function `{function_call.name}` with arguments `{function_call.arguments}`."))
        chat_history.append(Message(f"function_{function_call.name}", chatbot.resolve_function(function_call) ))


    return jsonify({'msg': response})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
