import os
import cv2
import numpy as np


def batch_normalize_images(input_dir, output_dir):
    # 创建输出目录
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 获取输入目录中的所有图像文件
    image_files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]

    for filename in image_files:
        # 读取图像
        image_path = os.path.join(input_dir, filename)
        image = cv2.imread(image_path)

        # 将图像转换为浮点类型并缩放像素值到 [0, 1] 范围内
        image = image.astype(np.float32) / 255.0

        # 执行标准化处理
        normalized_image = normalize_image(image)

        # 将像素值缩放回 [0, 255] 范围内
        normalized_image = (normalized_image * 255).astype(np.uint8)

        # 保存标准化后的图像，输出文件名与输入文件名保持一致
        output_path = os.path.join(output_dir, filename)
        cv2.imwrite(output_path, normalized_image)

        print(f"Processed: {filename}")


def normalize_image(image):
    # 执行标准化操作
    min_val = np.min(image)
    max_val = np.max(image)
    normalized_image = (image - min_val) / (max_val - min_val)

    return normalized_image


input_directory = "data/images"
output_directory = "data/normalized_images"

batch_normalize_images(input_directory, output_directory)