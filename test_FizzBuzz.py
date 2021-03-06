import unittest
import FizzBuzz
class test_FizzBuzz(unittest.TestCase): 
	def test_FizzBuzzValidNumber(self):
                #Testing Numbers
		result = FizzBuzz.SingleNumber(1)
		self.assertEqual(result, 1)
		
		
		result = FizzBuzz.SingleNumber(2)
		self.assertEqual(result, 2)
		
		
		result = FizzBuzz.SingleNumber(4)
		self.assertEqual(result, 4)
		result = FizzBuzz.SingleNumber(16)
		self.assertEqual(result, 16)
		
		result = FizzBuzz.SingleNumber(44)
		self.assertEqual(result, 44)

		result = FizzBuzz.SingleNumber(79)
		self.assertEqual(result, 79)


if __name__ == "__main__":
        unittest.main()
