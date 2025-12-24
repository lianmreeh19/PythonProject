import unittest

class myFirstPytest(unittest.TestCase):
    def setUp(self):
        print("setUp")
        self.num1 = 3
        self.num2 = 9
        self.num3 = 10
        self.num4 = 3

    def tearDown(self):
        print("tearDown")

    def test_summery(self):
        summery = self.num1 + self.num2

        assert summery == 12, "summery should be 12" # --------> This sentence appears only if the test failed
        print(summery)

    def test_multiple(self):
        multiple = self.num3 * self.num4

        assert multiple == 30, "multiple should be 30"
        print(multiple)

