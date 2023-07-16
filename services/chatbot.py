from models.bot import Bot 
from models.ai_model import AIModel
from models.message import Message

model_name = 'gpt-3.5-turbo-0613'

system_message = Message('system', 'You are a helpful assistant within an application called `Carousel`. If you believe the conversation has ended based on user input, you will use functions to exit Carousel.')

function_definitions = [{
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

model_token_limit = 16 * 1024
chat_history_token_limit = model_token_limit - system_message.content.__len__()

def get_chatbot():
    model = AIModel(
        model_name=model_name,
        context_window_size=chat_history_token_limit
    )
    return Bot(
        _ai_model=model,
        _system_message=system_message,
        _function_definitions=function_definitions,
    )
