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
	def test_FizzBuzzValidFizz(self):
                #Testing NumbersDivby3
		result = FizzBuzz.SingleNumber(3)
		self.assertEqual(result, "Fizz")
		
		
		result = FizzBuzz.SingleNumber(6)
		self.assertEqual(result, "Fizz")
		
		result = FizzBuzz.SingleNumber(9)
		self.assertEqual(result, "Fizz")
		
		result = FizzBuzz.SingleNumber(36)
		self.assertEqual(result, "Fizz")

		result = FizzBuzz.SingleNumber(78)
		self.assertEqual(result, "Fizz")

	def test_FizzBuzzValidBuzz(self):


		result = FizzBuzz.SingleNumber(5)
		self.assertEqual(result, "Buzz")
		
		
		result = FizzBuzz.SingleNumber(10)
		self.assertEqual(result, "Buzz")
		
		result = FizzBuzz.SingleNumber(85)
		self.assertEqual(result, "Buzz")
		
		result = FizzBuzz.SingleNumber(25)
		self.assertEqual(result, "Buzz")

		result = FizzBuzz.SingleNumber(50)
		self.assertEqual(result, "Buzz")
		


if __name__ == "__main__":
        unittest.main()
