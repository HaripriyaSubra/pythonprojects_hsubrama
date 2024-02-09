import unittest

import greeting;


class GreetingTest(unittest.TestCase):
    def test_greeting_morning(self):
        self.assertEqual(greeting.find_greeting(7), "Good Morning")

    def test_greeting_afternoon(self):
        self.assertEqual(greeting.find_greeting(13), "Good Afternoon")

    def test_greeting_evening(self):
        self.assertEqual(greeting.find_greeting(18), "Good Evening")
        
    def test_greeting_night(self):
        self.assertEqual(greeting.find_greeting(21), "Good Night")


if __name__ == '__main__':
    unittest.main()
