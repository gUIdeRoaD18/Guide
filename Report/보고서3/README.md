## 보고서 3 ##
#### 진행사항 ####
----------
#### 내용 ####
1. yolo v5 실습 (1차 실패)
+ Data 구조
  train_data
    -images
      -train: train 이미지에 바운딩 박스 씌운 것
      -val: val 이미지에 바운딩 박스 씌운 것
    -labels
      -train: train 이미지에 바운딩 박스 씌운 것
      -val: val 이미지에 바운딩 박스 씌운 것
+ 학습
  ![3](https://user-images.githubusercontent.com/95543704/145055777-1f028617-c0c4-4ef4-8590-e2ba8a6884ea.JPG)

+ Result
  + custon dataset training 에 적혀있는 대로 똑같이 진행하였으나 정확도가 1%도 나오지 않음. 원인은 pretrained weight라고 생각하여 이 방법은 잠시 보류..
   ![4](https://user-images.githubusercontent.com/95543704/145056067-a3f0728b-f2c9-414a-a186-31e024138fcf.JPG)

+ 실습 결과
  + label
  
  ![5](https://user-images.githubusercontent.com/95543704/145056316-7f1ab0a4-01e2-411b-b7c5-b48a2dcbd565.JPG)

  + predict
  
  ![6](https://user-images.githubusercontent.com/95543704/145056359-443dfe8b-4eca-4f48-887c-9585aaac4744.JPG)

