####### data visualisation using matplotlib ######
import requests, json, math, datetime
from matplotlib import pyplot as plt 

lat = 21.3145
lon = 76.2180
data = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat="+str(lat)+"&lon="+str(lon)+"&appid=bad08493d0542f6af1188fcbd122984a&exclude=hourly,current,minutely")
weather_data = json.loads(data.content)

# convert temparature in kelvin to celsius
def kelvin_to_celsius(n):
    if n == 273.15:
        return 0
    elif n > 273.15:
        return math.ceil(n - 273.15)
    else:
        return math.ceil(273.15 - n)

# To Get useful data for graph representation
def get_graph_data(weather_data):
    graph_data = {}
    date, temp_min, temp_max, humidity, weather_description, wind_speed = list(), list(), list(), list(), list(), list()
    title_date = datetime.datetime.fromtimestamp(weather_data["daily"][0]["dt"])
    xlabel_title = "days (" + title_date.strftime('%Y - %B') + ")"
    for i in weather_data["daily"]:
        timestamp = datetime.datetime.fromtimestamp(i["dt"])
        date.append(timestamp.strftime('%d'))
        temp_min.append(str(kelvin_to_celsius(i["temp"]["min"])))
        temp_max.append(str(kelvin_to_celsius(i["temp"]["max"])))
        humidity.append(i["humidity"])
        weather_description.append(i["weather"][0]["description"])
        wind_speed.append(i["wind_speed"])
    
    graph_data["date"]  = date
    graph_data["humidity"]  = humidity
    graph_data["temp_min"]  = temp_min
    graph_data["temp_max"]  = temp_max
    graph_data["weather_description"]  = weather_description
    graph_data["wind_speed"]  = wind_speed
    graph_data["xlabel_title"]  = xlabel_title

    return graph_data

# To plot and show temparature and Humidity forecast graphs
def show_graphs(weather_data):
    graph_data = get_graph_data(weather_data)
    temparature_fig = plt.figure(1)

    # Plot figure for temperature
    plt.plot(graph_data["date"], graph_data["temp_min"], label = "temp_min")
    plt.plot(graph_data["date"], graph_data["temp_max"], label = "temp_max")
    plt.xlabel(graph_data["xlabel_title"])
    plt.ylabel("Temperature(C)")
    plt.title('Temperature forecast!')
    plt.legend()
    temparature_fig.show()

    # Plot figure for humidity 
    humidity_fig = plt.figure(2)
    plt.plot(graph_data["date"], graph_data["humidity"], 'o-', color = "blue", label = "humidity")
    plt.xlabel(graph_data["xlabel_title"])
    plt.ylabel("Humidity(%) ")
    plt.title('Humidity forecast!')
    plt.legend()
    humidity_fig.show()
    input()

show_graphs(weather_data)