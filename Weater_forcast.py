import requests
import tkinter as tk

def get_weather():
    api_key = '8f432ad4340b5b0ea98765cc2018d85d'  # Replace 'YOUR_API_KEY_HERE' with your actual API key
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'

    city = location_entry.get()
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"

    response = requests.get(complete_url)
    weather_data = response.json()

    if weather_data['cod'] != '404':
        temperature_label.config(text=str(weather_data['main']['temp']) + "°C")
        humidity_label.config(text=str(weather_data['main']['humidity']) + "%")
        wind_speed_label.config(text=str(weather_data['wind']['speed']) + " km/h")
        pressure_label.config(text=str(weather_data['main']['pressure']) + " hPa")
        precipitation_label.config(text=str(weather_data['clouds']['all']) + "%")
    else:
        temperature_label.config(text="City Not Found")
        humidity_label.config(text="")
        wind_speed_label.config(text="")
        pressure_label.config(text="")
        precipitation_label.config(text="")

root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")  # Set the initial size of the window

# Adding more empty labels for increased spacing
empty_label1 = tk.Label(root, text="", font=("Arial", 12))
empty_label1.grid(row=0, column=0, columnspan=2)
empty_label2 = tk.Label(root, text="", font=("Arial", 12))
empty_label2.grid(row=0, column=1, columnspan=2)
empty_label3 = tk.Label(root, text="", font=("Arial", 12))
empty_label3.grid(row=0, column=2, columnspan=2)

location_label = tk.Label(root, text="Location:", font=("Arial", 12))
location_label.grid(row=0, column=4, sticky='n')

location_entry = tk.Entry(root, font=("Arial", 12), width=20)
location_entry.grid(row=0, column=5, sticky='n')

empty_label4 = tk.Label(root, text="", font=("Arial", 12))
empty_label4.grid(row=0, column=6, columnspan=2)
empty_label5 = tk.Label(root, text="", font=("Arial", 12))
empty_label5.grid(row=0, column=7, columnspan=2)
empty_label6 = tk.Label(root, text="", font=("Arial", 12))
empty_label6.grid(row=0, column=8, columnspan=2)

search_button = tk.Button(root, text="Search", command=get_weather, font=("Arial", 12))
search_button.grid(row=0, column=10, sticky='n')

temperature_label = tk.Label(root, text="", font=("Arial", 14))
temperature_label.grid(row=1, column=5)

humidity_label = tk.Label(root, text="", font=("Arial", 14))
humidity_label.grid(row=2, column=5)

wind_speed_label = tk.Label(root, text="", font=("Arial", 14))
wind_speed_label.grid(row=3, column=5)

pressure_label = tk.Label(root, text="", font=("Arial", 14))
pressure_label.grid(row=4, column=5)

precipitation_label = tk.Label(root, text="", font=("Arial", 14))
precipitation_label.grid(row=5, column=5)

# Labels explaining weather parameters with increased space and bold font
temp_desc_label = tk.Label(root, text="Temperature:", font=("Arial", 12, "bold"))
temp_desc_label.grid(row=1, column=4, sticky='e')

humidity_desc_label = tk.Label(root, text="Humidity:", font=("Arial", 12, "bold"))
humidity_desc_label.grid(row=2, column=4, sticky='e')

wind_speed_desc_label = tk.Label(root, text="Wind Speed:", font=("Arial", 12, "bold"))
wind_speed_desc_label.grid(row=3, column=4, sticky='e')

pressure_desc_label = tk.Label(root, text="Pressure:", font=("Arial", 12, "bold"))
pressure_desc_label.grid(row=4, column=4, sticky='e')

precipitation_desc_label = tk.Label(root, text="Precipitation:", font=("Arial", 12, "bold"))
precipitation_desc_label.grid(row=5, column=4, sticky='e')

root.mainloop()
