#my version attempt
number1 = int(input("Enter a number:" ))
factorial = number1

while number1 > 1:
    factorial = factorial * (number1  - 1)
    number1 = number1 - 1

print(factorial)

#example version
def factorial(number):

    return 1 if (number==1 or number==0) else number * factorial(number-1)

num = 5
print("Factorial of", num,"is",factorial(num))