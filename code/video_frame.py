import cv2
import numpy as np
import matplotlib.pyplot as plt

freezeFlag = False
font = cv2.FONT_HERSHEY_SIMPLEX

left_x=1000        #Left_x좌표---> 최소 x
left_y=0              #Left_y좌표---> 최소 y
right_x = 0          #Right_x좌표--->최대 x
right_y = 1000     #Right_y좌표--->최대 y


cv2.namedWindow('videoWindow')
cap = cv2.VideoCapture('./Bounding_box_Test01.mp4')

while(cap.isOpened()):
  if not freezeFlag: #화면 재생
    ret, frame = cap.read()
    img=cv2.resize(frame, None, fx=0.5, fy=0.5) #영상 너무 커서 화면 줄임
    #rows, cols = img.shape[:2]
    frameCopy=frame.copy()
  
    #img_gray=cv2.cvtColor(frame ,cv2.COLOR_BGR2GRAY)

  #######################1. 추가하는 부분####################################
  # 								          		 #
  # 								          		 #
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # cvtColor 함수를 이용하여 hsv 색공간으로 변환
    lower_red = (230, 30, 30) # hsv 이미지에서 바이너리 이미지로 생성
    upper_red = (255, 80, 70)
    img_mask = cv2.inRange(img_hsv, lower_red, upper_red)

    # 바이너리 이미지를 마스크로 사용하여 원본이미지에서 범위값에 해당하는 영상부분을 획득
    img_result = cv2.bitwise_and(img, img, mask = img_mask)

    # mask 배열에서 도형 윤곽의 좌표값들을 가져오기
    #contours, hierarchy = cv2.findContours(img_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    #한 줄의 코드로 윤곽선들의 좌표를 가져왔다.
    #위 코드에서 contours는 numpy배열을 담고 있는 리스트이고, 리스트에서 각각의 배열들은 윤곽선들의 좌표를 담고 있다.

    img_temp = cv2.cvtColor(img_result,cv2.COLOR_BGR2GRAY) #converting to grayscale
    img_temp = img_temp.astype(np.uint8)

    #get all non zero values
    coord = cv2.findNonZero(img_temp)
  # 								          		 #
  # 		           출처: https://sikaleo.tistory.com/84 [SIKALEO]		         	 #
  # 		           출처:https://krcodeblog.com/blog/456036				 #
  # 								          		 #				          		 #
  #####################################################################

    
    cv2.imshow('videoWindow' ,img)

  else:
     cv2.imshow('videoWindow', img)

  c = cv2.waitKey(10)
  print("coord = ", coord)   # x, y 좌표

  if c==27:
    break

cap.release()
