# import os
# import matplotlib.pyplot as plt
#
#
# def get_maturity_counts(dir_path):
#     maturity_counts = {15: 0, 16: 0, 17: 0, 19: 0}
#     file_list = os.listdir(dir_path)
#     for file_name in file_list:
#         if file_name.endswith(".txt"):
#             file_path = os.path.join(dir_path, file_name)
#             with open(file_path, 'r') as file:
#                 lines = file.readlines()
#                 for line in lines:
#                     maturity = int(line.strip().split()[0])
#                     if maturity in maturity_counts:
#                         maturity_counts[maturity] += 1
#     return maturity_counts
#
#
# def plot_maturity_counts(maturity_counts):
#     maturity_levels = ['mature', 'immature', 'semi-mature', 'extremely immature']
#     counts = [maturity_counts[15], maturity_counts[16], maturity_counts[17], maturity_counts[19]]
#
#     plt.bar(maturity_levels, counts)
#     plt.xlabel('Maturity Level')
#     plt.ylabel('Count')
#     plt.title('Maturity Distribution of All Apples')
#     plt.show()
#
#
# dir_path = r"D:\labels"  # 更改为你的txt文件路径
# maturity_counts = get_maturity_counts(dir_path)
# plot_maturity_counts(maturity_counts)

import matplotlib.pyplot as plt


def get_maturity_counts_single_image(file_path):
    maturity_counts = {15: 0, 16: 0, 17: 0, 19: 0}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            maturity = int(line.strip().split()[0])
            if maturity in maturity_counts:
                maturity_counts[maturity] += 1
    return maturity_counts


def plot_maturity_counts(maturity_counts):
    maturity_levels = ['mature', 'immature', 'semi-mature', 'extremely immature']
    counts = [maturity_counts[15], maturity_counts[16], maturity_counts[17], maturity_counts[19]]

    plt.bar(maturity_levels, counts, color=['green', 'red', 'orange', 'blue'])
    plt.xlabel('Maturity Level')
    plt.ylabel('Count')
    plt.title('Maturity Distribution of Apples in the Image')
    plt.show()


file_path = r"D:\labels\180.txt"  # 更改为你的txt文件路径
maturity_counts = get_maturity_counts_single_image(file_path)
plot_maturity_counts(maturity_counts)