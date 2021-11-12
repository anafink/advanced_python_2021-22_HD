path = "/Users/anafink/OneDrive - bwedu/Bachelor MoBi/5. Fachsemester/Python Praktikum/advanced_python_2021-22_HD/data/cities.csv"

import csv
import pandas as pd
import matplotlib.pyplot as plt
import math


def create_data_stucture(map_data_file):
    cities_dic = pd.read_csv(map_data_file)
    return cities_dic

def find_closest_cities(point, data_structure):
    distances = []
    for lat, lng in zip(data_structure['lat'].tolist(), data_structure['lng'].tolist()) :
        distances.append(math.dist(point,(lat,lng)))
    data_structure["Distance"] = distances
    data_structure = data_structure.sort_values(by = "Distance")
    closest_cities = data_structure.head(10)
    return closest_cities

hd = (49.4, 8.67) #Heidelberg
data_structure = create_data_stucture(path)
print(find_closest_cities(hd, data_structure))