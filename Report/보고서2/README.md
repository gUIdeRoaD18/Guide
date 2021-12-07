## 보고서 2 ##
#### 프로젝트 계획 ####
----------
#### 내용 ####
1. 정보 수집
  + 데이터정보 수집- 점자 블록을 포함한 도로의 데이터를 위해 ai hub에서 공개된 자료 중에서 인도 보행 영상을 사용하기로 함
  + 인도 보행 영상 데이터
    + 뎁스 프리딕션
    + 바운딩 박스
    + 서피스 마스킹
    + 폴리곤 세그멘테이션 ( 우리는 폴리곤 세그멘테이션 데이터를 사용할 예정)
 
-인도보행영상

![1](https://user-images.githubusercontent.com/95543704/145054326-8e53a11c-a887-4b94-9727-28c82d3fa23f.JPG)

-mask

![2](https://user-images.githubusercontent.com/95543704/145054396-79f03a2d-0cae-45b9-b7d0-9c84917efc6e.JPG)

+ 기술 정보 수집
  + segmentation : 모든 픽셀의 레이블을 예측. Sementic Image Segmentation의 목적은 사진에 있는 모든 픽셀을 미리 지정된 class로 분류하는 것이다.
  + YOLACT(You Only Look At CoefficienTs) : 객체 탐지 및 분류, 그리고 Image Segmentation까지 해주는 모델. 정확도도 높고, 무엇보다 실제 영상에 사용할 만큼 빠른 성능을 보여줌.

+ 필요한 도구
  + Google Colab Pro
