import unittest
from exercise2.ttd import largest


class AddTest(unittest.TestCase):

    def testlargest1(self):
        self.assertEqual(largest(0, 0, 0), 0)

    def testlargest2(self):
        self.assertEqual(largest(-1, 1, 2), 2)

    def testlargest3(self):
        self.assertEqual(largest(10, 3, 9), 10)

    def testlargest4(self):
        self.assertEqual(largest("A", 3, 4),"error")

    def testlargest5(self):
        self.assertEqual(largest(-1, -5, -3), -1)

    def testlargest6(self):
        self.assertEqual(largest(2.5, 5.6, 7.3),7.3)

    def testlargest7(self):
        self.assertEqual(largest(10, 3.8, 9.1), 10)

    def testlargest8(self):
        self.assertEqual(largest("a", "h", 4.3), "error")


