# Secure User Profile App

class UserProfile:
  def __init__(self, username, email, password):
    self.username = username
    self._email = email
    self.__password = password
    self.set_password(password)

  # Getter for email
  def get_email(self):
    return self._email

  # Setter for Email
  def set_email(self, new_email):
    if "@" in new_email and "." in new_email:
      self._email = new_email
      print("Email updated successfully")
    else:
      print("Invalid email format")


  # Setter for password
  def set_password(self, new_password):
    if len(new_password) < 6:
      print("Password must be at least 6 characters long")
    else:
      self.__password = new_password
      print("Password set successfully")

  # Display Profile
  def display_profile(self):
    print("\n--- User Profile ---")
    print(f"Username: {self.username}")
    print(f"Email: {self._email}")
    print(f"Password: {self.__password}")


#Main Program
users = []

def create_user():
  username = input("Enter username: ")
  email = input("Enter email: ")
  password = input("Enter password: ")
  user = UserProfile(username, email, password)
  users.append(user)
  print("User created successfully")

def view_profiles():
  if not users:
    print("No users found")
  else:
    for user in users:
      user.display_profile()

def update_email():
  username = input("Enter username to update email: ")
  for user in users:
    if user.username == username:
      new_email = input("Enter new email: ")
      user.set_email(new_email)
      return
  print("User not found")

# Main Menu

while True:
  print("\n--- Secure User Profile App ---")
  print("1. Create User")
  print("2. View All Profiles")
  print("3. Update Email")
  print("4. Exit")

  choice = input("Enter your choice(1-4): ")

  if choice == "1":
    create_user()
  elif choice == "2":
    view_profiles()
  elif choice == "3":
    update_email()
  elif choice == "4":
    print("Exiting the program")
    break
  else:
    print("Invalid choice. Please try again")
