from unittest import TestCase
from prime_number_function import is_prime

class Test_prime_number(TestCase):

	def test_prime(self):
		self.assertEqual(is_prime(18), False)

	def test_prime_is_true(self):
		self.assertTrue(is_prime(3))

	def test_prime_is_false(self):
		self.assertFalse(is_prime(6))

	def test_2_is_prime(self):
		self.assertEqual(is_prime(2), True)

	def test_3_is_prime(self):
		self.assertEqual(is_prime(3), True)

	def test_4_is_not_prime(self):
		self.assertEqual(is_prime(4), False)

	def test_5_is_prime(self):
		self.assertEqual(is_prime(5), True)

	def test_6_is_not__prime(self):
		self.assertEqual(is_prime(6), False)

	def test_7_is_prime(self):
		self.assertEqual(is_prime(7), True)

	def test_8_is_not_prime(self):
		self.assertEqual(is_prime(8), False)