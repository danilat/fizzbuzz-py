import unittest

def is_multiple(number, multiple):
    return number % multiple == 0

def fizzbuzz(number):
    if is_multiple(number, 15):
        return "FizzBuzz"
    if is_multiple(number, 5):
        return "Buzz"
    if is_multiple(number, 3):
        return "Fizz"
    return str(number)
    
class TestFizzBuzz(unittest.TestCase):
    def test_not_three_or_five_multiple(self):
        self.assertEqual("1", fizzbuzz(1))
        self.assertEqual("2", fizzbuzz(2))

    def test_three_or_multiple_of_three_to_print_fizz(self):
        self.assertEqual("Fizz", fizzbuzz(3))
        self.assertEqual("Fizz", fizzbuzz(6))
    
    def test_five_or_multiple_of_five_to_print_buzz(self):
        self.assertEqual("Buzz", fizzbuzz(5))
        self.assertEqual("Buzz", fizzbuzz(10))
    
    def test_five_and_three_or_multiple_of_five_and_three_to_print_fizzbuzz(self):
        self.assertEqual("FizzBuzz", fizzbuzz(15))
        self.assertEqual("FizzBuzz", fizzbuzz(30))

if __name__ == '__main__':
    unittest.main() 