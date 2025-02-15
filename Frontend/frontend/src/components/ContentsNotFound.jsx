import styled from "styled-components";
import { Link } from "react-router-dom";
import image from "../assets/css/asd.png"


const ContentsNotFound = () => {
  return (
    <NotFoundWrap>
      <img
        src={image}
        alt="당근"
      />
      <h1>게시글이 없습니다.</h1>
      <Link to='/contents' style={{color:'#ff8a3a',textDecoration:'none',marginBottom:'30px',fontSize:'20px' }}>홈으로 이동</Link>
    </NotFoundWrap>
  );
};
const NotFoundWrap = styled.div`
  display: flex;
  flex-direction: column;
  width: 100vw;
  height: 50vh;
  text-align: center;
  align-items: center;
  justify-content: center;
  
`;


export default ContentsNotFound;
