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
프론트는 다른 팀 깃허브 참조: [daangn_front](https://github.com/devmin24/daangn_front)


<br/>

#### 스스로 처음부터 만들어 보기
chat GPT를 사용하지 않음으로써 프로그래밍, 디버깅 실력 향상과 프로젝트의 완벽한 이해를 바탕으로 한 개발

<br/>

## 시작 가이드
### Requirements
For building and running the application you need:
#### 백엔드
- [Python 3.12.0+](https://www.python.org/downloads/release/python-3120/)
#### 프론트엔드
- [Node.js v22.13.1](https://nodejs.org/ko)

<br/>

### Installation
``` bash
$ git clone https://github.com/Voluntain-SKKU/Voluntain-2nd.git
$ cd Voluntain-2nd
```
#### Backend
```
$ cd strapi-backend
$ nvm use v.14.19.3
$ npm install
$ npm run develop
```

#### Frontend
```
$ cd voluntain-app
$ nvm use v.14.19.3
$ npm install 
$ npm run dev
```

---

## Stacks 🐈

### Environment
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?style=for-the-badge&logo=Visual%20Studio%20Code&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white)
![Github](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white)             

### Config
![npm](https://img.shields.io/badge/npm-CB3837?style=for-the-badge&logo=npm&logoColor=white)        

### Development
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=Javascript&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Strapi](https://img.shields.io/badge/Strapi-2F2E8B?style=for-the-badge&logo=Strapi&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=Next.js&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=Bootstrap&logoColor=white)
![Material UI](https://img.shields.io/badge/Material%20UI-007FFF?style=for-the-badge&logo=MUI&logoColor=white)

### Communication
![Slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=Slack&logoColor=white)
![Notion](https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white)
![GoogleMeet](https://img.shields.io/badge/GoogleMeet-00897B?style=for-the-badge&logo=Google%20Meet&logoColor=white)

---
## 화면 구성 📺
| 메인 페이지  |  소개 페이지   |
| :-------------------------------------------: | :------------: |
|  <img width="329" src="https://user-images.githubusercontent.com/50205887/208036155-a57900f7-c68a-470d-923c-ff3c296ea635.png"/> |  <img width="329" src="https://user-images.githubusercontent.com/50205887/208036645-a76cf400-85bc-4fa2-af72-86d2abf61366.png"/>|  
| 강좌 소개 페이지   |  강의 영상 페이지   |  
| <img width="329" src="https://user-images.githubusercontent.com/50205887/208038737-2b32b7d2-25f4-4949-baf5-83b5c02915a3.png"/>   |  <img width="329" src="https://user-images.githubusercontent.com/50205887/208038965-43a6318a-7b05-44bb-97c8-b08b0495fba7.png"/>     |

---
## 주요 기능 📦

### ⭐️ 강좌 선택 및 강의 영상 시청 기능
- Scratch, Python 2개 강좌 및 각 강좌마다 10개 가량의 강의 영상 제공
- 추후 지속적으로 강좌 추가 및 업로드 예정

### ⭐️ 강의 관련 및 단체에 대한 자유로운 댓글 작성 가능
- Disqus를 이용하여 강의 관련 질문이나 단체에 대한 질문 작성 가능

### ⭐️ 이어 학습하기 기능
- Cookie 기능을 이용하여 이전에 학습했던 내용 이후부터 바로 학습 가능

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

백엔드는 powershell 말고 cmd 사용하십쇼
백엔드 실행
```CMD
venv\Scripts\activate.bat
```
```CMD
fastapi dev main.py
```

프론트엔드 실행
```bash
npm install
```
```bash
npm run dev
```

연습용 DB 포함
