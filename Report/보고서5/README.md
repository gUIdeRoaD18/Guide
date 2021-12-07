## 보고서 5 ##
#### 진행사항 ####
----------
#### 내용 ####
1. Mask R-CNN Training 실습 결과
+ Data 구조
  + train_data
    - images
      - train: 22개 중 20개(val -> 2개)
    - labels
      - train: train 이미지에 바운딩 박스 씌운 것( block), 22개 중 20개( val -> 2개)

+ Sample image load

![13](https://user-images.githubusercontent.com/95543704/145059567-466fbbdb-59bb-4916-aa41-8029c70eb531.JPG)

+ 학습

![14](https://user-images.githubusercontent.com/95543704/145059647-6331f574-6157-4ec0-930c-e01ca7915f14.JPG)

+ Test on a random image
  + train image

![15](https://user-images.githubusercontent.com/95543704/145059846-010b7fad-a574-48da-8808-015985a2e5d5.JPG)

  + test

![16](https://user-images.githubusercontent.com/95543704/145059800-10f44ea2-4ea7-4bb8-94ce-bcd64195ce91.JPG)
