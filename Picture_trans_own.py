import numpy as np
import matplotlib.pyplot as plt


def rgb_to_gray(image):
    # 将RGB图像转换为灰度图像
    # image: 输入的RGB图像，类型为NumPy数组
    # 先获取图片的尺寸
    # shape获取图片数组的长度和维度
    height, width, channels = image.shape
    gray_img = np.zeros((height, width), dtype=np.uint8)   # 创建同样大小的灰度图片numpy数组
    # 使用循环来求取每一个像素灰度值,采用不同的算法
    for i in range(height):
        for j in range(width):
            # gray_value = (image[i, j, 0] + image[i, j, 1] + image[i, j, 2]) / 3    # 均值法
            gray_value = 0.299 * image[i, j, 0] + 0.587 * image[i, j, 1] + 0.114 * image[i, j, 2]  # 加权平均法
            gray_img[i, j] = gray_value

    return gray_img


def gray_to_binary(gray_image, threshold):
    # 将灰度图像转换为二值图像
    # gray_image: 输入的灰度图像，类型为NumPy数组
    # threshold: 二值化阈值，取值范围[0, 255]

    # 获取图像的宽度和高度
    height, width = gray_image.shape
    binary_image = np.zeros((height, width), dtype=np.uint8)  # 创建同样大小的灰度图片numpy数组
    # 使用循环来对每一个像素进行二值化处理
    for i in range(height):
        for j in range(width):
            if gray_image[i, j] > threshold:  # 如果像素的灰度值大于阈值，则为白色，否则为黑色
                binary_image[i, j] = 255

    return binary_image

# 【灰度化】
# 读取图像 matplotlib获取的图片会变成numpy的数组
image = plt.imread('C:/Users/Akaxi/Desktop/Akaxi_python/Sensor_learning_Akaxi/Keli.jpg')
image2 = plt.imread('C:/Users/Akaxi/Desktop/Akaxi_python/Sensor_learning_Akaxi/fig1.jpg')

# 显示彩色图
plt.imshow(image)
plt.axis('off')
plt.show()

plt.imshow(image2)
plt.axis('off')
plt.show()

# 将彩色图像转换为灰度图像
gray_img = rgb_to_gray(image)
gray_img2 = rgb_to_gray(image2)

# 显示灰度图
plt.imshow(gray_img, cmap='gray')
plt.axis('off')
plt.show()

plt.imshow(gray_img2, cmap='gray')
plt.axis('off')
plt.show()

# 【二值化】
# 加载灰度图
gray_image = gray_img
gray_image2 = gray_img2

# 将灰度图像转换为二值图
threshold = 127  # 二值化阈值
# threshold = 200  # 二值化阈值
binary_image = gray_to_binary(gray_image, threshold)
binary_image2 = gray_to_binary(gray_image2, threshold)

# 显示二值图
plt.imshow(binary_image, cmap='gray')
plt.axis('off')
plt.show()

plt.imshow(binary_image2, cmap='gray')
plt.axis('off')
plt.show()
