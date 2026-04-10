#Step 1: Create a module file

#Create a file named factorial.py

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
