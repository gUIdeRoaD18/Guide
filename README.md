# 시각장애인을 위한 보도블럭 가이드 #
----------
### 개요 ###
----------
2021년도 2학기 빅데이터 캡스톤디자인 프로젝트 통합 관리 페이지
### 팀 ###
----------
+ 팀명: Guide
+ 팀원 및 역할
   + 강민주 : yolox 적용, 보고서 작성, 포스터 제작, 캡스톤 발표 준비
   + 박윤리 : 직접 찍은 보도 블럭 사진과 영상 캠으로 결과 내기, 시연 영상 제작, 보고서 작성
   + 안해린 : make r-cnn weight생성, yolov5 적용, 보고서 작성, 캡스톤 발표 준비
### 프로젝트 내용 ###
> 시각 장애인들은 점자 블록만으로도 길을 다니기에는 많은 장애물과 위험이 있을 뿐만 아니라, 이 점자 블록마저도 아름다운 거리를 만든다는 명목으로 사라지거나, 무관심속에서 파손된 채로 방치되어 제 기능을 하지 못하고 있습니다. 이러한 이유로 시각장애인들이 길을 다닐 때, 기술적으로 도움을 주고사 "시각 장애인을 위한 보도블럭 가이드"를 만들기로 했습니다.

### 프로젝트 기능 ###
----------
    현재 따라 걷고 있는 블록을 카메라로 비추었을 때, 이 길이 블록을 따라 잘 가고 있는 것인지 알 수 있음.
    만약 맞는 길이라면 경고음이 울리지 않지만, 블록을 벗어날 경우 경고음으로 알림.
### 개발환경 ###
----------
+ python
    + Opencv
    + yolov5
    + Anaconda
+ Google Colab Pro

### 디렉터리 구조 ###
----------
```
REPORT         진행사항 관리 디렉토리
PROJECT        보고서 관련 디렉토리
CODE           학습에 필요한 소스코드 디렉토리
```

### 보고서 ###
----------
+ 프로젝트 신청서
+ 중간보고서
+ 결과보고서

### 진행사항 ###
----------
+ [Report](https://github.com/gUIdeRoaD18/Guide/tree/main/Report)
   + [보고서1](https://github.com/gUIdeRoaD18/Guide/tree/main/Report/%EB%B3%B4%EA%B3%A0%EC%84%9C1)
   + [보고서2](https://github.com/gUIdeRoaD18/Guide/tree/main/Report/%EB%B3%B4%EA%B3%A0%EC%84%9C2)
   + [보고서3](https://github.com/gUIdeRoaD18/Guide/tree/main/Report/%EB%B3%B4%EA%B3%A0%EC%84%9C3)
   + [보고서4](https://github.com/gUIdeRoaD18/Guide/tree/main/Report/%EB%B3%B4%EA%B3%A0%EC%84%9C%204)
   + [보고서5](https://github.com/gUIdeRoaD18/Guide/tree/main/Report/%EB%B3%B4%EA%B3%A0%EC%84%9C5)
   + [보고서6](https://github.com/gUIdeRoaD18/Guide/tree/main/Report/%EB%B3%B4%EA%B3%A0%EC%84%9C6)
   + [보고서7](https://github.com/gUIdeRoaD18/Guide/tree/main/Report/%EB%B3%B4%EA%B3%A0%EC%84%9C7)
   + [보고서8](https://github.com/gUIdeRoaD18/Guide/tree/main/Report/%EB%B3%B4%EA%B3%A0%EC%84%9C8)
   + [보고서9](https://github.com/gUIdeRoaD18/Guide/tree/main/Report/%EB%B3%B4%EA%B3%A0%EC%84%9C9)
   + [보고서10](https://github.com/gUIdeRoaD18/Guide/tree/main/Report/%EB%B3%B4%EA%B3%A0%EC%84%9C10)

### yolov5 ###
----------
* 사용한 weight
    + https://drive.google.com/file/d/1q2mc5-_yP1-_UW_XVv8C_kihY443b6V_/view?usp=sharing
