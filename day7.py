# -*- coding: utf-8 -*-
"""Day7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TPB2UzPad2QwAgJzDIeCIOdSbELIXwoE
"""

# shopping_list = ["Milk", "Eggs", "Bread"]
# #print(shopping_list[1])

# shopping_list.append("Butter")
# shopping_list.insert(1, "Juice")

# print(shopping_list)

# shopping_list.sort()
# print(shopping_list)

# shopping_list.reverse()

# print(shopping_list)

# shopping_list.clear()
# print(shopping_list)

# # shopping_list.remove("Bread")
# # print(shopping_list)

# # shopping_list.pop(0)
# # print(shopping_list)

# # for item in shopping_list:
# #     print(f"- {item}")

# # for index, item in enumerate(shopping_list):
# #     print(f"{index + 1}. {item}")

# Shopping List App

# Step 1: Initialize an empty shopping list
shopping_list = []

# Step 2: Define the main menu
def show_menu():
  print("\n--- Shopping List Menu ---")
  print("1. View the shopping list")
  print("2. Add an item")
  print("3. Remove an item")
  print("4. Clear List")
  print("5. Exit")

# Step 3: Main Program Loop
while True:
  show_menu()
  choice = input("Enter your choice (1-5): ")

  if choice == "1":
    print("\n--- Shopping List ---")
    if not shopping_list:
      print("Your shopping list is empty.")
    else:
      for index, item in enumerate(shopping_list):
        print(f"{index + 1}. {item}")

  elif choice == "2":
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"{item} has been added to the shopping list.")

  elif choice == "3":
    item = input("Enter the item to remove: ")
    if item in shopping_list:
      shopping_list.remove(item)
      print(f"{item} has been removed from the shopping list.")
    else:
      print(f"{item} is not in the shopping list.")

  elif choice == "4":
    shopping_list.clear()
    print("The shopping list has been cleared.")

  elif choice == "5":
    print("Goodbye! Happy Shopping!")
    break

  else:
    print("Invalid choice. Please try again.")