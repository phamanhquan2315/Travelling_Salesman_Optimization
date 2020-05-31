import numpy as np
import random
import matplotlib.pyplot as plt


class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, city):
        return np.hypot(self.x - city.x, self.y - city.y)

    def __repr__(self):
        return f"({self.x}, {self.y})"


def read_cities(size):
    cities = []
    with open(f'cities_{size}.data', 'r') as handle:
        lines = handle.readlines()
        for line in lines:
            x, y = map(int, line.split())
            cities.append(City(x, y))
    return cities


def write_cities_and_return_them(size):
    cities = generate_cities(size)
    with open(f'cities_{size}.data', 'w+') as handle:
        for city in cities:
            handle.write(f'{city.x} {city.y}\n')
    return cities


def generate_cities(size):
    return [City(x=int(random.random() * 200), y=int(random.random() * 200)) for _ in range(size)]


def path_cost(route):
    distance = 0
    for index, city in enumerate(route):
        distance += city.distance(route[(index + 1) % len(route)])
    return distance


def visualize_tsp(title, cities):
    fig = plt.figure()
    fig.suptitle(title)
    x_list, y_list = [], []
    for city in cities:
        x_list.append(city.x)
        y_list.append(city.y)
    x_list.append(cities[0].x)
    y_list.append(cities[0].y)

    plt.plot(x_list, y_list, 'ro')
    plt.plot(x_list, y_list, 'g')
    plt.show(block=True)