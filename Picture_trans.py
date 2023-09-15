import cv2
img_path = "C:/Users/Akaxi/Desktop/Akaxi_python/Sensor_learning_Akaxi/Keli.jpg"  # 读取图片的路径
img_path2 = "C:/Users/Akaxi/Desktop/Akaxi_python/Sensor_learning_Akaxi/fig1.jpg"

# 使用opencv函数进行灰度化以及二值化

# imread 读取图像
img_cv = cv2.imread(img_path)
img_cv2 = cv2.imread(img_path2)
cv2.imshow("Color_keli", img_cv)
cv2.imshow("Color_CQUPT", img_cv2)

# 使用cvtColor函数灰度化图像
img_cv_gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
img_cv_gray2 = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray_Keli", img_cv_gray)
cv2.imshow("Gray_CQUPT", img_cv_gray2)

# 或者在imread读取图象时直接读取成灰度图像
img_cv_st = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
img_cv_st2 = cv2.imread(img_path2, cv2.IMREAD_GRAYSCALE)
cv2.imshow("Gray_read-Keli", img_cv_st)
cv2.imshow("Gray_read-CQUPT", img_cv_st2)

# 使用threshold函数二值化图像
# ret, img_cv_dua = cv2.threshold(img_cv_gray, 127, 255, cv2.THRESH_BINARY)
# ret2, img_cv_dua2 = cv2.threshold(img_cv_gray2, 127, 255, cv2.THRESH_BINARY)
ret, img_cv_dua = cv2.threshold(img_cv_gray, 200, 255, cv2.THRESH_BINARY)
ret2, img_cv_dua2 = cv2.threshold(img_cv_gray2, 200, 255, cv2.THRESH_BINARY)
cv2.imshow("Dua_Keli", img_cv_dua)
cv2.imshow("Dua_CQUPT", img_cv_dua2)
cv2.waitKey()