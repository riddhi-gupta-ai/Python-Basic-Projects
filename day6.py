# -*- coding: utf-8 -*-
"""Day6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vY40w31dQhYzIYUo_EMzfoqth1lN9dlV
"""

def function_name():
  # Code block inside the functuion
  print("Hello from the function")

function_name()

def greet():
  print("Hello, welcome to Python!")

greet()

def greet_user(name):
  print(f"Hello, {name}! welcome to Python!")

greet_user('Vivian')

def add(a, b):
  print(f"The sum is: {a + b}")

add(5, 4)

def multiply(a, b):
  return a * b

result = multiply(5, 4)
print("The result is: ", result)

# Basic Math Quiz Game

import random

# Step 1: Define the math question function
def generate_question():
  num1 = random.randint(1, 10)
  num2 = random.randint(1, 10)
  operator = random.choice(['+', '-', '*'])

  if operator == '+':
    answer = num1 + num2
  elif operator == '-':
    answer = num1 - num2
  else:
    answer = num1 * num2

  return f"{num1} {operator} {num2}", answer

# Step 2: Main Quiz Game Function
def math_quiz():
  score = 0
  rounds = 5

  print("\n--- Welcome to the Math Quiz Game! ---")
  print("You will be presented with math problems, and you need to provide the correct answers.")

  for i in range(rounds):
    question, correct_answer = generate_question()
    print(f"\nQuestion {i + 1}: {question}")
    user_answer = int(input("Your answer: "))

    if user_answer == correct_answer:
      print("Correct!")
      score += 1
    else:
      print(f"Wrong! The correct answer is: {correct_answer}")

  print("\n--- Game Over! ---")
  print(f"Your final score is: {score}/{rounds}")
  if score == rounds:
    print("Congratulations! You got all the questions correct.")
  elif score >= rounds // 2:
    print("Good job! You did well.")
  else:
    print("Keep practicing! You can do better next time.")


# Step 3: Run the Game
math_quiz()