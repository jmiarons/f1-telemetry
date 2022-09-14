import fastf1 as ff1
from fastf1 import plotting
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.collections import LineCollection
import numpy as np
import pandas as pd
import json
import sys


def formatter(data):
    # Avoids adding a new line in the array 
    # TODO search for a better way of adding a number
    aux = np.array2string(data, max_line_width=9999999999999999999)
    return aux

# Creates a json adding lap time for each lap
def total_laps_plot():
    result = []
    j = 0
    for i in drivers:
        lapNumber = formatter(i['LapNumber'].to_numpy())
        lapTime = formatter(i['LapTime'].to_numpy().astype(float))
        result.append({driver_list[j]: {'LapNumber': lapNumber, 'lapTime': lapTime}})
        j += 1

    json_string = json.dumps(result, indent=4)
    print(json_string)

# Creates a json adding speed and time per lap of all selected drivers
def speed_plot():
    result = []
    j = 0
    for i in speed_drivers_car:
        time = formatter(i['Time'].to_numpy().astype(float))
        speed = formatter(i['Speed'].to_numpy())
        # result.append({driver_list[j]: {'Time': i['Time'].to_numpy().astype(float), 'Speed': i['Speed'].to_numpy().astype(float)}})
        result.append({driver_list[j]: {'Time': time, 'Speed': speed}})
        j += 1

    json_string = json.dumps(result, indent=4)
    print(json_string)


# if I want to do modules for each type I can use this
# result[0]['Gear'] = "asdadsad,  asdsadasdasd"

# def load_session(year, circuit, session):
#     race = ff1.get_session(year, circuit, session)
#     return race


# Enable cache for downloaded data
ff1.Cache.enable_cache('cache')

year=2022
circuit='Monaco'
session='Q'

drivers = []
speed_drivers = []
speed_drivers_car = []

# Data from race and quali
race = ff1.get_session(year, circuit, session)

# Get the laps
race.load(telemetry=True, laps=True)
driver_list= ['NOR', 'ALO', 'RUS']

for i in driver_list:
    drivers.append(race.laps.pick_driver(i))
    speed_drivers.append(race.laps.pick_driver(i).pick_fastest())
    speed_drivers_car.append(race.laps.pick_driver(i).pick_fastest().get_car_data())

# Comparison between two drivers the whole race
# total_laps_plot()
speed_plot()


