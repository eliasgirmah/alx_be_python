#!/bin/bash
# Learn to use Match Case statements for handling multiple operations in a simple calculator program.
num1= int(input("Enter the first number:"))
num2= int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):").strip()

match operation:
    case '+':
        result= num1 + num2
        print(f"The result is {result}.")
    case '-':
        result= num1 -num2
        print(f"The result is {result}.")
    case '*':
        result= num1 * num2
        print(f"The result is {result}.")
    case '/':
        result= num1 / num2 if num2 != 0 else "Cannot divide by zero."
        print(f"The result is {result}.")

