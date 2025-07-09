# Animal Sound Simulator

#Base Class
class Animal:
  def make_sound(self):
    print("Some generic animal sound")

# Derived Classes
class Dog(Animal):
  def make_sound(self):
    print("Woof! Woof!")

class Cat(Animal):
  def make_sound(self):
    print("Meow! Meow!")

class Cow(Animal):
  def make_sound(self):
    print("Moo! Moo!")

class Duck(Animal):
  def make_sound(self):
    print("Quack! Quack!")

# Simulator Class
class AnimalSoundSimulator:
  def __init__(self):
    self.animals = []

  def add_animal(self, animal):
    if isinstance(animal, Animal):
      self.animals.append(animal)
      print(f"{animal.__class__.__name__} added to the simulator")
    else:
      print("Invalid animal type")

  def make_all_sounds(self):
    if not self.animals:
      print("No animals in the simulator")
    else:
      print("\n--- Animal Sounds ---")
      for animal in self.animals:
        animal.make_sound()

#Main Program
simulator = AnimalSoundSimulator()

while True:
  print("\n--- Animal Sound Simulator ---")
  print("1. Add Dog")
  print("2. Add Cat")
  print("3. Add Cow")
  print("4. Add Duck")
  print("5. Make All Sounds")
  print("6. Exit")

  choice = input("Enter your choice (1-6): ")

  if choice == '1':
    simulator.add_animal(Dog())
  elif choice == '2':
    simulator.add_animal(Cat())
  elif choice == '3':
    simulator.add_animal(Cow())
  elif choice == '4':
    simulator.add_animal(Duck())
  elif choice == '5':
    simulator.make_all_sounds()
  elif choice == '6':
    print("Exiting the simulator. Goodbye!")
    break
  else:
    print("Invalid choice. Please try again.")
