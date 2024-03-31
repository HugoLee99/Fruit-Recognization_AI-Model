import os
import matplotlib.pyplot as plt

def calculate_masses(folder_path, k, img_width, img_height):
    masses = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):  # 假设标签文件是txt格式
            total_area_per_image = 0
            with open(os.path.join(folder_path, file_name), 'r') as file:
                lines = file.readlines()
                for line in lines:
                    _, x_center, y_center, width, height = map(float, line.strip().split())
                    # 为了得到实际像素面积，��要用到原始图像的宽度和高度来进行反归一化
                    area = (width * img_width) * (height * img_height)
                    total_area_per_image += area
                mass = total_area_per_image * k  # 估算质量
                masses.append(mass)
                print(f'Total apple area in {file_name}: {total_area_per_image}')
    print(f'Total apple area in all images: {sum(masses)}')
    return masses

def plot_mass_distribution(masses):
    plt.hist(masses, bins=20, color='blue', edgecolor='black')
    plt.xlabel('Mass')
    plt.ylabel('Count')
    plt.title('Mass distribution of apples')
    plt.show()

folder_path = r"D:\labels" # 替换为你的标签文件夹路径
img_width = 270 # 替换为你的图像宽度
img_height = 185 # 替换为你的图像高度
k = 2 # 设定比例系数，此值需根据实际情况调整

masses = calculate_masses(folder_path, k, img_width, img_height)
plot_mass_distribution(masses)