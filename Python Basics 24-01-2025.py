"""Python 24-01-2025

Original file is located at
    https://colab.research.google.com/drive/17wYIIQrVslq1Z2OPv5sFaOkZ5eUULJ_6

Khushi Bagaria 
Python Basics 1 - 24/01/2025
"""
# Finding the last digit of a number:
num = int(input("Enter number: "))
res = num%10 #modulo operator gives us the remainder
print("Last digit is:", res)

# Finding the sum of digits of a 2 digit number:
num = int(input("Enter number: "))
a = num%10
b = num//10 #floor division gives us the quotient
res = a+b
print("Sum of digits of a 2 digit number is:", res)

# Finding the sum of digits of a 3 digit number (without using functions, loops, etc., only hard coding) :
num = int(input("Enter number: "))
n1 = num%10
num = num//10
n2 = num%10
num = num//10
n3 = num%10
res = n1+n2+n3
print("Sum of digits of a 3 digit number is:", res)

# Homework: Finding the sum of digits of a 6 digit number (without using functions, loops, etc., only hard coding) :
num = int(input("Enter number: "))
digit1 = num % 10
num = num // 10
digit2 = num % 10
num = num // 10
digit3 = num % 10
num = num // 10
digit4 = num % 10
num = num // 10
digit5 = num % 10
num = num // 10
digit6 = num % 10
res = digit1 + digit2 + digit3 + digit4 + digit5 + digit6
print("Sum of digits of a 6 digit number is:", res)
