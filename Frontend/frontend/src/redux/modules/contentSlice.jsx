import { createSlice } from "@reduxjs/toolkit";
import instance from "../../shared/axios";

//middlewares
// 컨텐츠 로드
export const loadContentDB = () => {
  return async function (dispatch, getState) {
    const page = getState().content.page; // 초기 페이지는 항상 1
    await instance
      .get('/posts', { params: { page: page, limit: 4 } }) // 페이지와 한 번에 가져올 개수 설정
      .then((response) => {
        const data = response.data.posts; // posts 배열 추출
        if (Array.isArray(data)) {
          dispatch(loadContent({ data: data }));
          // 초기 로드에서는 페이지 증가하지 않음
        } else {
          console.error("Received data is not an array", data);
        }
      })
      .catch((error) => {
        console.error("Error fetching content:", error);
      });
  };
};

// 무한스크롤시 컨텐츠를 더 로드
export const loadMoreContentDB = () => {
  return async function (dispatch, getState) {
    const page = getState().content.page; // 현재 페이지 가져오기
    console.log("Current Page:", page); // 현재 페이지 로그

    await instance
      .get('/posts', { params: { page: page + 1, limit: 4 } }) // 다음 페이지 요청
      .then((response) => {
        console.log("API Response:", response.data); // 응답 데이터 로깅
        const newData = response.data.posts; // 응답에서 posts 배열 추출

        if (Array.isArray(newData)) {
          if (newData.length > 0) {
            dispatch(appendContent(newData)); // 기존 데이터에 추가
            dispatch(incrementPage()); // 페이지 증가
          } else {
            console.log("No more content to load."); // 더 이상 로드할 콘텐츠가 없음을 알림
          }
        } else {
          console.error("Received data is not an array", newData);
        }
      })
      .catch((error) => {
        console.error("Error fetching more content:", error);
      });
  };
};

// 디테일 페이지에서 해당 컨텐츠만 로드
export const loadDetailContentDB = (post_id) => {
  return async function (dispatch) {
    await instance.get(`/posts/${post_id}`).then((response) => {
      dispatch(loadDetailContent(response.data));
    });
  };
};
export const loadSearchContentDB = (search) => {
  return async function (dispatch, getState) {
    // const page = getState().content.page;
    await instance
      .get('/posts', { params: { keyword: search } })
      .then((response) => {
        const data = response.data;
        console.log(data)
        dispatch(loadSearchContent(data));
      });
  };
};
// 컨텐츠 생성
export const createContentDB = (formData) => {
  return async function (dispatch) {
    await instance
      .post("/posts", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      })
      .then((response) => {
        dispatch(createContent(response.data));
        window.location.replace('/contents');
      })
      .catch((error) => {
        console.log(error);
      });
  };
};
// 컨텐츠 수정
export const updateContentDB = (data,postID) => {
  return async function (dispatch) {
    console.log(data);
    await instance
      .put(`/posts/${postID}`, data ,{headers:{
        "Content-Type": "multipart/form-data",
      }})
      .then((response) => {
        console.log(response)
        dispatch(updateContent(response.data));
        window.location.replace('/contents');
      }).catch((error) =>{
        console.log(error)
      })
  };
};
// 컨텐츠 삭제
export const deleteContentDB = (postID) => {
  return async function (dispatch) {
    await instance.delete(`/posts/${postID}`).then((response) => {
      console.log("삭제 리스폰스", response.data);
      dispatch(deleteContent(postID));
      window.location.replace("/contents");
    });
  };
};
// 끌어올리기
export const pullupContentDB = (postID) => {
  return async function (dispatch) {
    try {
      const response = await instance.put(`/posts/pullup/${postID}`);
      console.log("끌어올리기 리스폰스:", response.data);

      dispatch(updateContent(response.data)); // 응답 데이터를 업데이트
      alert("게시글이 끌어올려졌습니다.");
      window.location.replace(`/contents`); // 게시글 목록 페이지로 이동
    } catch (error) {
      console.error("끌어올리기 오류:", error);
      alert("끌어올리기에 실패했습니다. 다시 시도해주세요.");
    }
  };
};

const contentSlice = createSlice({
  name: "content",
  initialState: {
    content_list: [],
    detail_list: [],
    search_list:[],
    page: 1,
  },
  reducers: {
    loadContent: (state, action) => {
      state.content_list = action.payload.data;
    },
    // appendContent: (state, action) => {
    //   // 중복된 콘텐츠를 방지하기 위해 필터링
    //   const newPosts = action.payload.filter(
    //     (newPost) => !state.content_list.some((existingPost) => existingPost.postID === newPost.postID)
    //   );
    //   state.content_list.push(...newPosts); // 새로운 데이터 추가
    // },
    appendContent: (state, action) => {
      state.content_list.push(...action.payload); // 새로운 데이터 추가
    },
    incrementPage: (state) => {
      state.page += 1;
    },
    loadDetailContent: (state, action) => {
      state.detail_list = action.payload;
    },
    loadSearchContent: (state, action) => {
      state.search_list = action.payload;
    },
    heartLoadContent: (state, action) => {
      state.content_list = action.payload;
    },
    createContent: (state, action) => {
      state.content_list.push(action.payload);
    },
    updateContent: (state, action) => {
      const index = state.content_list.findIndex(
        (v) => v.post.id === action.payload.id
      );
      state.content_list[index] = action.payload;
    },
    deleteContent: (state, action) => {
      const new_content = state.content_list.filter(
        (v, i) => v.post.id !== action.payload
      );
      state.content_list = new_content;
    },
  },
});

export const {
  loadContent,
  incrementPage,
  appendContent,
  loadDetailContent,
  loadSearchContent,
  heartLoadContent,
  createContent,
  updateContent,
  deleteContent,
} = contentSlice.actions;
export default contentSlice.reducer;
