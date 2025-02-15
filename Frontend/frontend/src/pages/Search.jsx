import {React, useState, useEffect} from "react";
import { useSelector } from "react-redux";
import { useNavigate, useParams } from "react-router-dom";
import styled from "styled-components";
import Fab from "@mui/material/Fab";
import AddIcon from "@mui/icons-material/Add";
import { orange } from "@mui/material/colors";
import Like from "../components/Like";
import SearchNotFound from "../components/SearchNotFound";
import image from "../assets/css/asd.png"

const Search = () => {
  const params = useParams();
  const data = useSelector((state) => state.content.content_list).filter((v) =>
    v.post.title.includes(params.search)
  );
  const username = localStorage.getItem('nickname')
  const navigate = useNavigate();
  // const [images, setImages] = useState({});

  const color = orange[500];

  // useEffect(() => {
  //   const fetchImages = async () => {
  //     try {
  //       const newImages = {};
  //       await Promise.all(
  //         data.map(async (v) => {
  //           const response = await fetch(`http://localhost:8000/photos/static/${v.author_id}/${v.id}`);
  //           if (!response.ok) {
  //             const errorText = await response.text();
  //             throw new Error(`HTTP error! status: ${response.status}, message: ${errorText}`);
  //           }
  //           const imageData = await response.json();
  //           console.log("Fetched image data:", imageData);
  //           newImages[v.id] = imageData[0];
  //         })
  //       );
  //       setImages(newImages);
  //     } catch (error) {
  //       console.error("Error fetching images:", error);
  //     }
  //   };

  //   // data가 비어있지 않을 때만 이미지를 불러옵니다.
  //   if (data.length > 0 && Object.keys(images).length === 0) {
  //     fetchImages();
  //   }
  // }, [data]); 


  return (
    <Wrap>
      <Container>
        <p className="Tname">인기 중고</p>
        {data.length !== 0 ? 
        <CardList>
          {data.map((v) => (
            <Card
              key={v.post.id}
            >
              <img src={`http://localhost:8000/${[v.photo.image_src]}`|| {image}} onClick={() => {
                navigate(`/detail/${v.post.id}`);
              }} alt=""></img>
              <h2>{v.post.title}</h2>
              <div style={{ color: "#868e96" }}>{v.post.location}</div>
              <div className="bottom">
              <div style={{ color: "#ff8a3d" }}>{v.post.price}원</div>
              <div className="LikeCnt">
              <Like likeCnt={v.post.like} commentCnt={0} postID={v.post.id}></Like>
              </div>
              </div>
            </Card>
          ))}
        </CardList>
        :
        <SearchNotFound/>
            }
      </Container>
      {username && 
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
}
    </Wrap>
  );
};

const Wrap = styled.div`
  background-color: #f8f9fa;
  padding: 100px 0 40px 0;
 
`;
const Container = styled.div`
  width: 60%;
  padding: 0 40px;
  margin-bottom: 50px;
  border-radius: 8px;
  border: 1px solid #e9ecef;
  margin: 0 auto;
  margin-bottom: 20px;
  background: #fff;
  .Tname {
    font-weight: 600;
    font-size: 18px;
    margin: 20px 85px;
  }
    
  
`;
const CardList = styled.div`
  width: 80%;
  margin: 0 auto;
  /* display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  gap: 10px; */
  /* display: flex; */
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
  /* align-items: center; */
  /* justify-content: center;
  align-items: center; */
  gap: 30px;
`;
const Card = styled.div`
  margin-top: 20px;
  width: 30%;
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

const LikeCnt = styled.div`
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
`;

export default Search;
