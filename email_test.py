
import unittest
import syntax
import my_email


class testhelloworld(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(syntax.hello_function(), "hello world")


class test_email(unittest.TestCase):

    def make_email(self):
        aa = my_email.make_email("larry", "pizza")
        self.assertEqual(aa, 12)


unittest.main()
