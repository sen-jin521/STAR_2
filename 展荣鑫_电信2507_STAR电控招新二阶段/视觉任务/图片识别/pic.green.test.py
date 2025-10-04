import cv2
import numpy as np
#导入cv2库和np库

green=cv2.imread("green.1.jpg")
cv2.imshow("green",green)
cv2.waitKey(0)
#读取图片

if green is None:
    print("无法读取图片，请检查图片路径")
    exit()


hsv=cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
#令图片从BGR类型转换为HSV类型,便于颜色检测

cv2.imshow("green.0",green)
#展示原始图像

mingreen=np.array([35,43,46])
maxgreen=np.array([77,255,255])
#定义绿色的上下界

mask=cv2.inRange(hsv,mingreen,maxgreen)
#从hsv中筛选出处于规定范围的绿色，并创建掩码，绿色部分255，非绿色部分0

green1=cv2.bitwise_and(green,green,mask=mask)
#合并原图像与掩码，生成只有绿色部分的图像

cv2.imshow("green.1",green1)
#展示成果

cv2.imwrite("E:\picture\green_result.jpg",green1)
#保存成果图片

contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#在掩码中查找绿色色块的轮廓



for contour in contours:
    M=cv2.moments(contour)
    #遍历轮廓，并计算绿色色块的矩

    if M["m00"]!=0:
        #用if语句防止0作为分母的错误，防止无绿色色块的图片错误

        cx=int(M["m10"]/M["m00"])
        cy=int(M["m01"]/M["m00"])
        #分别计算绿色色块重心的x坐标和y坐标

        print(f"绿色色块的重心坐标是({cx},{cy})")

cv2.waitKey(0)
cv2.destroyAllWindows()
#杀青大吉 嘿嘿