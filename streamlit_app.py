# home.py
# Streamlit 웹앱의 시작 페이지 - 자기소개를 위한 대문 구성입니다.

import streamlit as st  # streamlit 라이브러리 불러오기

# 페이지 설정 (탭 제목, 아이콘, 레이아웃 등)
st.set_page_config(
    page_title="나의 LLM 웹앱",   # 브라우저 탭 제목
    page_icon="📘",              # 브라우저 탭 파비콘
    layout="centered"           # 화면 레이아웃: centered 또는 wide
)

# 제목과 설명
st.title("나를 소개합니다")  # 페이지 메인 제목
st.markdown("Streamlit을 활용한 **LLM 웹앱 실습**의 첫걸음입니다.")  # 간단한 소개 문구

# 사용자 자기소개 입력창
name = st.text_input("이름을 입력하세요")  # 이름 입력
intro = st.text_area("간단한 자기소개를 작성해보세요", height=100)  # 소개글 입력

# 입력이 있을 때만 결과 출력
if name and intro:
    st.markdown("---")  # 구분선
    st.header(f"👋 반갑습니다, {name}님!")
    st.write(intro)

# 메시지 종류 예시
st.markdown("### 💬 메시지 종류 예시")
st.success("이것은 성공 메시지입니다. (초록색)")
st.error("이것은 오류 메시지입니다. (빨간색)")
st.warning("이것은 경고 메시지입니다. (노란색)")
st.info("이것은 정보 메시지입니다. (파란색)")

# 사이드바 안내
st.sidebar.info("👉 좌측 사이드바에서 실습을 선택하세요.")
