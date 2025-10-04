import cv2
import numpy as np
#导入cv库和np库

green = cv2.VideoCapture("green_video.mp4")
#读取视频

if not green.isOpened():
    print("读取视频失败，请检查视频路径")
    exit()
#检查是否读取成功

fps = green.get(cv2.CAP_PROP_FPS)
width = int(green.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(green.get(cv2.CAP_PROP_FRAME_HEIGHT))
#获取视频的帧率，尺寸大小，保证生成的视频与原视频的要素一致，其中w和h设置为int，防止报错

print("width:",width)
print("height:",height)
print("fps:",fps)
#输出获取得到的要素值（非必要）

fourcc=cv2.VideoWriter_fourcc(*"XVID")
#定义输出视频的编码格式

out=cv2.VideoWriter("green_video_result.avi",fourcc,fps,(width,height))
#初始化待输出视频

while green.isOpened():
    #读取视频的每一帧
    ret, frame = green.read()
    if not ret:
        break
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #将每一帧画面都转换为HSV类型，方便颜色检测

    min_green = np.array([35, 40, 40])
    max_green = np.array([77, 255, 255])
    #定义绿色的上下限

    green_mask = cv2.inRange(hsv_frame, min_green, max_green)
    #创建掩码，使只显示绿色部分，非绿色部分为黑色

    green_1=cv2.bitwise_and(frame,frame,mask=green_mask)
    #合并原视频帧画面与掩码，生成所需要的只含绿色的帧画面

    cv2.imshow("green_video_result",green_1)
    #显示成果视频

    out.write(green_1)
    #将帧画面写入，保存

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #铵“q”可提前退出

green.release()
out.release()
cv2.destroyAllWindows()
#杀青大吉 嘿嘿

