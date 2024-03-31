import os
import numpy as np
from sklearn.svm import SVC
import shutil  # Import shutil for copying files
# 文件夹路径和类别标签
folder_path = '/kaggle/input/kaggle/Attachment 2'
folder_path2 = '/kaggle/input/kaggle/Attachment 3'
class_labels = ['Apple', 'Carambola', 'Pear','Plum','Tomatoes']  # 根据实际情况进行修改

# 创建保存分类结果的文件夹
output_folder = '/kaggle/working/'
os.makedirs(output_folder, exist_ok=True)

# 数据准备
X_labeled = []  # 有标签样本的图像特征
y_labeled = []  # 有标签样本的类别标签
X_unlabeled = []  # 无标签样本的图像特征

# 读取有标签样本
for i, class_label in enumerate(class_labels):
    class_folder = os.path.join(folder_path, class_label)
    for image_file in os.listdir(class_folder):
        image_path = os.path.join(class_folder, image_file)
        # 在这里添加图像处理步骤，将图像转换为特征向量
        image_features = extract_features(image_path)
        X_labeled.append(image_features)
        y_labeled.append(i)

# 读取无标签样本
for image_file in os.listdir(folder_path2):
    image_path = os.path.join(folder_path2, image_file)
    # 在这里添加图像处理步骤，将图像转换为特征向量
    image_features = extract_features(image_path)
    X_unlabeled.append(image_features)

# 转换为NumPy数组
X_labeled = np.array(X_labeled)
y_labeled = np.array(y_labeled)
X_unlabeled = np.array(X_unlabeled)

# 使用有标签数据训练模型
model_svm = SVC()  # 使用不同的变量名以避免冲突
model_svm.fit(X_labeled, y_labeled)#训练模型svm，找出内在联系

# 使用模型对无标签数据进行预测
y_pred_unlabeled = model_svm.predict(X_unlabeled)

# 将有标签和伪标签数据合并
X_pseudo_labeled = np.concatenate((X_labeled, X_unlabeled), axis=0)
y_pseudo_labeled = np.concatenate((y_labeled, y_pred_unlabeled), axis=0)

# 使用伪标签数据+有标签数据一起 重新训练模型，以提高模型准确度
model_svm.fit(X_pseudo_labeled, y_pseudo_labeled)

# 循环对新的无标签样本进行分类
for image_file in os.listdir(folder_path2):
    image_path = os.path.join(folder_path2, image_file)
    image_features = extract_features(image_path)
    predicted_label = model_svm.predict([image_features])[0]
    predicted_class = class_labels[predicted_label]

    # 创建预测类别的文件夹
    output_class_folder = os.path.join(output_folder, predicted_class)
    os.makedirs(output_class_folder, exist_ok=True)

    # 将图像复制到相应的文件夹中
    output_image_path = os.path.join(output_class_folder, image_file)
    shutil.copy(image_path, output_image_path)

    print(f"图像 {image_file} 保存在文件夹 {predicted_class} 中。")