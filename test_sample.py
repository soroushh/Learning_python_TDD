def fizzBuzz(x):
    if(x%15==0):
        return("fizzbuzz")
    elif(x%3==0):
        return("fizz")
    elif(x%5==0):
        return("buzz")
    else:
        return(x)

def test_answer():
    assert fizzBuzz(15)== "fizzbuzz"
    assert fizzBuzz(3) == "fizz"
    assert fizzBuzz(5) == "buzz"
    assert fizzBuzz(11)== 11
