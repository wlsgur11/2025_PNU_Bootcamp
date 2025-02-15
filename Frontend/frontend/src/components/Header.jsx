import React, {useEffect} from "react"
import styled from "styled-components";
import { useNavigate } from "react-router-dom";
import { ModalSignup, ModalLogin } from "../components/Modal";
import profile from ".././assets//css/profile.jpeg";
import logo from '../assets/css/logo.svg';

const Header = () => {
    const navigate = useNavigate();
    const searchRef = React.useRef(null);
    const onKeyPress = (e) => {
      if (e.key === "Enter") {
        const searchTerm = searchRef.current.value.trim();
        if (searchTerm) {
          navigate(`/search/${searchTerm}`);
        }
      }
    };

    const users = localStorage.getItem("token");
    const profileImage = localStorage.getItem("profileImage");

    const [modalSignupOpen, setModalSignupOpen] = React.useState(false);
    const [modalLoginOpen, setModalLoginOpen] = React.useState(false);

  //   useEffect(() => {
  //     const interval = setInterval(() => {
  //         const token = localStorage.getItem("token");
  //         if (token) {
  //             const tokenTime = localStorage.getItem("tokenTime");
  //             const currentTime = new Date().getTime();
  //             if (tokenTime && currentTime - tokenTime > 30 * 60 * 1000) { // 30분
  //                 deleteToken();
  //             }
  //         }
  //     }, 60000); // 1분마다 체크

  //     return () => clearInterval(interval); // 컴포넌트 언마운트 시 interval 정리
  // }, []);

    
    // 실행 시 modal창 state 변경
    const openSignupModal = () => {
        setModalSignupOpen(true);
    };
    const closeSignupModal = () => {
        setModalSignupOpen(false);
    };

    const openLoginModal = () => {
        setModalLoginOpen(true);
    };
    const closeLoginModal = () => {
        setModalLoginOpen(false);
    };

    // 로그아웃 시 토큰 삭제
    const deleteToken = () => {
        localStorage.removeItem("token");
        localStorage.removeItem("username");
        localStorage.removeItem("login_id");
        localStorage.removeItem("profileImage");
        navigate("/");
        // window.location.reload();
    };

    const handleLogin = () => {
      // 로그인 성공 시 토큰과 시간 저장
      localStorage.setItem("token", "your_token_here");
      localStorage.setItem("tokenTime", new Date().getTime());
  };

    return (
        <Container>
            <Logo>
                <LogoImg onClick={() => navigate("/")}>
                    <Image
                    style={{ height: "50px", width: "100px" }}
                    src={logo}
                    alt="로고"
                    ></Image>
                </LogoImg>
                <LogoItem onClick={() => navigate("/contents")}>중고거래</LogoItem>
            </Logo>
            

            <List>
                    {
                <Search
                    type="text"
                    placeholder="물품이나 동네를 검색해보세요"
                    ref={searchRef}
                    onKeyPress={onKeyPress}
                ></Search>
                }
                {users && (
                <ProfileImage
                    style={{
                    height: "40px",
                    width: "40px",
                    borderRadius: "50px",
                    marginLeft: "10px",
                    }}
                    src={profileImage ? profileImage : profile}
                    alt="프로필이미지"
                ></ProfileImage>
                )}
                {users && <Title>{localStorage.getItem("nickname")}님</Title>}
                {/* {users && <Item>당근채팅</Item>} */}
                {!users && <Item onClick={openLoginModal}>로그인</Item>}
                {!users && <Item onClick={openSignupModal}>회원가입</Item>}

                <ModalLogin open={modalLoginOpen} close={closeLoginModal}></ModalLogin>

                {users && <Item onClick={deleteToken}>로그아웃</Item>}

                <ModalSignup
                open={modalSignupOpen}
                close={closeSignupModal}
                ></ModalSignup>
            </List>
        </Container>
    )

}

const Logo = styled.div`
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  margin-left: 6vw;
`;

const LogoImg = styled.div`
  width: 50px;
  padding: 10px;
  margin-left: 1vw;
  cursor: pointer;
  img {
    width: 100%;
    height: 100%;
  }
`;

const Image = styled.img`
  width: 110px;
  height: 180px;
`;

const LogoItem = styled.div`
  margin-left: 80px;
  font-size: 16px;
  color: #ff8a3a;
  font-weight: bold;
  white-space: nowrap;
  cursor: pointer;
  &:hover {
    color: #cccccc;
  }
`;
const Search = styled.input`
  width: 230px;
  height: 40px;
  text-align: left;
  padding: 9px 12px;
  border: none;
  border-radius: 5px;
  background-color: #f2f3f6;
  &::placeholder {
    color: #8a8f98;
  }
`;

const ProfileImage = styled.img``;

const List = styled.div`
  margin-right: 6vw;
`;

const Item = styled.div`
  display: flex;
  justify-content: center;
  padding-top: 10px;
  height: 40px;
  width: 77px;
  border-radius: 3px;
  outline: 1px solid #d3d3d4;
`;

const Title = styled.div`
  color: black;
  font-size: 16px;
  font-weight: bolder;
  margin-left: 10px;
`;
const Container = styled.div`
  display: flex;
  justify-content: space-between;
  background-color: white;
  position: fixed;
  width: 100%;
  height: 8vh;
  z-index: 100;
  padding-top: 0.5vw;
  @media (max-width: 499px) {
    /* padding: 30px; */
  }
  @media (min-width: 500px) {
    /* padding: 25px; */
  }
  ${List} {
    display: flex;
    align-items: center;
  }
  ${Item} {
    border: 1px black;
    margin-left: 10px;
    font-size: 16px;
    font-weight: bold;
    color: black;

    cursor: pointer;
    &:hover {
      color: #cccccc;
      background-color: #fcfafa;
    }
  }`

export default Header;