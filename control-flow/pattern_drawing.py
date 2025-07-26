#!/bin/bash
#Utilize while loops and nested for loops to draw a simple text-based pattern.
length= int(input("Enter the size of the pattern:"))
while length >0:
    for i in range (length):
        print("*" * length, end=" ")
        print()
        i += 1
    break