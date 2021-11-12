path = "/Users/anafink/OneDrive - bwedu/Bachelor MoBi/5. Fachsemester/Python Praktikum/advanced_python_2021-22_HD/data/cities.csv"

import csv
import pandas as pd
import matplotlib.pyplot as plt
import math

with open(path, mode='r') as cities:
    reader = csv.reader(cities)
    citydict = {rows[0]:rows[2] for rows in reader}


print(citydict)