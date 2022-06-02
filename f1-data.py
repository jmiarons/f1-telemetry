import fastf1 as ff1
from fastf1 import plotting
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.collections import LineCollection
import numpy as np
import pandas as pd


def total_laps_plot():
    plt.rcParams['figure.figsize'] = [10, 6]

    fig, ax = plt.subplots()
    j = 0
    for i in drivers:
        ax.plot(i['LapNumber'], i['LapTime'], label=driver_list[j])
        j += 1
    ax.set(ylabel='Time', xlabel='Laps')
    ax.legend(loc='upper center')

    plt.show()

def speed_plot():
    plt.rcParams['figure.figsize'] = [10, 6]

    fig, ax = plt.subplots()
    j = 0
    for i in speed_drivers_car:
        ax.plot(i['Time'], i['Speed'], label=driver_list[j])
        j += 1
    ax.set(xlabel='Time', ylabel='Speed [Km/h]')
    ax.legend(loc='upper center')

    plt.show()



# Graphs using matplotlib
ff1.plotting.setup_mpl()

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
driver_list= ['NOR', 'RUS', 'ALO']

for i in driver_list:
    drivers.append(race.laps.pick_driver(i))
    speed_drivers.append(race.laps.pick_driver(i).pick_fastest())
    speed_drivers_car.append(race.laps.pick_driver(i).pick_fastest().get_car_data())

# Comparison between two drivers the whole race
# total_laps_plot()
speed_plot()


