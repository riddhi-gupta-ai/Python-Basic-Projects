# Weather App using OpenWeatherMap API
import requests

#Step 1: API SETUP
API_KEY = "enter your own"
BASE_URL = "enter your own"

# Step 2: Get Weather Data
def get_weather(city):
  try:
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
      data = response.json()
      weather = {
          "City": data["name"],
          "Temperature": f"{data['main']['temp']}C",
          "Weather": data["weather"][0]['description'].title(),
          "Humidity": f"{data['main']['humidity']}%",
          "Wind Speed": f"{data['wind']['speed']}m/s"
      }
      return weather
    elif response.status_code == 404:
      print("City not found.")
    else:
      print("An error occurred. Status Code: ", response.status_code)
  except Exception as e:
    print("An error occurred: ", e)
  return None

# Step 3: Display Weather Information
def display_weather(weather):
  print("\n--- Weather Information ---")
  for key,value in weather.items():
    print(f"{key}: {value}")

# Step 4: Main Program Loop
while True:
  print("\n--- Weather App ---")
  city = input("Enter a city name (or 'q' to quit): ").strip()
  if city.lower() == 'q':
    break
  weather = get_weather(city)
  if weather:
    display_weather(weather)
