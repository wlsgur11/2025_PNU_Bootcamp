import styled from "styled-components";
import { Link } from "react-router-dom";
import image from '../assets/css/asd.png'

const SearchNotFound = () => {
  return (
    <NotFoundWrap>
      <img
        src={image}
        alt="당근"
      />
      <Title>검색 결과를 찾을 수 없습니다.</Title>
      <Link to='/contents' style={{color:'#ff8a3a',textDecoration:'none',marginTop:'20px',fontSize:'20px' }}>홈으로 이동</Link>
    </NotFoundWrap>
  );
};
const NotFoundWrap = styled.div`
  display: flex;
  flex-direction: column;
  width: 50vw;
  height: 50vh;
  text-align: center;
  align-items: center;
  justify-content: center;
`;

const Title = styled.h1`
  margin-top: 10vh;
`;
export default SearchNotFound;
