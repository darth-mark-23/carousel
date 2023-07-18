import unittest
from unittest.mock import patch, Mock
from services.get_completion import get_completion  # replace with actual module path

class TestGetCompletion(unittest.TestCase):
    @patch('openai.ChatCompletion.create')
    def test_get_completion(self, mock_create):
        mock_create.return_value = "Mocked completion"
        mock_message = Mock()
        mock_message.to_json.return_value = "Mocked JSON message"
        result = get_completion('gpt-3', ['mock_function'], [mock_message])
        self.assertEqual(result, "Mocked completion")

    def test_model_none(self):
        with self.assertRaises(Exception):
            get_completion(None, ['mock_function'], ['mock_message'])

    def test_function_definitions_none(self):
        with self.assertRaises(Exception):
            get_completion('gpt-3', None, ['mock_message'])

    def test_messages_none(self):
        with self.assertRaises(Exception):
            get_completion('gpt-3', ['mock_function'], None)


if __name__ == '__main__':
    unittest.main()
