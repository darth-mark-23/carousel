from completions.get_completion import get_completion

while True:
    user_input = input("User: ")
    if user_input.lower() == 'exit':
        print("Exiting...")
        break
    prompt = f"User: {user_input}\nAI:"
    completion = get_completion(prompt)
    print("AI:", completion)
