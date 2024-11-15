import unittest
from math import sqrt


# Utility functions to test
def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


class TestUtilityFunctions(unittest.TestCase):

    # Tests for add()
    def test_add_integers(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_add_floats(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=1)

    def test_add_strings(self):
        self.assertEqual(add("foo", "bar"), "foobar")

    # Tests for divide()
    def test_divide_integers(self):
        self.assertEqual(divide(6, 3), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(5, 0)

    # Tests for is_prime()
    def test_is_prime_with_primes(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(17))

    def test_is_prime_with_non_primes(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(20))

    def test_is_prime_with_negative_numbers(self):
        self.assertFalse(is_prime(-5))


if __name__ == '__main__':
    unittest.main()
