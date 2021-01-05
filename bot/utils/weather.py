from py_owm import Weather

def format_weather(w: Weather):
    data = f"In {w.name}, {w.sys['country']} it's {w.get_human_weather()},\n"
    data += f"the temperature is {round(w.temp - 273.15, 3)}C, the humidity is {w.humidity},\n"
    data += f"and the wind speed is {round(w.wind['speed'], 3)} mph."
    return data
