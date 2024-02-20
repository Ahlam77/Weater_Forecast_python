import requests
import tkinter as tk
from tkinter import ttk

def get_weather():
    api_key = '8f432ad4340b5b0ea98765cc2018d85d'
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    city = location_entry.get()
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"

    response = requests.get(complete_url)
    weather_data = response.json()

    update_labels(weather_data)

def update_labels(data):
    if data['cod'] != '404':
        temperature_label.config(text=str(data['main']['temp']) + "°C")
        humidity_label.config(text=str(data['main']['humidity']) + "%")
        wind_speed_label.config(text=str(data['wind']['speed']) + " km/h")
        pressure_label.config(text=str(data['main']['pressure']) + " hPa")
        precipitation_label.config(text=str(data['clouds']['all']) + "%")
    else:
        temperature_label.config(text="City Not Found")
        humidity_label.config(text="")
        wind_speed_label.config(text="")
        pressure_label.config(text="")
        precipitation_label.config(text="")

root = tk.Tk()
root.title("Weather App")

# Styling
style = ttk.Style()
style.configure('TLabel', font=('Arial', 12))
style.configure('Header.TLabel', font=('Arial', 12, 'bold'))

# Location Input
location_label = ttk.Label(root, text="Location:", style='Header.TLabel')
location_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

location_entry = ttk.Entry(root, font=("Arial", 12), width=20)
location_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')

search_button = ttk.Button(root, text="Search", command=get_weather, style='TButton')
search_button.grid(row=0, column=2, padx=10, pady=10, sticky='w')

# Weather Information Labels
weather_labels = [
    "Temperature:",
    "Humidity:",
    "Wind Speed:",
    "Pressure:",
    "Precipitation:"
]

for i, label_text in enumerate(weather_labels, start=1):
    label = ttk.Label(root, text=label_text, style='Header.TLabel')
    label.grid(row=i, column=0, padx=10, pady=5, sticky='e')

    weather_info_label = ttk.Label(root, text="", font=("Arial", 14))
    weather_info_label.grid(row=i, column=1, padx=10, pady=5, sticky='w')

    # Assign labels to global variables for update
    if i == 1:
        temperature_label = weather_info_label
    elif i == 2:
        humidity_label = weather_info_label
    elif i == 3:
        wind_speed_label = weather_info_label
    elif i == 4:
        pressure_label = weather_info_label
    elif i == 5:
        precipitation_label = weather_info_label

root.mainloop()
