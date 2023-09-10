import tkinter as tk
import requests 

def get_weather():
    city=entry.get()
    api_key="41b959cbd215894b8cb1bc3ea1a12b45"
     
    response=requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric")
    
    
    weather_data=response.json()
    
    temperature=weather_data["main"]["temp"]

    description=weather_data["weather"][0]["description"]
    
    result_label.config(text=f"Temperature : {temperature}Celsius \n Weather : {description}")

window=tk.Tk()
window.title("Weather Forecast")

label=tk.Label(window,text="Enter city :")
label.pack()

entry=tk.Entry(window)
entry.pack()

button=tk.Button(window,text="Get Weather",command=get_weather)
button.pack()

result_label=tk.Label(window,text=" ")
result_label.pack()   

window.mainloop()