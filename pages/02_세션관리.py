# 02_세션관리.py
# 사용자의 입력을 기억하는 세션 상태(session_state) 실습 페이지입니다.

import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="세션 상태 실습",
    page_icon="🧠",
    layout="centered"
)

st.title("세션 상태 기억하기")
st.markdown("입력한 내용을 기억해서 유지하는 기능을 실습해봅니다.")

# 입력값 받기
user_input = st.text_input("질문을 입력하세요")

# 버튼을 누르면 입력값 저장
if st.button("입력 저장하기"):
    if "history" not in st.session_state:
        st.session_state.history = []  # history 리스트가 없으면 생성
    st.session_state.history.append(user_input)  # 입력값을 리스트에 추가

# 입력 내역 출력
st.markdown("---")
st.subheader("📚 지금까지 입력한 내용")

if "history" in st.session_state and st.session_state.history:
    for i, text in enumerate(st.session_state.history, start=1):
        st.write(f"{i}. {text}")
else:
    st.info("아직 저장된 입력이 없습니다.")
