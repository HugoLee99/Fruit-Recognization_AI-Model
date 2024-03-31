# import matplotlib.pyplot as plt
#
#
# def get_apple_coordinates_in_file(file_path):
#     coordinates = []
#     with open(file_path, 'r') as file:
#         lines = file.readlines()
#         for line in lines:
#             _, x, y, _, _ = map(float, line.strip().split())
#             y = 1 - y  # 反转y坐标
#             coordinates.append((x, y))
#     return coordinates
#
#
# def plot_apple_coordinates(file_path):
#     coordinates_in_file = get_apple_coordinates_in_file(file_path)
#
#     x = [coord[0] for coord in coordinates_in_file]
#     y = [coord[1] for coord in coordinates_in_file]
#
#     plt.scatter(x, y)
#     plt.xlabel('x')
#     plt.ylabel('y')
#     plt.title('Apple Coordinates')
#     plt.show()
#
#
#
# file_path = r"D:\labels\182.txt"  # 更改为你的txt文件路径
# plot_apple_coordinates(file_path)

import os
import matplotlib.pyplot as plt


def get_apple_coordinates_in_file(file_path):
    coordinates = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            _, x, y, _, _ = map(float, line.strip().split())
            y = 1 - y  # 反转y坐标
            coordinates.append((x, y))
    return coordinates


def plot_apple_coordinates(dir_path):
    file_list = os.listdir(dir_path)
    all_coordinates = []
    for file_name in file_list:
        if file_name.endswith(".txt"):
            file_path = os.path.join(dir_path, file_name)
            coordinates_in_file = get_apple_coordinates_in_file(file_path)
            all_coordinates.extend(coordinates_in_file)

    x = [coord[0] for coord in all_coordinates]
    y = [coord[1] for coord in all_coordinates]

    plt.scatter(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Apple Coordinates')
    plt.show()


dir_path = r"D:\labels"  # 更改为你的txt文件夹路径
plot_apple_coordinates(dir_path)