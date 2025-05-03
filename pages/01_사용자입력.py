# 01_사용자입력.py
# 다양한 Streamlit 입력 요소를 실습하는 페이지입니다.

import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="사용자 입력 실습",
    page_icon="📝",
    layout="centered"
)

st.title("사용자 입력 실습")
st.markdown("아래 입력 칸들을 채워보세요. 입력한 값은 실시간으로 바로 아래에 표시됩니다.")

# 1. 텍스트 입력
name = st.text_input("이름을 입력하세요")

# 2. 숫자 입력
age = st.number_input("나이를 입력하세요", min_value=0, max_value=120, step=1)

# 3. 라디오 버튼
favorite_color = st.radio("좋아하는 색을 선택하세요", ["빨강", "파랑", "노랑"], horizontal=True)

# 4. 셀렉트 박스
hobby = st.selectbox("취미를 선택하세요", ["독서", "운동", "음악", "게임", "기타"])

# 5. 체크박스
agree = st.checkbox("위의 내용을 모두 확인하였습니다.")

# 6. 텍스트 파일 업로드
uploaded_text = st.file_uploader("텍스트 파일을 업로드하세요", type=["txt"])
text_content = None
if uploaded_text:
    text_content = uploaded_text.read().decode("utf-8")

# 7. 이미지 업로드
uploaded_image = st.file_uploader("이미지 파일을 업로드하세요", type=["png", "jpg", "jpeg"])

# 8. 카메라 입력
camera_image = st.camera_input("카메라로 사진을 찍어보세요")

# --- 출력부 ---
st.markdown("---")
st.subheader("입력 결과 확인")

if name:
    st.write(f"🙋 이름: {name}")
if age:
    st.write(f"🎂 나이: {int(age)}")
st.write(f"🎨 좋아하는 색: {favorite_color}")
st.write(f"🎯 취미: {hobby}")
st.write(f"✅ 동의 여부: {'동의함' if agree else '동의하지 않음'}")

if text_content:
    st.markdown("📄 업로드한 텍스트 파일 내용:")
    st.text(text_content)

if uploaded_image:
    st.image(uploaded_image, caption="업로드한 이미지", use_column_width=True)

if camera_image:
    st.image(camera_image, caption="카메라로 촬영한 이미지", use_column_width=True)
