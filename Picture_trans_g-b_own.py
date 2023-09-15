import numpy as np
import matplotlib.pyplot as plt


def gray_to_binary(gray_image, threshold):
    # 将灰度图像转换为二值图像
    # gray_image: 输入的灰度图像，类型为NumPy数组
    # threshold: 二值化阈值，取值范围[0, 255]

    # 获取图像的宽度和高度
    height, width = gray_image.shape

    # 创建一个空白的二值图像数组
    binary_image = np.zeros((height, width), dtype=np.uint8)

    # 对每个像素进行二值化处理
    for i in range(height):
        for j in range(width):
            # 如果当前像素的灰度值大于阈值，则为前景（白色），否则为背景（黑色）
            if gray_image[i, j] > threshold:
                binary_image[i, j] = 255

    return binary_image


# 加载灰度图像
gray_image = plt.imread('C:/Users/Akaxi/Desktop/Akaxi_python/Sensor_learning_Akaxi/Keli_gray.jpg')

# 将灰度图像转换为二值图像
threshold = 128 # 二值化阈值
binary_image = gray_to_binary(gray_image, threshold)

# 显示二值图像
plt.imshow(binary_image, cmap='gray')
plt.axis('off')
plt.show()
