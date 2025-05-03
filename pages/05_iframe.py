# 외부 웹페이지를 Streamlit 앱에 삽입하는 실습입니다.
import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정
st.set_page_config(
    page_title="iframe 활용 실습",
    page_icon="🌐",
    layout="centered"
)

st.title("🌐 외부 페이지 가져오기 실습")
st.markdown("iframe을 사용하여 외부 콘텐츠를 스트림릿 앱에 삽입해보는 예제입니다.")

# 사용자 선택: 삽입할 사이트 선택
site = st.selectbox("불러올 외부 페이지를 선택하세요", [
    "Desmos 계산기",
    "YouTube 영상",
    "구글 설문지"
])

# 각 선택에 따른 iframe 주소 정의
if site == "Desmos 계산기":
    src_url = "https://www.desmos.com/scientific?lang=ko"
elif site == "YouTube 영상":
    src_url = "https://youtu.be/yKNxeF4KMsY?si=qF71ypZ_kG3Xkr9x"
elif site == "구글 설문지":
    src_url = "https://docs.google.com/forms/d/e/1FAIpQLSdLfZ.../viewform"

# iframe 삽입
components.iframe(src=src_url, width=700, height=500, scrolling=True)
