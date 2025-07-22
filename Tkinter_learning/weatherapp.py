import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "746bf880d5d04de68bc202252251407"  #  WeatherAPI.com key

def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"

    try:
        response = requests.get(url)
        data = response.json()

        if "error" in data:
            weather_result.config(text=data["error"]["message"])
            return

        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        humidity = data["current"]["humidity"]
        wind = data["current"]["wind_kph"]

        weather = (
            f"City: {data['location']['name']}, {data['location']['country']}\n"
            f"Temperature: {temp}°C\n"
            f"Condition: {condition}\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind} kph"
        )

        weather_result.config(text=weather)

    except Exception as e:
        weather_result.config(text="Error fetching data.")
        print("Error:", e)

# GUI setup
root = tk.Tk()
root.title("Weather Forecast App")
root.geometry("400x300")

tk.Label(root, text="Enter City Name", font=("Helvetica", 14)).pack(pady=10)
city_entry = tk.Entry(root, font=("Helvetica", 12), justify='center')
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", font=("Helvetica", 12), command=get_weather).pack(pady=10)

weather_result = tk.Label(root, text="", font=("Helvetica", 12), justify="left")
weather_result.pack(pady=20)

root.mainloop()
