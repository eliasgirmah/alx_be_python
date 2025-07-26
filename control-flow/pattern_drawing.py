
#Utilize while loops and nested for loops to draw a simple text-based pattern.
length = int(input("Enter the size of the pattern: "))

while length > 0:
    for i in range(length):
        for j in range(length):
            print("*", end="")  
        print()  # Moves to the next line
    break

print("Pattern complete.")
