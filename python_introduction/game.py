#!/bin/bash
# this script to write a simple game in python.

# Sample options
colors = ["red", "blue", "green"]
animals = ["cat", "dog", "rabbit"]
foods = ["pizza", "banana", "carrot"]

print("Pick a color:")
for i, color in enumerate(colors, 1):
    print(f"{i}. {color}")
print("Please enter the number for your choice (e.g., 1, 2, or 3).")
color_choice = int(input("Enter the number: ")) - 1

print("\nPick an animal:")
for i, animal in enumerate(animals, 1):
    print(f"{i}. {animal}")
print("Please enter the number for your choice (e.g., 1, 2, or 3).")
animal_choice = int(input("Enter the number: ")) - 1

print("\nPick a food:")
for i, food in enumerate(foods, 1):
    print(f"{i}. {food}")
print("Please enter the number for your choice (e.g., 1, 2, or 3).")
food_choice = int(input("Enter the number: ")) - 1

# Make the story
story = f"One day, I saw a {colors[color_choice]} {animals[animal_choice]}. It was eating {foods[food_choice]}!"

print("\nHere is your story:")
print(story)
