import React, { useEffect, useState } from "react";
import GlobalStyles from './assets/css/GlobalStyles'
import { Routes, Route } from "react-router-dom";
import Main from './pages/Main'
import Header from "./components/Header";
import Footer from "./components/Footer";
import Contents from "./pages/Contents";
import { useDispatch } from "react-redux";
import { loginUser } from "./redux/modules/userSlice";
import { loadContentDB } from "./redux/modules/contentSlice";
import PageNotFound from "../src/pages/PageNotFound";
import Search from "../src/pages/Search";
import Write from "./pages/Write"
import RegionContent from "./pages/RegionContent";
import Detail from "./pages/Detail"

function App() {
  const dispatch = useDispatch();
  const [isloaded, setIsloaded] = useState(false);

  //useEffect로 쿠키에 토큰 있을시 로그인 체크
  useEffect(() => {
    if (localStorage.getItem("token") !== null) {
      dispatch(loginUser(true));
    }
  });
  useEffect(() => {
    async function load() {
      await dispatch(loadContentDB());
      setIsloaded(true);
    }
    load();
  }, []);

  return (
    <div className='App'>
      <GlobalStyles />
      <Header />
        <Routes>
          <Route path="/" element={<Main />} />
          <Route path="/contents" element={isloaded && <Contents />} />
          <Route path="/region/:region" element={isloaded && <RegionContent />} />
          <Route path="*" element={<PageNotFound />} />
          <Route path="/detail/:id" element={<Detail />} />
          <Route path="/write" element={<Write />} />
          <Route path="/write/:id" element={isloaded && <Write />} />
          <Route path="/search/" element={isloaded && <Search />} />
          <Route path="/search/:search" element={isloaded && <Search />} />
        </Routes>
      <Footer />
    </div>
  )
}



export default App
