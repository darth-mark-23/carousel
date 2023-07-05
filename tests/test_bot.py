import unittest
from unittest.mock import patch, Mock
from models.bot import Bot

class TestBot(unittest.TestCase):
    def setUp(self):
        self.model = 'gpt-3.5-turbo-0613'
        self.system_message = 'You are a helpful assistant within an application called `Carousel`. If you believe the conversation has ended based on user input, you will use functions to exit Carousel.'
        self.function_definitions = [{
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
        self.bot = Bot(self.model, self.system_message, self.function_definitions)

    def test_get_model(self):
        self.assertEqual(self.bot.get_model(), self.model)

    def test_get_system_message(self):
        self.assertEqual(self.bot.get_system_message(), self.system_message)

    def test_get_function_definitions(self):
        self.assertEqual(self.bot.get_function_definitions(), self.function_definitions)

    @patch('bot.get_completion')
    def test_get_completion(self, mock_get_completion):
        # Arrange
        mock_messages = ['Hello', 'How can I help you?']
        mock_get_completion.return_value = 'Here is a completion'

        # Act
        result = self.bot.get_completion(mock_messages)

        # Assert
        mock_get_completion.assert_called_once_with(self.model, self.function_definitions, mock_messages)
        self.assertEqual(result, 'Here is a completion')

    def test_get_completion_with_none_messages(self):
        with self.assertRaises(Exception) as context:
            self.bot.get_completion(None)

        self.assertTrue('Bot Bot asked for completion when `messages` is None' in str(context.exception))

if __name__ == '__main__':
    unittest.main()
