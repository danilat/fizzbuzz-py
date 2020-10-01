import unittest


def fizzbuzz(number):
    pass

class TestFizzBuzz(unittest.TestCase):
    def test_not_three_or_five_multiple(self):
        self.assertEqual("1", fizzbuzz(1))


if __name__ == '__main__':
    unittest.main()