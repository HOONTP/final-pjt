# [프로젝트 이름]

HOONCHUL

< 이상훈의 'HOON' + 황호출의 'CHUL'의 합성어로, 서로의 개성을 나타내는 글자들로 팀의 색깔을 강조하였다. >





## 🧑‍🤝‍🧑팀원

| 이름   | 담당 업무                                                    | Github                          |
| :----- | ------------------------------------------------------------ | ------------------------------- |
| 이상훈 | \- 프론트엔드(30%) / 백엔드(70%)<br />\- DB 모델링, 백엔드 데이터 로직 작성 | https://github.com/HOONTP       |
| 황호철 | - 프론트엔드(70%) / 백엔드(30%)<br />- 프론트엔드 기능 구현 및 디버깅, 테스트 | https://github.com/HocheolHwang |





## 📅개발 일지

| No.  | 날짜          | 이름   | 변경사항                                  |
| ---- | ------------- | ------ | ----------------------------------------- |
| 1    | 23/11/15      | 이상훈 | 아이디어 및 컨셉 구상                     |
| 2    | 23/11/15      | 황호철 | 아이디어 및 컨셉 구상                     |
| 3    | 23/11/16 - 17 | 이상훈 | Django 모델링 및 ERD 작업                 |
| 4    | 23/11/16 - 17 | 황호철 | Vue - Views.vue 및 Component 구상         |
| 5    | 23/11/20      | 이상훈 | TMDB API 데이터 추출 및 데이터 가공       |
| 6    | 23/11/20      | 황호철 | Component 구성 및 유저 페이지 작업        |
| 7    | 23/11/21-22   | 이상훈 | Django 기능 구현 및 영화 페이지 작업      |
| 8    | 23/11/21-22   | 황호철 | 게시판/프로필 Vue 구현 및 Django 연결     |
| 9    | 23/11/23-24   | 이상훈 | Django 상세 기능 구현 및 에러 디버깅 작업 |
| 10   | 23/11/23-24   | 황호철 | Vue 세부 동작 수정 및 CSS 작업            |





## 🥇목표 서비스

### 프로젝트 목표

- 영화 데이터 기반 추천 서비스 구성
- 영화 추천 알고리즘 구성
- 커뮤니티 서비스 구성
- 서비스 관리 및 유지보수



### 필수 요구사항

| No.  | 구분               | 요구사항                                                     | 구현 정도 (⭐5) |
| ---- | ------------------ | ------------------------------------------------------------ | -------------- |
| 1    | 영화 데이터        | - 50개 이상의 영화 정보 데이터<br />- 데이터는 fixtures를 사용하여 언제든 load 가능 | ⭐⭐⭐⭐⭐          |
| 2    | 영화 추천 알고리즘 | - 사용자에게 1개 이상의 영화 추천<br />- 추천 시스템 구현 방법에 대한 기술적 설명 | ⭐⭐⭐⭐⭐          |
| 3    | API                | - API 사용 (사용하는 API에 제한 없음)                        | ⭐⭐⭐⭐⭐          |
| 4    | 커뮤니티           | - 유저간 소통 할 수 있는 커뮤니티 기능 구현<br />- 다양한 아이디어로 자유롭게 구현 | ⭐⭐⭐⭐⭐          |
| 5    | README             | - README 작성                                                | ⭐⭐⭐⭐⭐          |
| 6    | 기타               | - 5개 이상의 URL 및 페이지 구성<br />- 상황에 맞는 HTTP response stauts code 반환<br />- .gitignore 파일 사용 | ⭐⭐⭐⭐⭐          |



### 서비스 구현

