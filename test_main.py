import unittest
import io
import sys
from contextlib import redirect_stdout
from main import main

class TestHelloWorld(unittest.TestCase):
    def test_hello_world_output(self):
        """Test that the main function prints 'Hello World'"""
        f = io.StringIO()
        with redirect_stdout(f):
            main()
        output = f.getvalue().strip()
        self.assertEqual(output, "Hello World")

if __name__ == "__main__":
    unittest.main()