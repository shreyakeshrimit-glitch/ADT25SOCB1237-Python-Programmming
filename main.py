#Step 2: Main program to import module

Create another file, for example main.py

import factorial

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    result = factorial.factorial(num)
    print("Factorial of", num, "is", result)