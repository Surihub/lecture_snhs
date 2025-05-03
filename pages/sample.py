import streamlit as st

# 페이지 기본 설정: 제목, 파비콘, 레이아웃 지정
st.set_page_config(
    page_title="나만의 웹앱(Subhin Hwang)",
    page_icon="🤖"
)

# 화면에 제목 표시
st.title("🤖 나만의 LLM 웹앱 만들기")


####################
# # 부제목 표시
# st.subheader("반갑습니다. 황수빈입니다!")
# # 화면에 여러 줄 설명 표시
# st.markdown("""
# 이 앱은 Streamlit과 GPT API를 활용하여 다양한 실습을 진행합니다.  
# 왼쪽 사이드바에서 원하는 실습 페이지를 선택하세요.
# """)


###################
# 텍스트 입력 (한 줄)
user_text = st.text_input("질문을 입력하세요")
st.write(f"질문: {user_text}")  # 입력한 질문 바로 출력

# 텍스트 입력 (여러 줄)
user_long_text = st.text_area("긴 문장을 입력하세요", height=100)
st.write(f"긴 문장: {user_long_text}")  # 입력한 긴 문장 바로 출력

# 숫자 선택 (슬라이더)
level = st.slider("난이도를 선택하세요", 1, 10, 5)
st.write(f"선택한 난이도: {level}")  # 선택한 난이도 바로 출력

# 단일 선택 (라디오 버튼)
option = st.radio("옵션을 선택하세요", ["A", "B", "C"])
st.write(f"선택한 옵션: {option}")  # 선택한 옵션 바로 출력

# 단일 선택 (셀렉트박스)
selection = st.selectbox("항목을 선택하세요", ["Option 1", "Option 2", "Option 3"])
st.write(f"선택한 항목: {selection}")  # 선택한 항목 바로 출력

# 체크 여부 (체크박스)
agree = st.checkbox("위 내용을 모두 확인했습니다")
st.write(f"동의 여부: {'동의함' if agree else '동의하지 않음'}")  # 체크 여부 출력

# 파일 업로드 (이미지)
uploaded_image = st.file_uploader("이미지를 업로드하세요", type=["png", "jpg", "jpeg"])
if uploaded_image:
    st.image(uploaded_image, caption="업로드한 이미지", use_container_width=True)  # 업로드한 이미지 출력

# 파일 업로드 (텍스트 파일)
uploaded_text = st.file_uploader("텍스트 파일을 업로드하세요", type=["txt"])
if uploaded_text:
    text_content = uploaded_text.read().decode("utf-8")
    st.text_area("업로드한 텍스트 파일 내용", text_content, height=200)  # 업로드한 텍스트 내용 출력

# 카메라 입력
photo = st.camera_input("사진을 찍어주세요")
if photo:
    st.image(photo, caption="찍은 사진", use_container_width=True)  # 촬영한 사진 출력


#######################

# # 텍스트 입력
# user_text = st.text_input("질문을 입력하세요")

# # 버튼 클릭 시 동작
# if st.button("전송하기"):
#     if not user_text.strip():
#         st.warning("질문을 입력해야 합니다.")  # 입력이 비었을 때 경고
#     else:
#         st.success("질문이 정상적으로 입력되었습니다.")  # 정상 입력 시 성공 메시지
#         st.write("입력한 질문:", user_text)  # 입력한 질문 출력