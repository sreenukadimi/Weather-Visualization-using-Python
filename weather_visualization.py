import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Replace with your OpenWeatherMap API key
API_KEY = "70d78ff8ab79fec8bd819f1e852aa0c0"
CITY = "Japan"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def fetch_weather_data():
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data")
        return None

def visualize_weather(data):
    if not data:
        return

    # Extract necessary details
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    # Labels and values
    weather_params = ["Temperature (°C)", "Humidity (%)", "Wind Speed (m/s)"]
    values = [temperature, humidity, wind_speed]

    # Set Seaborn style
    sns.set_theme(style="whitegrid")

    # Create a bar chart
    plt.figure(figsize=(8, 5))
    sns.barplot(x=weather_params, y=values, palette="coolwarm")
    plt.title(f"Weather in {CITY}", fontsize=14)
    plt.ylabel("Values")
    plt.show()

if __name__ == "__main__":
    weather_data = fetch_weather_data()
    visualize_weather(weather_data)
