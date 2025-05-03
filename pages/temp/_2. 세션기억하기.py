# pages/02_세션_기억_앱.py
import streamlit as st

st.set_page_config(page_title="세션 기억 앱", layout="centered")

st.header("2. 세션 기억 앱")
st.markdown("""
이 앱은 사용자가 입력한 내용을 세션에 저장하여 대화 흐름을 기억합니다.
Streamlit의 `st.session_state`를 활용합니다.
""")

# 세션 상태 초기화
if "history" not in st.session_state:
    st.session_state.history = []

# 사용자 입력
user_input = st.text_input("무엇이든 질문해보세요")

if st.button("질문 저장하기"):
    if user_input.strip():
        st.session_state.history.append(user_input)
        st.success("질문이 저장되었습니다!")
    else:
        st.warning("빈 질문은 저장되지 않습니다.")

# 대화 이력 출력
if st.session_state.history:
    st.markdown("#### 💬 지금까지 입력한 질문")
    for i, q in enumerate(st.session_state.history[::-1], 1):
        st.write(f"{i}. {q}")
