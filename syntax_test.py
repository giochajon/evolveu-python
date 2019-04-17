import syntax
import unittest


class testhelloworld(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(syntax.hello_function(), "hello world")


class testcalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(syntax.calc(3, 4, "add"), 7)

    def test_sub(self):
        self.assertEqual(syntax.calc(3, 4, "min"), -1)

    def test_mul(self):
        self.assertEqual(syntax.calc(30, 4, "mul"), 120)

    def test_div(self):
        self.assertEqual(syntax.calc(30, 4, "div"), 7.5)


class test_tax_calc(unittest.TestCase):
    def test_lowest(self):
        self.assertEqual(syntax.tax_calc(500), 75)

    def test_m1(self):
        self.assertEqual(syntax.tax_calc(60000), 9619.0)

    def test_m2(self):
        self.assertEqual(syntax.tax_calc(85000), 14619)

    def test_m3(self):
        self.assertEqual(syntax.tax_calc(130000), 25940.66)

    def test_highest(self):
        self.assertEqual(syntax.tax_calc(110000000), 36279296.57)


class test_array(unittest.TestCase):
    def test_add_nothing(self):
        self.assertEqual(syntax.my_array("add"), [0])

    def test_add_one(self):
        self.assertEqual(syntax.my_array("add", 10), [0, 10])

    def test_add_second(self):
        self.assertEqual(syntax.my_array("add", 22), [0, 10, 22])

    def test_total(self):
        syntax.my_array("clear")
        syntax.my_array("add", 10)
        syntax.my_array("add", 22)
        self.assertEqual(syntax.my_array("total"), 32)

    def test_show(self):
        syntax.my_array("clear")
        self.assertEqual(syntax.my_array("show"), [])


class test_dictionary(unittest.TestCase):

    def test_ON(self):
        self.assertEqual(syntax.my_dictionary("ON"), "Ontario")

    def test_ab(self):
        self.assertEqual(syntax.my_dictionary("AB"), "Alberta")


unittest.main()
