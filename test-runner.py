import unittest
import importlib

class TestAssignmentFour(unittest.TestCase):
    def test_01(self):
        self.assertEqual(asgmt.check_data_type(1), 'int')
        self.assertEqual(asgmt.check_data_type(1.0), 'float')
        self.assertEqual(asgmt.check_data_type(False), 'bool')
        self.assertEqual(asgmt.check_data_type(True), 'bool')
        self.assertEqual(asgmt.check_data_type('5566'), 'str')
        self.assertEqual(asgmt.check_data_type(None), 'NoneType')
    def test_02(self):
        self.assertEqual(asgmt.check_data_structure([2, 3, 5, 7, 11]), 'list')
        self.assertEqual(asgmt.check_data_structure((2, 3, 5, 7, 11)), 'tuple')
        self.assertEqual(asgmt.check_data_structure({'0': 2, '1': 3, '2': 5, '3': 7, '4': 11}), 'dict')
        self.assertEqual(asgmt.check_data_structure({2, 3, 5, 7, 11}), 'set')
    def test_03(self):
        self.assertEqual(asgmt.retrieve_first_and_last_elements([2, 3, 5]), (2, 5))
        self.assertEqual(asgmt.retrieve_first_and_last_elements([2, 3, 5, 7]), (2, 7))
        self.assertEqual(asgmt.retrieve_first_and_last_elements(["Frieren", "Heiter", "Eisen", "Himmel"]), ('Frieren', 'Himmel'))
    def test_04(self):
        self.assertEqual(asgmt.retrieve_middle_elements([2, 3, 5]), 3)
        self.assertEqual(asgmt.retrieve_middle_elements([2, 3, 5, 7]), (3, 5))
        self.assertEqual(asgmt.retrieve_middle_elements([2, 3, 5, 7, 11]), 5)
        self.assertEqual(asgmt.retrieve_middle_elements(["Heiter", "Frieren", "Himmel", "Eisen"]), ('Frieren', 'Himmel'))
    def test_05(self):
        self.assertEqual(asgmt.median([2, 3, 5, 7, 11]), 5)
        self.assertEqual(asgmt.median([2, 3, 5, 7, 11, 13]), 6.0)
        self.assertEqual(asgmt.median([11, 13, 17, 2, 3, 5, 7]), 7)
        self.assertEqual(asgmt.median([7, 11, 13, 17, 19, 2, 3, 5]), 9.0)
    def test_06(self):
        self.assertEqual(asgmt.collect_divisors(1), {1})
        self.assertEqual(asgmt.collect_divisors(2), {1, 2})
        self.assertEqual(asgmt.collect_divisors(3), {1, 3})
        self.assertEqual(asgmt.collect_divisors(4), {1, 2, 4})
        self.assertEqual(asgmt.collect_divisors(5), {1, 5})
    def test_07(self):
        self.assertFalse(asgmt.is_prime(1))
        self.assertFalse(asgmt.is_prime(4))
        self.assertFalse(asgmt.is_prime(6))
        self.assertFalse(asgmt.is_prime(8))
        self.assertFalse(asgmt.is_prime(9))
        self.assertTrue(asgmt.is_prime(2))
        self.assertTrue(asgmt.is_prime(3))
        self.assertTrue(asgmt.is_prime(5))
        self.assertTrue(asgmt.is_prime(7))
    def test_08(self):
        self.assertEqual(asgmt.list_first_n_prime_numbers(5), [2, 3, 5, 7, 11])
        self.assertEqual(asgmt.list_first_n_prime_numbers(10), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
        self.assertEqual(asgmt.list_first_n_prime_numbers(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113])
    def test_09(self):
        self.assertEqual(asgmt.swap_vowel_case('a'), 'A')
        self.assertEqual(asgmt.swap_vowel_case('b'), 'b')
        self.assertEqual(asgmt.swap_vowel_case('c'), 'c')
        self.assertEqual(asgmt.swap_vowel_case('d'), 'd')
        self.assertEqual(asgmt.swap_vowel_case('e'), 'E')
        self.assertEqual(asgmt.swap_vowel_case('A'), 'a')
        self.assertEqual(asgmt.swap_vowel_case('B'), 'B')
        self.assertEqual(asgmt.swap_vowel_case('C'), 'C')
        self.assertEqual(asgmt.swap_vowel_case('D'), 'D')
        self.assertEqual(asgmt.swap_vowel_case('E'), 'e')
    def test_10(self):
        self.assertEqual(asgmt.swap_vowels_case_in_word('Frieren'), 'FrIErEn')
        self.assertEqual(asgmt.swap_vowels_case_in_word('Himmel'), 'HImmEl')
        self.assertEqual(asgmt.swap_vowels_case_in_word('Luke Skywalker'), 'LUkE SkywAlkEr')
        self.assertEqual(asgmt.swap_vowels_case_in_word('Anakin Skywalker'), 'anAkIn SkywAlkEr')
        self.assertEqual(asgmt.swap_vowels_case_in_word('Darth Vader'), 'DArth VAdEr')
        self.assertEqual(asgmt.swap_vowels_case_in_word('Yoda'), 'YOdA')
        self.assertEqual(asgmt.swap_vowels_case_in_word('Han Solo'), 'HAn SOlO')
        
asgmt = importlib.import_module("answers")
suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignmentFour)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print(f"You've got {number_of_successes} successes among {number_of_test_runs} questions.")