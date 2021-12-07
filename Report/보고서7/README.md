## 보고서 7 ##
#### 진행사항 ####
----------
#### 내용 ####
1. YOLOV5로 데이터 학습
+ 다운로드한 인도 보행 영상을 기반으로 makesense.ai 사이트에서 직접 라벨링을 지정하여 train, validation 데이터를 제작.
+ 데이터 중에서 시각 장애인 보도 블럭이 있는 이미지만을 선별한 후, bounding box를 지정.

+ Data 구조
  + train_data
    - images
      - train: 325장의 보도블럭 이미지
      - val: 30장의 보도블럭 이미지
    - labels
      - train: train 이미지에 바운딩 박스 씌운 것(block)
      - val: val 이미지에 바운딩 박스 씌운 것 (block)
 
+ 학습 결과
  + yolov5 모델로 train과 val 데이터, 그리고 labeling된 각각 데이터들을 학습.
  + yolov5s와 yolov5x 두 모델로 진행하여 더 좋은 성능이 나온 weight로 test 진행
  + 가장 성능이 좋았던 yolov5x의 weight를 저장.( epoch-70, accuracy-85%)

+ Test
  
  ![17](https://user-images.githubusercontent.com/95543704/145062104-b3d182ad-4663-4901-86c8-b5abe96e6618.JPG)

