import unittest
from name_fun import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_fun.py'."""

    def test_first_last_name(self):
        """Do names like 'Rosie Peanut' work?"""
        formatted_name = get_formatted_name('rosie', 'peanut')
        self.assertEqual(formatted_name, 'Rosie Peanut')

if __name__ == '__main__':
    unittest.main()

print("""

        This exercise is from Python Crash Course by
        Eric Matthes, and is intended for practice only.

        """)
