import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import styled from "styled-components";
import Fab from "@mui/material/Fab";
import AddIcon from "@mui/icons-material/Add";
import { orange } from "@mui/material/colors";
import Like from "../components/Like";
import { loadContentDB, loadMoreContentDB } from "../redux/modules/contentSlice";
import image from "../assets/css/asd.png"

const Contents = () => {
  const data = useSelector((state) => state.content.content_list);
  console.log(data)
  const navigate = useNavigate();
  const dispatch = useDispatch()
  const username = localStorage.getItem("nickname");
  const [region, setRegion] = useState();
  // const [images, setImages] = useState({});


  const regionChange = (e) => {
    setRegion(e.target.value);
    navigate(`/region/${e.target.value}`);
  };
  const [target, setTarget] = useState(null);
    // 무한스크롤 관련 intersection observer
    // page를 넘겨주면서 백엔드 쪽에서 몇번부터 시작해서 가져올지
    const onIntersect = async ([entry], observer) => {
        //entry.isIntersecting은 내가 지금 target을 보고있니?라는 뜻 그 요소가 화면에 들어오면 true 그전엔 false
        if (entry.isIntersecting) {
            // observer.unobserve(entry.target); // 이제 그 target을 보지 않겠다는 뜻
            await dispatch(loadMoreContentDB());

        }
    };
    useEffect(() => {
        let observer;
        if (target) {
            observer = new IntersectionObserver(onIntersect, {
                threshold: 1,
            });
            observer.observe(target); // target을 보겠다!
        }
        return () => {
            observer && observer.disconnect();
        };
    }, [target]);

  //   useEffect(() => {
  //     const fetchImages = async () => {
  //       try {
  //         const newImages = {};
  //         await Promise.all(
  //           data.map(async (v) => {
  //             const response = await fetch(`http://localhost:8000/photos/static/${v.author_id}/${v.id}`);
  //             if (!response.ok) {
  //               const errorText = await response.text();
  //               throw new Error(`HTTP error! status: ${response.status}, message: ${errorText}`);
  //             }
  //             const imageData = await response.json();
  //             console.log("Fetched image data:", imageData);
              
  //             // 첫 번째 이미지를 썸네일로 설정
  //             // newImages[v.id] = imageData.length > 0 ? imageData[0] : null; // 첫 번째 이미지를 저장
  //             newImages[v.id] = imageData[0];
  //           })
  //         );
  //         setImages(newImages);
  //       } catch (error) {
  //         console.error("Error fetching images:", error);
  //       }
  //     };

  //   fetchImages();
  // }, []);

  const color = orange[500];
  return (
    <Wrap>
      <h1>중고거래 인기매물</h1>
      <Nav>
        <select onChange={regionChange} value={region}>
          <option value="default">지역을 선택하세요</option>
          <option value="서울특별시">서울특별시</option>
          <option value="경기도">경기도</option>
          <option value="부산광역시">부산광역시</option>
          <option value="대구광역시">대구광역시</option>
          <option value="인천광역시">인천광역시</option>
          <option value="광주광역시">광주광역시</option>
          <option value="대전광역시">대전광역시</option>
          <option value="울산광역시">울산광역시</option>
          <option value="제주특별자치도">제주도</option>
        </select>
      </Nav>
      <CardList>
        {data.map((v,i) => (
          <Card key={v.post.id} ref={i === data.length - 1 ? setTarget : null}>
            <img
              // src={v.imagefile[0]}
              // src={image}
              src={`http://localhost:8000/${v.photo.image_src}`|| {image}}
              onClick={() => {
                navigate(`/detail/${v.post.id}`);
              }}
              alt=""
            ></img>
            <h2>{v.post.title}</h2>
            <div>{v.post.price}원</div>
            <div>{v.post.location}</div>
            <Like
              likeCnt={v.post.like}
              commentCnt={v.commentCnt || 0}
              postID={v.post.id}
            ></Like>
          </Card>
        ))}
      </CardList>
      {username && (
        <Fab
          color="primary"
          aria-label="add"
          style={{
            backgroundColor: color,
            position: "fixed",
            bottom: "10px",
            right: "10px",
          }}
          onClick={() => {
            navigate("/write");
          }}
        >
          <AddIcon />
        </Fab>
      )}
    </Wrap>
  );
};

const Wrap = styled.div`
  /* height: 100vh; */
  /* flex: 1; */
  /* background-color: green; */
  /* padding-top: 150px; */

  h1 {
    padding-top: 150px;
    font-size: 32px;
    font-weight: 600;
    margin-bottom: 30px;
    width: 100%;
    text-align: center;
  }
`;
const Nav = styled.nav`
  width: 83%;
  text-align: right;
  margin-bottom: 30px;
  select {
    border: 1px solid;
    border-radius: 5px;
    padding: 10px;
    width: 15%;
    height: 50px;
  }
`;
const CardList = styled.div`
  width: 80%;
  margin: 0 auto;
  margin-bottom: 50px;
  /* display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  gap: 10px; */
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  gap: 30px;
`;
const Card = styled.div`
  margin-top: 20px;
  width: 19%;
  /* width: calc(70% - 44px); */
  left: 35px;
  img {
    border-radius: 10px;
    width: 100%;
    height: 250px;
    box-sizing: border-box;
    cursor: pointer;
  }
  h2 {
    width: 100%;
    margin-top: 10px;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
    font-weight: normal;
  }
  div {
    margin-top: 10px;
  }
  span {
    margin-right: 10px;
    color: #868e96;
  }
`;

export default Contents;
