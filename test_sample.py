from fizbuz import *

def test_answer():
    assert fizzBuzz(15)== "fizzbuzz"
    assert fizzBuzz(3) == "fizz"
    assert fizzBuzz(5) == "buzz"
    assert fizzBuzz(11)== 11

def test_3():
    object = FizzBuzz()
    assert object.play(3) == "fizz"

def test_5():
    object = FizzBuzz()
    assert object.play(5) == "buzz"

def test_15():
    object = FizzBuzz()
    assert object.play(15) == "fizzbuzz"

def test_7():
    object = FizzBuzz()
    assert object.play(7) == 7
