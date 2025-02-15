import React, { useState } from "react";
import styled from "styled-components";
import { BsFillCameraFill } from "react-icons/bs";
import { useParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import {
  createContentDB,
  updateContentDB,
} from "../redux/modules/contentSlice";
import { ImCancelCircle } from "react-icons/im";

const Write = () => {
  const dispatch = useDispatch();
  const params = useParams();
  // const username = localStorage.getItem("login_id");
  // const nickname = localStorage.getItem("nickname");
  // const address = localStorage.getItem("location");
  const post = useSelector((state) => state.content.content_list).filter(
    (v) => v.post.id === Number(params.id)
  );
  // const [region, setRegion] = useState(post[0]?.address);
  const [title, setTitle] = useState(post[0]?.title);
  const [body, setBody] = useState(post[0]?.body);
  const [price, setPrice] = useState(post[0]?.price);
  const [preview, setPreview] = useState(
    post[0]?.imagefile ? post[0]?.imagefile : []
  );
  const [location, setLocation] = useState(post?.location || "서울특별시");
  const [published, setPublished] = useState(1);
  const [prevImage, setPrevImage] = useState(post[0]?.imagefile);
  const [image, setImage] = useState([]);

  // 이미지 미리보기 기능 구현
  const uploadImage = (e) => {
    let imagelist = [];
    let filelist = [];
    for (let i = 0; i < e.target.files.length; i++) {
      console.log(e.target.files[i]);
      filelist[i] = e.target.files[i];
      let reader = new FileReader(); // 이미지 미리보기!!!
      reader.readAsDataURL(e.target.files[i]);
      reader.onload = () => {
        imagelist[i] = reader.result;
        setPreview([...preview, ...imagelist]);
      };
    }
    setImage([...image,...filelist]);
    e.target.value = "";
  };

  // const uploadImage = (e) => {
  //   let newFiles = [];
  //   let newPreviews = [];
  
  //   for (let i = 0; i < e.target.files.length; i++) {
  //     let file = e.target.files[i];
  //     newFiles.push(file);
  
  //     let reader = new FileReader();
  //     reader.readAsDataURL(file);
  //     reader.onload = () => {
  //       newPreviews.push(reader.result);
  //       // setPreview 동기 처리
  //       setPreview((prev) => [...prev, ...newPreviews]);
  //     };
  //   }
  
  //   // 최신 이미지 배열로 상태 업데이트
  //   setImage((prev) => [...prev, ...newFiles]);
  //   e.target.value = "";
  // };

  const titleChange = (e) => {
    setTitle(e.target.value);
  };
  const bodyChange = (e) => {
    setBody(e.target.value);
  };

  const priceChange = (e) => {
    setPrice(e.target.value)
  };

  const addContent = async () => {
    const formData = new FormData();
  
    // 이미지 파일 추가
    image.forEach((file) => formData.append("files", file));
  
    // 텍스트 데이터 추가
    // formData.append("name", nickname);
    formData.append("title", title);
    formData.append("price", price);
    formData.append("body", body);
    formData.append("location", location);
    formData.append("published", published);
  
    // FormData 출력 확인
    for (let pair of formData.entries()) {
      console.log(pair[0] + ", " + pair[1]);
    }
  
    // 백엔드에 form-data 전송
    dispatch(createContentDB(formData));
  };

  // const updateContent = async () => {
  //   const formData = new FormData();
  //   image.forEach((file) => formData.append("files", file));

  //   const data = {
  //     // username: username,
  //     // nickname: nickname,
  //     files: prevImage,
  //     title: title,
  //     price: price,
  //     body: body,
  //     location: location,
  //     published: published,
  //   };
  //   const json = JSON.stringify(data);
  //   const blob = new Blob([json], { type: "application/json" });
  //   formData.append("contents", blob);
  //   dispatch(updateContentDB(formData, params.id));
  // };

  const updateContent = async () => {
    const formData = new FormData();
  
    // 이미지 파일 추가 (새로 업로드된 파일들)
    image.forEach((file) => formData.append("files", file));
  
    // 기존 이미지(prevImage)를 백엔드에서 처리할 수 있도록 문자열 형태로 추가
    if (prevImage && prevImage.length > 0) {
      prevImage.forEach((file) => formData.append("files", file));
    }
  
    // 텍스트 데이터 추가
    formData.append("title", title);
    formData.append("price", price);
    formData.append("body", body);
    formData.append("location", location);
    formData.append("published", published);
  
    // FormData 출력 확인
    for (let pair of formData.entries()) {
      console.log(pair[0] + ": " + pair[1]);
    }
  
    // 백엔드에 form-data 전송
    dispatch(updateContentDB(formData, params.id));
  };

  return (
    <Container>
      <h1>{!params.id ? "중고거래 글쓰기" : "글 수정하기"}</h1>
      <ImageContainer>
        <label htmlFor="image">
          <BsFillCameraFill size="35px"></BsFillCameraFill>
          <p>
            {preview.length}
            <span>/5</span>
          </p>
        </label>
        <input
          className="image"
          id="image"
          type="file"
          multiple
          accept="image/*"
          onChange={uploadImage}
          // disabled={preview.length===5}
          onClick={(e) => {
            if (preview.length >= 5) {
              e.preventDefault();
              alert("사진은 최대 5장만 올릴 수 있어요 :)");
            }
          }}
        ></input>

        {preview &&
          preview.map((v, i) => (
            <Image key={Math.random()}>
              <ImCancelCircle
                onClick={() => {
                  setPreview(preview.filter((value, index) => index !== i));
                  setPrevImage(prevImage.filter((val, idx) => idx !== i));
                }}
                size="25px"
                style={{
                  position: "absolute",
                  right: "0",
                  cursor: "pointer",
                  color: "white",
                  mixBlendMode: "difference",
                }}
              ></ImCancelCircle>
              <img src={v} alt=""></img>
            </Image>
          ))}
      </ImageContainer>
      <input
        id="title"
        className="title"
        placeholder="글 제목"
        onChange={titleChange}
        value={title ? title : ""}
      ></input>
      
      <input
        className="price"
        placeholder="₩ 가격"
        // type="number"
        onChange={priceChange}
        value= {price ? price : ""}
      ></input>
      {/* <input id="region" className="region" value={address} readOnly></input> */}
      
      <SelectWrapper>
        <label htmlFor="location">지역 선택</label>
        <select
          id="location"
          value={location}
          onChange={(e) => setLocation(e.target.value)}
        >
          <option value="서울특별시">서울특별시</option>
          <option value="경기도">경기도</option>
          <option value="부산광역시">부산광역시</option>
          <option value="대구광역시">대구광역시</option>
          <option value="인천광역시">인천광역시</option>
          <option value="광주광역시">광주광역시</option>
          <option value="대전광역시">대전광역시</option>
          <option value="울산광역시">울산광역시</option>
          <option value="제주도">제주도</option>
        </select>
      </SelectWrapper>

      <textarea
        className="body"
        onChange={bodyChange}
        value={body}
        placeholder="게시글 내용을 작성해주세요(가품 및 판매금지품목은 게시가 제한될 수 있어요.)"
      ></textarea>

<RadioWrapper>
        <RadioButton>
          <input
            type="radio"
            id="public"
            name="published"
            value={1}
            checked={published === 1}
            onChange={() => setPublished(1)}
          />
          <label htmlFor="public">공개</label>
        </RadioButton>
        <RadioButton>
          <input
            type="radio"
            id="private"
            name="published"
            value={0}
            checked={published === 0}
            onChange={() => setPublished(0)}
          />
          <label htmlFor="private">비공개</label>
        </RadioButton>
      </RadioWrapper>

      {!params.id ? (
        <Btn
          disabled={!title || preview.length === 0 || !body || !price}
          onClick={addContent}
        >
          등록 하기
        </Btn>
      ) : (
        <Btn
          disabled={!title || preview.length === 0 || !body || !price}
          onClick={updateContent}
        >
          수정 하기
        </Btn>
      )}
      {/* <Btn
        disabled={!title || preview.length === 0 || !body || !price}
        onClick={!params.id ? addContent : updateContent}
      >
        {!params.id ? "등록 하기" : "수정 하기"}
      </Btn> */}
    </Container>
  );
};

const Container = styled.div`
  padding-top: 15vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 80%;
  margin: 0 auto;
  h1 {
    margin-bottom: 50px;
  }
  input {
    width: 80%;
    margin-bottom: 20px;
    border: none;
    outline: none;
    border-bottom: 1px solid;
    padding-bottom: 20px;
  }
  .title {
    font-size: large;
  }
  .region {
    font-size: medium;
    padding-bottom: 15px;
  }
  .price {
    ::-webkit-outer-spin-button,  // number input에 오른쪽 화살표 없애는 css
    ::-webkit-inner-spin-button {
      -webkit-appearance: none;
      margin: 0;
    }
  }
  textarea {
    width: 80%;
    margin-bottom: 20px;
    height: 250px;
    padding: 20px;
  }
  button {
    border-radius: 5px;
    border: none;
    height: 30px;
    width: 20%;
  }
`;
const Image = styled.div`
  width: 15%;
  height: 100%;
  position: relative;
  margin-right: 30px;
  img {
    width: 100%;
    height: 100%;
    border: none;
    outline: none;
    border-radius: 5px;
    /* background-color: gray; */
  }
`;
const Btn = styled.button`
  background-color: ${(props) => (props.disabled ? "#f8cbac" : "#ff8a3a")};
  border-radius: 5px;
  border: none;
  height: 30px;
  width: 20%;
  margin-bottom: 20px;
  cursor: pointer;
`;
const ImageContainer = styled.div`
  width: 80%;
  height: 170px;
  margin-bottom: 40px;
  display: flex;
  flex-direction: row;
  label {
    border-radius: 5px;
    border: 1px solid;
    width: 15%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    margin-right: 30px;
  }
  input {
    display: none;
    color: transparent;
  }
  p {
    margin-top: 5px;
    color: #ff8a3a;
  }
  span {
    color: black;
  }
`;
const SelectWrapper = styled.div`
  margin-bottom: 20px;
  label {
    display: block;
    font-weight: bold;
    margin-bottom: 5px;
  }
  select {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
`;

const RadioWrapper = styled.div`
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
`;

const RadioButton = styled.div`
  display: flex;
  align-items: center;
  input {
    margin-right: 5px;
  }
  label {
    font-size: 16px;
  }
`;
export default Write;