| No.  | 기능               | 기능 설명                                                    | 구현 정도 (⭐5) |
| ---- | ------------------ | ------------------------------------------------------------ | -------------- |
| 1    | 영화 데이터        | 영화 데이터를 db에 저장 및 가공<br />영화 목록 페이지에서 인기 영화 목록을 볼 수 있음. |                |
| 2    | 영화 추천 알고리즘 | 좋아요를 누른 영화를 기반으로 감독과 장르 및 인기도를 고려<br />5개의 영화를 추천함. |                |
| 3    | API                | API를 이용하여 영화 데이터를 받고 영화 포스터 및 배우 사진을 제공함. |                |
| 4    | 커뮤니티           | 여러 개의 게시판을 구현하여 원하는 주제의 게시판에 글을 쓰고 볼 수 있음. 댓글 및 좋아요를 통해 유저 간의 소통을 지원. |                |
| 5    | 프로필             | 사진과 자기소개 작성. 사용자가 작성한 글과 좋아요한 데이터를 볼 수 있음. |                |
| 6    |                    |                                                              |                |





## 🖥️데이터베이스 모델링(ERD)

<!--[ERD 이미지]-->





## 🛠️컴포넌트 구조

<!--[컴포넌트 이미지]-->





## 📊서비스 플로우 차트

<!--[컴포넌트 이미지]-->





## 📽️영화 추천 알고리즘

사용자가 좋아요를 누른 선호 영화를 기반으로 아래의 조건으로 추천함. ( 5개 이상 시 )

1. 선호 영화의 감독이 찍은 영화

2. 선호 영화의 장르

   - 영화 개수에 따라 장르별 가점 부여

3. 영화의 인기도

4. 영화의 평점

   각 조건은 최대 50점까지 계산되어 합계.

   점수가 높은 순으로 5개의 영화를 추천함.



## 📝서비스 대표 기능

<!--서비스 대표 기능에 대한 설명-->

| No.  | 구분                                        | 기능 | 기능 설명 |
| ---- | ------------------------------------------- | ---- | --------- |
| 1    | 영화 추천 알고리즘                          |      |           |
| 2    | 소통이 가능한 커뮤니티                      |      |           |
| 3    | 좋아요를 이용한<br />선호 영화 및 리뷰 저장 |      |           |
| 4    |                                             |      |           |
| 5    |                                             |      |           |
| 6    |                                             |      |           |



## 🔗배포 서버 URL

<!--배포 서버 URL-->





## 🍻후기

#### 이상훈

< 아쉬웠던 점 >

인증과 권한에 대한 부분을 깊게 이해하지 못 했음.

인증되지 않은 유저에 대해 기능을 허가 해줬을 때 유저의 정보가 데이터로 넘어오지 않는 부분을 해결하지 못 했다. 간단한 해결책으로는 허가할 기능과 인증을 필요로 하는 기능을 다른 함수로 구현할 수 있을 것 같다.



< 재밌었던 점 >

전체적으로 프로젝트를 진행하는 동안 작업물을 만들어가는 과정이 모두 재밌었다.

기능에 대한 학습을 할 때보다 프로젝트를 진행하며 배운 부분이 굉장히 많았고 결과를 만들어가는 재미가 있었따. 



< 느낀점 >

프로젝트 경험에 대한 중요성을 알 수 있는 기회였다.

많은 학습량 뿐 아니라 아이디어 구상 그리고 팀원 과의 소통이 얼마나 중요한지 알게되었고, 특히 기능을 구현하는 과정에서 조차 소통이 많이 필요했고 그만큼 계획 명세서에 대한 중요도를 느낄 수 있었다.





#### 황호철

< 아쉬웠던 점 >

처음부터 완벽한 설계를 가지고 프로젝트를 진행한 것이 아니다 보니, 전체적으로 코드가 통일성을 가지지 못하거나 비효율적인 코드가 존재하는 것이 아쉬웠다. 


< 재밌었던 점 >

내 생각대로 만들어가는 과정이 매우 재미있었다. 마치 게임을 하는 것처럼 계획에 맞춰 만들어 가고 문제를 해결해나가는 과정이 즐거웠다.


< 느낀점 >

2학기에 대비해 프로젝트 경험을 할 수 있어서 좋았다. 이번에는 운이 좋게도 서로 잘 할 수 있는 부분이 달라서 역할분담이 매우 잘 되었다. 앞으로의 프로젝트에서도 역할 분담, 그리고 팀원 구성이 매우 중요할 것이라고 느꼈다.



