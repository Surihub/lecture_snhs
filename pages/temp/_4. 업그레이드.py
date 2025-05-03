# pages/03_GPT_챗봇.py
import streamlit as st
from openai import OpenAI
import base64

st.set_page_config(page_title="GPT 챗봇 및 이미지 해석", layout="centered")

st.header("3. GPT 챗봇 & 이미지 해석")
st.markdown("""
OpenAI의 GPT API (`gpt-4o`)를 활용하여 텍스트 질문 응답뿐 아니라,
이미지를 함께 분석하는 비전 기능도 체험할 수 있습니다.
""")

# OpenAI 클라이언트
client = OpenAI(api_key=st.secrets["openai"]["api_key"])

# 사용자 텍스트 입력
prompt = st.text_input("🤖 GPT에게 질문을 입력하세요 (이미지를 첨부할 수도 있어요):")

# 이미지 업로드
image_file = st.file_uploader("이미지를 업로드해 주세요 (선택 사항)", type=["png", "jpg", "jpeg"])

# 전송 버튼
if st.button("전송하기"):
    if not prompt.strip() and not image_file:
        st.warning("텍스트 또는 이미지를 입력해야 합니다.")
    else:
        try:
            content = []
            if prompt.strip():
                content.append({"type": "input_text", "text": prompt})

            if image_file:
                b64_image = base64.b64encode(image_file.read()).decode("utf-8")
                content.append({
                    "type": "input_image",
                    "image_url": f"data:image/png;base64,{b64_image}"
                })

            response = client.responses.create(
                model="gpt-4o",
                input=[{
                    "role": "user",
                    "content": content
                }]
            )

            st.markdown("#### 💡 GPT의 응답:")
            st.write(response.output_text)

        except Exception as e:
            st.error(f"GPT 호출 오류: {e}")
