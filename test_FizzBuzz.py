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
                

        def test_FizzBuzzValidFizzBuzz(self):


                result = FizzBuzz.SingleNumber(15)
                self.assertEqual(result, "FizzBuzz")
                
                
                result = FizzBuzz.SingleNumber(30)
                self.assertEqual(result, "FizzBuzz")
                
                result = FizzBuzz.SingleNumber(45)
                self.assertEqual(result, "FizzBuzz")
                
                result = FizzBuzz.SingleNumber(60)
                self.assertEqual(result, "FizzBuzz")

                result = FizzBuzz.SingleNumber(75)
                self.assertEqual(result, "FizzBuzz")

                result = FizzBuzz.SingleNumber(90)
                self.assertEqual(result, "FizzBuzz")

        def test_PrintFizzBuzz(self):
                result = FizzBuzz.Print100()
                self.assertEqual(result, """1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz
Fizz
52
53
Fizz
Buzz
56
Fizz
58
59
FizzBuzz
61
62
Fizz
64
Buzz
Fizz
67
68
Fizz
Buzz
71
Fizz
73
74
FizzBuzz
76
77
Fizz
79
Buzz
Fizz
82
83
Fizz
Buzz
86
Fizz
88
89
FizzBuzz
91
92
Fizz
94
Buzz
Fizz
97
98
Fizz
Buzz
""")

                
if __name__ == "__main__":
        unittest.main()
