import unittest
from dataclasses import dataclass
from models.function_call import FunctionCall


class TestFunctionCall(unittest.TestCase):

    def setUp(self):
        self.function_call = FunctionCall("test_func", {"arg1": 1, "arg2": 2})

    def test_name(self):
        self.assertEqual(self.function_call.name, "test_func")

    def test_arguments(self):
        self.assertDictEqual(self.function_call.arguments, {"arg1": 1, "arg2": 2})

    def test_name_is_string(self):
        self.assertIsInstance(self.function_call.name, str)

    def test_arguments_is_dict(self):
        self.assertIsInstance(self.function_call.arguments, dict)

    def test_name_not_empty(self):
        with self.assertRaises(AttributeError):
            FunctionCall("", {"arg1": 1, "arg2": 2})

    def test_arguments_not_empty(self):
        with self.assertRaises(AttributeError):
            FunctionCall("test_func", {})


if __name__ == '__main__':
    unittest.main()
