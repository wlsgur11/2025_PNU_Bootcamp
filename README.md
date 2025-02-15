# 2주 당근마켓

<div align="center">
<img width="329" alt="image" src="https://user-images.githubusercontent.com/50205887/207568862-cdc9e2c0-b03c-43ff-bf46-3ba79a110d0c.png">

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FVoluntain-SKKU%2FVoluntain-2nd&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

</div>











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
