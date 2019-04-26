
import unittest
import syntax
import my_email



class test_email(unittest.TestCase):

    def test_email(self):
        aa = my_email.make_email("larry", "shumlich")
        self.assertEqual(aa, "larry.shumlich@evolveu.ca")


unittest.main()
