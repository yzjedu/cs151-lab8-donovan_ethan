# Programmers: Ethan D'Souza & Donovan Raymond
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 11/6/2024
# Lab Assignment: 08
# Problem: Create a program to display the distribution of rolls of two dice.
# Purpose: Practice with lists, functions, loops, random numbers.

import random

# Function to prompt user for the number of rolls
def num_rolls():
    # Purpose: Prompt the user for the number of rolls and validate input
    rolls = input("How many times would you like to roll the dice? ")
    while not rolls.isdigit():
        print("Please enter a valid number.")
        rolls = input("How many times would you like to roll the dice? ")
    return int(rolls)

# Function to roll two dice and return their sum
def dice_roll():
    # Purpose: Roll two dice and return their sum
    num1 = random.randint(1,6)
    num2 = random.randint(1, 6)
    rolls_sum = num1 + num2
    return rolls_sum

# Function to count the occurrences of each possible sum
def match_count(num_rolls):
    # Purpose: Count the frequency of each sum (2-12) from dice rolls
    rolls_list = [0] * 11
    count = 0
    while count < num_rolls:
        sum = dice_roll()
        rolls_list[sum - 2] += 1
        count += 1
    return rolls_list

# Function to display the results as a chart
def display_result(rolls_list):
    # Purpose: Display the distribution of sums in a chart
    print("Rolling", sum(rolls_list), "pairs of dice")
    print(rolls_list)
    number = 2
    for count in rolls_list:
        stars = '*' * count
        print("Sum of", number, stars)
        number += 1

# Main function to coordinate the program
def main():
    # Purpose: Coordinate the program flow
    print("Welcome to the Dice Roll Distribution Program!")
    rolls = num_rolls()  # Get the number of rolls from the user
    rolls_list = match_count(rolls)  # Get the frequency distribution
    display_result(rolls_list)  # Display the results as a chart
    print("Thank you for using our program!")

# Directly call main to start the program
main()

