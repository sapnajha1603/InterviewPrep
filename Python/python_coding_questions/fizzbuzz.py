'''
Task: Write a Python function to solve the classic FizzBuzz problem. For numbers from 1 to n:

    Print "Fizz" for numbers divisible by 3.
    Print "Buzz" for numbers divisible by 5.
    Print "FizzBuzz" for numbers divisible by both 3 and 5.
    Print the number itself for all other cases.'''

def fizzbuzz(n):
    if n%3 == 0 and n%5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n%5 == 0:
        print("Buzz")

    else:
        print(n)

number = int(input("Please enter a valid number: "))
fizzbuzz(number)