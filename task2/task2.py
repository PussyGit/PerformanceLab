# Окружность и координаты

import sys

with open(sys.argv[1], 'r') as circle_file:
    center_x, center_y = map(float, circle_file.readline().split())
    radius = float(circle_file.readline())

with open(sys.argv[2], 'r') as points_file:
    for line in points_file:
        point_x, point_y = map(float, line.split())

        distance = ((point_x - center_x) ** 2 + (point_y - center_y) ** 2) ** 0.5

        if distance == radius:
            print(0)  # Точка на окружности
        elif distance < radius:
            print(1)  # Точка внутри окружности
        else:
            print(2)  # Точка снаружи окружности

