import unittest
from unittest.mock import Mock
from models.ai_model import AIModel  # assuming this is the location of your AIModel class

class TestAIModel(unittest.TestCase):
    def setUp(self):
        # Mock the get_completion function for testing
        self.mock_get_completion = Mock(return_value="Mocked completion")
        self.model = AIModel('gpt-3', 4096, self.mock_get_completion)

    def test_model_name(self):
        self.assertEqual(self.model.model_name, 'gpt-3')

    def test_context_window_size(self):
        self.assertEqual(self.model.context_window_size, 4096)

    def test_get_ai_completion(self):
        function_definitions = "mock_function_definitions"
        messages = "mock_messages"
        result = self.model.get_ai_completion(function_definitions, messages)
        self.assertEqual(result, "Mocked completion")
        self.mock_get_completion.assert_called_once_with('gpt-3', function_definitions, messages)

    def test_model_name_none(self):
        with self.assertRaises(Exception):
            AIModel(None, 4096, self.mock_get_completion)

    def test_context_window_size_none(self):
        with self.assertRaises(Exception):
            AIModel('gpt-3', None, self.mock_get_completion)

    def test_get_ai_completion_messages_none(self):
        with self.assertRaises(Exception):
            self.model.get_ai_completion("mock_function_definitions", None)


if __name__ == '__main__':
    unittest.main()
