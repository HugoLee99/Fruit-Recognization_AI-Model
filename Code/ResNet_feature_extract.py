import torch
from torchvision import models, transforms
from PIL import Image

# 初始化 ResNet 模型，并将其移动到 GPU（如果可用）
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = models.resnet50(pretrained=False).to(device)

# 加载手动下载的本地权重文件
model.load_state_dict(torch.load("/kaggle/input/weight/resnet50-0676ba61.pth"))
model.eval()  # 将模型设置为评估模式

def extract_features(image_path, transform=None, target_size=224):
    """
    将图像文件转换为特征向量。
    """
    if transform is None:
        # 定义图像预处理流程
        transform = transforms.Compose([
            transforms.Resize((target_size, target_size)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])

    # 加载图像
    img = Image.open(image_path)
    img = img.convert('RGB')

    # 预处理图像并添加批量维度
    img_tensor = transform(img).unsqueeze(0).to(device)

    # 禁用梯度计算
    with torch.no_grad():
        # 提取特征
        features = model(img_tensor)

    # 将特征转换为 NumPy 数组
    features = features.squeeze(0).cpu().numpy()

    return features
