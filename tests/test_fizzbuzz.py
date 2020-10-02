import unittest


def fizzbuzz(number):
    is_three_multiple = number % 3 == 0
    is_five_multiple = number % 5 == 0

    if (is_three_multiple and is_five_multiple):
        return 'FizzBuzz'

    if (is_three_multiple):
        return 'Fizz'

    if (is_five_multiple):
        return 'Buzz'

    return str(number)

class TestFizzBuzz(unittest.TestCase):
    def test_not_three_or_five_multiple(self):
        self.assertEqual("1", fizzbuzz(1))

    def test_three_should_return_fizz(self):
        self.assertEqual("Fizz", fizzbuzz(3)) 

    def test_five_should_return_buzz(self):
        self.assertEqual("Buzz", fizzbuzz(5))

    def test_fifteen_should_return_fizzbuzz(self):
        self.assertEqual("FizzBuzz", fizzbuzz(15))


if __name__ == '__main__':
    unittest.main()