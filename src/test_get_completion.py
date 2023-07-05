import unittest
from unittest.mock import patch, MagicMock
import os
from get_completion import get_completion

class TestGetCompletion(unittest.TestCase):
    def setUp(self):
        self.model = 'gpt-3.5-turbo-0613'
        self.functions = [{'name': 'function1'}, {'name': 'function2'}]
        self.messages = [{'role': 'system', 'content': 'Hello, how can I help you?'}]

    def test_get_completion_with_none_model(self):
        with self.assertRaises(Exception) as context:
            get_completion(None, self.functions, self.messages)
        self.assertTrue('Completion requested with missing model parameter' in str(context.exception))

    def test_get_completion_with_none_functions(self):
        with self.assertRaises(Exception) as context:
            get_completion(self.model, None, self.messages)
        self.assertTrue('Completion requested with missing functions parameter' in str(context.exception))

    def test_get_completion_with_none_messages(self):
        with self.assertRaises(Exception) as context:
            get_completion(self.model, self.functions, None)
        self.assertTrue('Completion requested with blank messages parameter' in str(context.exception))

    @patch('openai.ChatCompletion.create')
    def test_get_completion_calls_openai_create(self, mock_create):
        # Arrange
        mock_create.return_value = MagicMock()

        # Act
        result = get_completion(self.model, self.functions, self.messages)

        # Assert
        mock_create.assert_called_once_with(
            model=self.model,
            messages=self.messages,
            functions=self.functions,
            max_tokens=2000,
            temperature=0.7
        )

if __name__ == '__main__':
    unittest.main()
