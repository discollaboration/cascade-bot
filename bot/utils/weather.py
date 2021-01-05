from discord import Embed
from py_owm import Weather

img_url = "https://openweathermap.org/img/wn/{code}@2x.png"

def format_weather(w: Weather):
    data = f"In {w.name}, {w.sys['country']} it's {w.get_human_weather()}, "
    data += f"the temperature is {round(w.temp - 273.15, 3)}°c,\nthe humidity is {w.humidity}, "
    data += f"and the wind speed is {round(w.wind['speed'], 3)} mph."
    return data

def ftemp(temp: float):
    return str(round(temp - 273.15, 3)) + "°c"

def fwind(wind: dict):
    speed = wind.get("speed", None)
    gust = wind.get("gust", None)
    deg = wind.get("deg", None)
    speed = f"{speed} mph" if speed else "N/A"
    gust = f"{gust} mph" if gust else "N/A"
    deg = f"{deg}°" if deg else "N/A"
    return f"Speed: {speed}\nGust: {gust}\nDirection: {deg}"

def weather_embed(w: Weather):
    description = format_weather(w)

    e = Embed(title=f"Weather in {w.name}, {w.sys['country']}", description=description, colour=0x87ceeb)
    e.set_thumbnail(url=img_url.format(code=w.weather[0]["icon"]))
    e.add_field(name="Lat/Long", value=f"{w.latitude}/{w.longitude}")
    e.add_field(name="Weather", value=f"Type: {w.weather[0]['main']}\nSubtype: {w.weather[0]['description']}")
    e.add_field(name="Wind", value=fwind(w.wind))
    e.add_field(name="Visibility", value=f"{w.visibility}")
    e.add_field(name="Temperature", value=f"Current: {ftemp(w.temp)}\nMin: {ftemp(w.temp_min)}\nMax: {ftemp(w.temp_max)}\nFeels like: {ftemp(w.feels_like)}")
    e.set_footer(text=f"Timestamp: {w.timestamp}")

    return e