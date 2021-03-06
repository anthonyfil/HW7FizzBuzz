def SingleNumber(x):
    if(((x/3.0) == round(x/3.0)) and ((x/5.0) == round(x/5.0))):
        return "FizzBuzz"
    if((x/3.0) == round(x/3.0)):
        return "Fizz"
    if((x/5.0) == round(x/5.0)):
        return "Buzz"
    return x
    
