import React from "react";
import Slider from "react-slick";

import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import styled from "styled-components";

function SampleNextArrow(props) {
  const { className, style, onClick } = props;
  return (
    <div
      className={className}
      style={{
        ...style,
        width: "12px",
        background:
          'url("https://d1unjqcospf8gs.cloudfront.net/assets/home/articles/icon-slider-right-134c53f44716c3bef227ec30da385b4b09c9c068d339a617a23093718f379d02.svg")',
        backgroundRepeat: "no-repeat",
      }}
      onClick={onClick}
    />
  );
}
function SamplePrevArrow(props) {
  const { className, style, onClick } = props;
  return (
    <div
      className={className}
      style={{
        ...style,
        width: "12px",
        display: "block",
        background:
          'url("https://d1unjqcospf8gs.cloudfront.net/assets/home/articles/icon-slider-left-4c0e713bfa2cd12bd959e6dd9ef456cd6fc094953c41e605f6b9a59bc1680686.svg")',
        backgroundRepeat: "no-repeat",
      }}
      onClick={onClick}
    />
  );
}
const CardSlide = ({ images }) => {
  const settings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
    adaptiveHeight: true, 
    adaptiveWidth: true, 
    nextArrow: <SampleNextArrow />,
    prevArrow: <SamplePrevArrow />,
  };
  return (
    <Wrap>
      <Slider {...settings}>
        {/* {image.map((v) => (
          // <img src={v} key={v} alt=""></img>
          <img src={`http://localhost:8000/${v.id}`|| {image}}></img>
        ))} */}
        {images && images.length > 0 ? (
          images.map((v, index) => (
            <SlideImage
              src={`http://localhost:8000${v}`}
              key={index}
              alt={`Slide-${index}`}
            />
          ))
        ) : (
          <p>이미지가 없습니다.</p>
        )}
      </Slider>
    </Wrap>
  );
};
const Wrap = styled.div`
  padding-top: 11vh;
  width: 42%;
  margin: 0 auto;
  .slick-prev:before {
    display: none;
  }
  .slick-next:before {
    display: none;
  }
  .slick-dots {
    margin-bottom: 30px;
  }
  .slick-dots li button:before {
    /* color: white; */
  }
  img {
    border-radius: 10px;
    height: 500px;
  }
`;
const SlideImage = styled.img`
  border-radius: 20px;
  width: 100%;
  height: auto;
  object-fit: cover;
`;

export default CardSlide;
