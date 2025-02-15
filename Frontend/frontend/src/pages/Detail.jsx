import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate, useParams } from "react-router-dom";
import styled from "styled-components";
import CardSlide from "../components/CardSlide";
import { deleteContentDB, loadDetailContentDB, pullupContentDB } from "../redux/modules/contentSlice";
import profile from "../assets/css/profile.jpeg";
import Like from "../components/Like";
// import image from "../assets/css/asd.png"

const Detail = () => {
  const params = useParams();
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const [isloaded, setIsloaded] = useState(false);
  const data = useSelector((state) => state.content.detail_list);
  const username = localStorage.getItem("nickname");
  // const [images, setImages] = useState({});
  

  useEffect(() => {
    async function detailLoad() {
      await dispatch(loadDetailContentDB(params.id));
      setIsloaded(true);
    }
    detailLoad();
  }, [dispatch, params.id]);

  const handleDelete = () => {
    if (window.confirm("정말로 삭제하시겠습니까?")) {
      dispatch(deleteContentDB(data.post.id));
      alert("삭제되었습니다.");
    } else {
      alert("삭제가 취소되었습니다.");
    }
  };

  const handlePullup = async () => {
    if (window.confirm("이 게시글을 최신 글로 끌어올리겠습니까?")) {
      await dispatch(pullupContentDB(data.post.id));
      // alert("게시글이 최신 글로 끌어올려졌습니다.");
      navigate("/contents"); // 메인 페이지로 이동 또는 새로고침
    }
  };

  return (
    <>
      {isloaded && (
        <>
          {/* <CardSlide images={Array.isArray(data.photos) ? data.photos : []} /> */}
          <CardSlide images={(() => {
            return Array.isArray(data.photos) ? data.photos : [];
          })()} />

          <Container>
            <Wrap>
              <Profile>
                <div>
                  <img
                    src= {profile}
                    alt=""
                  ></img>
                </div>
                <div className="name">
                  <p style={{ fontSize: "15px", fontWeight: "600" }}>
                    {data.post.author_name}
                  </p>
                  <p style={{ fontSize: "15px" }}>{data.post.location}</p>
                </div>
              </Profile>
              <ProfileRight>
                <dl>
                  <dt>매너온도</dt>
                  <dd>
                    36.5<span>°Cㅤ</span>
                    <span></span>
                  </dd>
                </dl>
                <div className="meters">
                  <div className="bar"></div>
                </div>
                <div className="face"></div>
              </ProfileRight>
            </Wrap>
            <Content>
              <div className="title">
                <h1>{data.post.title}</h1>
                <div className="button">
                  {username === data.post.author_name ? (
                    <>
                      <ButtonGroup>
                        <StyledButton
                          onClick={() => {
                            navigate(`/write/${data.post.id}`);
                          }}
                        >
                          수정
                        </StyledButton>
                        <StyledButton $delete onClick={handleDelete}>
                          삭제
                        </StyledButton>
                        <StyledButton $primary onClick={handlePullup}>
                          끌어올리기
                        </StyledButton>
                      </ButtonGroup>
                    </>
                  ) : null}
                </div>
              </div>
              <p style={{ color: "#868e96", fontSize: "15px", marginTop: "4px" }}>
                {/* {data.post.updated_at.toString()?.slice(0, 10) || ""} */}
                {data.post.updated_at ? new Date(data.post.updated_at * 1000).toLocaleDateString() : ""}
              </p>
              <p style={{ marginTop: "4px", fontSize: "16px", fontWeight: "bold" }}>
                {data.post.price}원
              </p>
              <div>{data.post.body}</div>
              <Like
                likeCnt={data.post.like}
                commentCnt={0}
                postID={data.post.id}
              ></Like>
            </Content>
          </Container>
        </>
      )}
    </>
  );
};

const Container = styled.div`
  width: 50%;
  margin: 50px auto;
`;
const Wrap = styled.div`
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 13px;
  border-bottom: 1px solid #e9ecef;
`;
const Profile = styled.div`
  display: flex;
  flex-direction: row;
  align-items: center;
  p {
    margin-bottom: 5px;
  }
  img {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    object-fit: cover;
  }
  .name {
    margin-left: 8px;
  }
`;
const ProfileRight = styled.div`
  position: relative;
  width: 18%;

  dl {
    width: 100%;
  }
  dt {
    position: absolute;
    top: 36px;
    right: -8px;
    font-size: 12px;
    line-height: 1;
    letter-spacing: -0.6px;
    color: #868e96;
    width: 50px;
    height: 50px;
  }
  dd {
    position: absolute;
    color: #1561a9;
    font-size: 16px;
    font-weight: bold;
    line-height: 1;
    letter-spacing: -0.5px;
    margin-top: 1px;
    width: 100px;
    text-align: right;
  }
  .meters {
    clear: both;
    display: block;
    width: 100px;
    background-color: #e9ecef;
    height: 4px;
    border-radius: 100px;
    -webkit-border-radius: 100px;
    -moz-border-radius: 100px;
    position: relative;
    vertical-align: middle;
    margin-top: 24px;
  }
  .bar {
    background-color: #1561a9;
    width: 36.5%;
    position: absolute;
    height: 4px;
    border-radius: 10px;
  }
  .face {
    position: absolute;
    width: 31px;
    height: 24px;
    right: 0;
    top: 0;
    overflow: hidden;
    text-align: left;
    text-indent: -9999px;
    background-size: 29px 147px;
    background: url("https://d1unjqcospf8gs.cloudfront.net/assets/home/articles/face-icon-set-0cffc52be32961b0bb4a308c272d8f526ddcdeda66dbde6eb32618eeb22b74e6.png");
    background-repeat: no-repeat;
    background-position: 0px -75px;
  }
`;
const Content = styled.div`
  margin-top: 20px;
  padding-bottom: 13px;
  border-bottom: 1px solid #e9ecef;
  width: 100%;
  .title {
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
  }
  // .button {
  //   display: flex;
  //   flex-direction: row;
  //   justify-content: flex-end;
  //   width: 10%;
  //   button {
  //     border: none;
  //     background-color: transparent;
  //     margin-left: 5px;
  //     font-size: medium;
  //     cursor: pointer;
  //     :hover {
  //       color: #ff8a3a;
  //     }
  //   }
  // }
  // h1 {
  //   margin-bottom: 5px;
  // }
  // p {
  //   margin-bottom: 10px;
  //   font-size: 17px;
  // }
  div {
    margin-top: 10px;
    font-size: 17px;
      white-space: pre-line;
}
  //   p {
  //     font-size: 13px;
  //     color: #868e96;
  //   }
  // }
`;

const StyledButton = styled.button`
  padding: 5px 10px;
  font-size: 13px;
  font-weight: bold;
  color: ${(props) =>
    props.$delete ? "white" : props.$primary ? "white" : "#ff8a3a"};
  background-color: ${(props) =>
    props.$delete ? "#ff4d4d" : props.$primary ? "#87CEFA" : "transparent"};
  border: ${(props) =>
    props.$delete ? "none" : props.$primary ? "none" : "2px solid #ff8a3a"};
  border-radius: 5px;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-right: 15px;

  &:hover {
    background-color: ${(props) =>
      props.$delete ? "#ff1a1a" : props.$primary ? "#4682B4" : "#ff8a3a"};
    color: white;
  }
`;

const ButtonGroup = styled.div`
  display: flex;
  gap: 1px; /* 버튼 사이 간격 */
  margin-top: 10px; /* 위 요소와의 간격 */
`;



export default Detail;
