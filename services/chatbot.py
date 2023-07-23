from models.bot import Bot 
from models.ai_model import AIModel
from models.message import Message

class ChatBot(Bot):
    MODEL_NAME = 'gpt-3.5-turbo-0613'
    SYSTEM_MESSAGE_DIRECTORY = 'services/'
    SYSTEM_MESSAGE_FILE = 'chatbot_system_message.txt'
    FUNCTION_DEFINITIONS = [
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
    MODEL_TOKEN_LIMIT = 16 * 1024
    
    def __init__(self):
        with open(self.SYSTEM_MESSAGE_DIRECTORY + self.SYSTEM_MESSAGE_FILE, 'r') as file:
            system_message_content = file.read()
        system_message = Message('system', system_message_content)
        
        chat_history_token_limit = self.MODEL_TOKEN_LIMIT - len(system_message.content)
        
        model = AIModel(
            model_name=self.MODEL_NAME,
            context_window_size=chat_history_token_limit
        )
        super().__init__(
            _ai_model=model,
            _system_message=system_message,
            _function_definitions=self.FUNCTION_DEFINITIONS,
            _function_resolvers=self._get_function_resolvers()
        )
    
    def _get_function_resolvers(self):
        return {
            'create_html_display': self.create_html_display_function
        }

    @staticmethod
    def create_html_display_function(arguments) -> any:
        # TODO: Make it so the html is actually served to the user
        return print(arguments['html'])
