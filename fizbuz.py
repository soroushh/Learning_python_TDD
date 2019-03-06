def fizzBuzz(x):
    if(x%15==0):
        return("fizzbuzz")
    elif(x%3==0):
        return("fizz")
    elif(x%5==0):
        return("buzz")
    else:
        return(x)

class FizzBuzz:
    def play(self,number):
        if(number%15==0):
            return "fizzbuzz"
        elif(number%3==0):
            return "fizz"
        elif(number%5 == 0):
            return "buzz"
        else:
            return number
