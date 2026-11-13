
import unittest


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(40, 40), 80)

    def test_subtract(self):
        self.assertEqual(subtract(30, 15), 15)

    def test_multiply(self):
        self.assertEqual(multiply(6, 4), 24)


if __name__ == "__main__":

    print("Student Calculator Application")

    print("Addition:", add(40, 40))
    print("Subtraction:", subtract(30, 15))
    print("Multiplication:", multiply(6, 4))

    print("\nExecuting automated tests.\n")

    unittest.main(argv=['first-arg-is-ignored'], exit=False)

