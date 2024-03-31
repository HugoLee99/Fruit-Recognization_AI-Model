import os
import cv2


def batch_enhance_contrast(input_dir, output_dir):
    # 创建输出目录
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 获取输入目录中的所有图像文件
    image_files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]

    for filename in image_files:
        # 读取图像
        image_path = os.path.join(input_dir, filename)
        image = cv2.imread(image_path)

        # 对比度增强
        enhanced_image = enhance_contrast(image)

        # 保存增强后的图像，输出文件名与输入文件名保持一致
        output_path = os.path.join(output_dir, filename)
        cv2.imwrite(output_path, enhanced_image)

        print(f"Processed: {filename}")


def enhance_contrast(image):
    # 将彩色图像转换为YUV颜色空间
    yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)

    # 对Y通道应用直方图均衡化
    yuv_image[:, :, 0] = cv2.equalizeHist(yuv_image[:, :, 0])

    # 将图像转换回BGR颜色空间
    enhanced_image = cv2.cvtColor(yuv_image, cv2.COLOR_YUV2BGR)

    return enhanced_image


input_directory = "data/images"
output_directory = "data/enhanced_images"

batch_enhance_contrast(input_directory, output_directory)