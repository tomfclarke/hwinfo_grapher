import matplotlib.pyplot as plt
from .parse import *

def plot(json_array, keys):
    x = to_datetimes(extract_values(json_array, "Date"), extract_values(json_array, "Time"))

    units = find_units(keys)
    figure, axes = plt.subplots(len(units))
    if len(units) == 1:
        axes = [axes]
    figure.suptitle('HWInfo Log')

    for unit, axis in zip(units, axes):
        for key in keys:
            if unit in key:
                y = to_numbers(extract_values(json_array, key))
                axis.plot(x, y, label=key)
        axis.set(xlabel='Date/Time', ylabel=unit)
        axis.grid()
        axis.legend()

    plt.show()
