import unittest
from math_quiz import minmax, randomsign, operation


class TestMathGame(unittest.TestCase):

    def test_minmax(self):
        # Test if random numbers generated are within the specified range
        min_val = 19
        max_val = 10
        for _ in range(100):  # Test a large number of random values
            rand_num = minmax(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val, "Random number is out of the range")

    def test_randomsign(self):
        # Test if the operator returned is from the given set only
        result = randomsign()
        self.assertTrue(result in {'+', '-', '*'}, "Result operator does not belong to given set")

    def test_operation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (20, 0, '*', '20 * 0', 0),
                (200, 500, '-', '200 - 500', -300),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                result_problem, result_answer = operation(num1, num2, operator)
                self.assertEqual(result_problem, expected_problem, f"Problem format mismatch for {num1} {operator} {num2}")
                self.assertEqual(result_answer, expected_answer, f"Answer mismatch for {num1} {operator} {num2}")

if __name__ == "__main__":
    unittest.main()