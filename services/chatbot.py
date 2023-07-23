from models.bot import Bot 
from models.ai_model import AIModel
from models.message import Message

model_name = 'gpt-3.5-turbo-0613'

system_message = Message('system', '''
                         You are a helpful assistant within an application called `Carousel`. You interact with the user to determine what kinds of custom html pages they require.
                         
                         You can use the `create_html_display` function to generate a webpage for the user. You must supply all the HTML code, including inline CSS and JavaScript.
                         
                         If you are unsure of what kind of a page to create, you can ask the user for clarification or assistance.''')

function_definitions = [
    {
        'name': 'create_html_display',
        'description': "Serve a webpage to the user based on the html supplied via the arguments",
        'parameters': {
            'type': 'object',
            'properties': {
                'html': {
                    'type': 'string',
                    'description': 'The html to serve to the user, including inline CSS and JavaScript'
                }
            }
        }
    }
]

def create_html_display_function( arguments ) -> any:
    # TODO: Make it so the html is actually served to the user
    return print(arguments['html'])

function_resolvers = {
    'create_html_display': create_html_display_function
}

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
        _function_resolvers=function_resolvers
    )
