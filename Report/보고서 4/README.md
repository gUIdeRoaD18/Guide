## 보고서 4 ##
#### 진행사항 ####
----------
#### 내용 ####
1. Mask R-CNN Training 실습
+ Data 
  + makesense.ai : 직접 사진의 폴리곤 모양대로 라벨링을 할 수 있음.
  
  ![7](https://user-images.githubusercontent.com/95543704/145056879-185ecfeb-01b0-4782-ae0e-3c3b2165af25.JPG)
  
  mask r-cnn을 위한 labeling을 위해 이미지에서 보도블럭만 지정함(bounding box처럼)
  
+ Data 구조
  + 전체적으로 데모를 확인하기 위해 전체 20개의 데이터 폴더 중 5개의 폴더 내 이미지만 사용함  

![8](https://user-images.githubusercontent.com/95543704/145057136-79eda92e-8e13-4b08-97a0-c99c57421557.JPG)

+ train_data
  + images
    + train
  + labels
    + train

+ sample image load

![9](https://user-images.githubusercontent.com/95543704/145057430-fadff772-51b1-4724-9a51-35b9fa3c3f9c.JPG)

+ 학습 & Result

![10](https://user-images.githubusercontent.com/95543704/145057518-b72a1564-e6d6-4c4c-a523-2e13cbac846d.JPG)

epoch 5개(default)로 학습을 진행한 결과, loss 값은 약 0.08, validation loss는 0.07정도로 준수하게 학습 됨.
그 중 val_loss가 제일 낮은 weight 2개를 저장(h5파일)하여 다른 모델의 weight로 사용해 볼 예정.

+ Test on a random image
  + train image

![11](https://user-images.githubusercontent.com/95543704/145057975-d661cf44-a23b-4f9d-be83-868c9599c362.JPG)
 
  + test image

![12](https://user-images.githubusercontent.com/95543704/145058003-509878ee-9fa9-4cb9-9a10-ea27771a8c4f.JPG)



