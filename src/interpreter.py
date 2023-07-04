from bot import Bot 

model = 'gpt-3.5-turbo-0613'

system_message = 'You are a helpful assistant within an application called `Carousel`. If you believe the conversation has ended based on user input, you will use functions to exit Carousel.'

functions = [{
'name': 'exit_application',
'description': 'exits the Carousel application',
'parameters': {
        'type': 'object',
        'properties': {
            'reason': {
                'type': 'string',
                'description': 'reason for exiting the application'
            }
        }
    }
}]

def get_interpreter():
    return Bot(model, system_message, functions)
