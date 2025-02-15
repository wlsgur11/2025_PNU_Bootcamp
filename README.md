# 2주 당근마켓

<div align="center">
<img width="329" alt="image" src="https://raw.githubusercontent.com/wlsgur11/2025_PNU_Bootcamp/232739b75cb25ba6c1c2f4c122d5106e0c3253e9/Frontend/frontend/src/assets/css/logo.svg">

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fwlsgur11%2F2025_PNU_Bootcamp&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
</div>

<br/>

# 2주 당근마켓 Web Page v1.0
> **2025 PNU Mini Bootcamp - BE with 멋쟁이사자처럼** <br/> **개발기간: 2025.02.03 ~ 2025.02.14**

<br/>

## 웹개발팀 소개

|문진혁|                                                                                                              
| :------: | 
| <img src="https://github.com/wlsgur11.png" width="100"> | 
| 부산대학교 정보컴퓨터공학부 4학년 | 
| **백엔드** |

<br/>

## 프로젝트 소개

2주간의 부트캠프 과정에서 학습한 게시판의 이해를 기반으로 새로운 서비스가 아닌 기존의 존재하는 서비스의 기능을 비슷하게 만들어 보는 프로젝트.
프론트는 다른 깃허브 참조: [daangn_front](https://github.com/devmin24/daangn_front)

#### 스스로 처음부터 만들어 보기
chat GPT를 사용하지 않음으로써 프로그래밍, 디버깅 실력 향상과 프로젝트의 완벽한 이해를 바탕으로 한 개발

<br/>

## 시작 가이드
### 로컬
#### 백엔드
- [Python 3.12.0+](https://www.python.org/downloads/release/python-3120/)
#### 프론트엔드
- [Node.js v22.13.1](https://nodejs.org/ko)

<br/>

### Installation
``` bash
$ git clone https://github.com/wlsgur11/2025_PNU_Bootcamp.git
$ cd 2025_PNU_Bootcamp
```
#### Backend
```CMD
// open CMD (sure not powershell in window os)
$ venv\Scripts\activate.bat
$ (venv) fastapi dev main.py
```

#### Frontend
```powershell
Different terminal with backend
$ cd FrontEnd
$ cd frontend
$ npm install 
$ npm run dev
```

---

## Stacks 🐈

### 개발 환경
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?style=for-the-badge&logo=Visual%20Studio%20Code&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white)
![Github](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white)             
       

### 백엔드
![fastapi](https://img.shields.io/badge/fastapi-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![sqlite](https://img.shields.io/badge/sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![sqlalchemy](https://img.shields.io/badge/sqlalchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![redis](https://img.shields.io/badge/redis-FF4438?style=for-the-badge&logo=redis&logoColor=white)
![pydantic](https://img.shields.io/badge/pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)

### 프론트엔드
![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=white)
![vite](https://img.shields.io/badge/vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)
![redux](https://img.shields.io/badge/redux-764ABC?style=for-the-badge&logo=redux&logoColor=white)
![axios](https://img.shields.io/badge/axios-5A29E4?style=for-the-badge&logo=axios&logoColor=white)
![styledcomponents](https://img.shields.io/badge/styledcomponents-DB7093?style=for-the-badge&logo=styledcomponents&logoColor=white)


### 문서
![Notion](https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white)

---
## 화면 구성 📺
| 메인 페이지  |  소개 페이지   |
| :-------------------------------------------: | :------------: |
|  <img width="329" src="https://user-images.githubusercontent.com/50205887/208036155-a57900f7-c68a-470d-923c-ff3c296ea635.png"/> |  <img width="329" src="https://user-images.githubusercontent.com/50205887/208036645-a76cf400-85bc-4fa2-af72-86d2abf61366.png"/>|  
| 강좌 소개 페이지   |  강의 영상 페이지   |  
| <img width="329" src="https://user-images.githubusercontent.com/50205887/208038737-2b32b7d2-25f4-4949-baf5-83b5c02915a3.png"/>   |  <img width="329" src="https://user-images.githubusercontent.com/50205887/208038965-43a6318a-7b05-44bb-97c8-b08b0495fba7.png"/>     |

---
## 주요 기능 📦

### ⭐️ 회원가입, 로그인
- JWT토큰을 사용한 HTTP stateless 환경의 유지 및 단점 보완

### ⭐️ 최신순 게시물 정렬, 무한 스크롤, redid 캐싱
- 한 페이지에 네개의 게시물을 불러오고 화면 끝까지 스크롤 하면 다음 페이지의 게시물들을 불러오는 무한 스크롤 기능
- 빠른 로딩을 위한 redis 캐싱 전략: in memory 캐시인 redis에 캐싱된 게시물이 아니라면 DB에 요청해서 받아오고 이미 캐싱되어 있다면 redis에서 가져오는 식으로 게시물 페이지 로딩속도 개선(게시물 20개 기준 전체 페이지 기준 기존: 5~10초, redis 적용 후: 1초 이내)

### ⭐️ 끌어올리기
- Post테이블에 created_at, updated_at을 추가하여 정렬은 업데이트 순 디테일에는 작성일자가 보이도록 나눔

## 추후 추가 기능

#### 배포
- 부트캠프에서 학습한 Amazon Lightsail을 활용하여 배포 시도

#### 채팅, 댓글
- 세션을 활용한 실시간 채팅과 댓글 기능 추가

#### 게시글 수정 방법
- 현재 수정은 기존 게시물의 정보를 등고오지 않고 처음부터 다시쓴다.

#### 검색 기능
- 현재 검색 기능은 스크롤을 하여 불러온 게시물에서 검색하는 기능이다
- api는 구현했지만 프론트에서 단어를 고르고 스크롤된 카드리스트에서 가져오는 식이라 api를 활용하지 못하는 중이다

#### 회원정보
- 회원정보 페이지의 부재로 인한 불편함

---
## 아키텍쳐

### 디렉토리 구조









```
전체 프로젝트 구조
📦2025_PNU_Bootcamp
┣ BackEnd
┃ ┣ 📂FrontEnd
┗ ┗ ┗ 📜frontend
```
```
📦BackEnd
 ┣ 📦app
 ┃ ┣ 📂dependencies
 ┃ ┣ 📜__pycache__
 ┃ ┃ ┣ 📜jwt_utils.py
 ┃ ┃ ┣ 📜redis_db.py
 ┃ ┃ ┣ 📜sqlite_db.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂models
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┣ 📜parameter_models.py
 ┃ ┃ ┣ 📜post_models.py
 ┃ ┃ ┣ 📜user_models.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂routers
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┣ 📜auth_routers.py
 ┃ ┃ ┣ 📜post_routers.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂services
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┣ 📜auth_service.py
 ┃ ┃ ┣ 📜post_service.py
 ┃ ┃ ┣ 📜redis_service.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂__pycache__
 ┃ ┃ ┣ 📜dependencies
 ┃ ┃ ┗ 📜__init__
 ┗ ┗ 📜__init__.py
```
```
📦FrontEnd
 ┣ 📂assets
 ┃ ┗ 📂css
 ┃ ┃ ┣ 📜asd.png
 ┃ ┃ ┣ 📜GlobalStyles.jsx
 ┃ ┃ ┣ 📜logo.svg
 ┃ ┃ ┣ 📜modal.css
 ┃ ┃ ┗ 📜profile.jpeg
 ┣ 📂components
 ┃ ┣ 📜CardSlide.jsx
 ┃ ┣ 📜Comment.jsx
 ┃ ┣ 📜CommentList.jsx
 ┃ ┣ 📜ContentsNotFound.jsx
 ┃ ┣ 📜Footer.jsx
 ┃ ┣ 📜Header.jsx
 ┃ ┣ 📜Like.jsx
 ┃ ┣ 📜MainBottom.jsx
 ┃ ┣ 📜MainBottom2.jsx
 ┃ ┣ 📜MainMiddle.jsx
 ┃ ┣ 📜MainTop.jsx
 ┃ ┣ 📜Modal.jsx
 ┃ ┗ 📜SearchNotFound.jsx
 ┣ 📂pages
 ┃ ┣ 📜Contents.jsx
 ┃ ┣ 📜Detail.jsx
 ┃ ┣ 📜Main.jsx
 ┃ ┣ 📜PageNotFound.jsx
 ┃ ┣ 📜RegionContent.jsx
 ┃ ┣ 📜Search.jsx
 ┃ ┗ 📜Write.jsx
 ┣ 📂redux
 ┃ ┣ 📂modules
 ┃ ┃ ┣ 📜commentSlice.jsx
 ┃ ┃ ┣ 📜contentSlice.jsx
 ┃ ┃ ┗ 📜userSlice.jsx
 ┃ ┗ 📜store.jsx
 ┣ 📂shared
 ┃ ┗ 📜axios.jsx
 ┣ 📜App.jsx
 ┗ 📜main.jsx
```

