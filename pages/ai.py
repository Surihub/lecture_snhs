import streamlit as st
import requests

st.set_page_config(page_title="Hugging Face API 실습", layout="wide")
st.title("Hugging Face Inference API로 문장 요약하기")

API_URL = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"
headers = {"Authorization": f"Bearer YOUR_HUGGINGFACE_API_KEY"}

text = st.text_area("요약할 문장을 입력하세요", height=300)

if st.button("요약하기"):
    if not text.strip():
        st.warning("문장을 입력하세요.")
    else:
        payload = {"inputs": text}
        response = requests.post(API_URL, headers=headers, json=payload)
        result = response.json()
        st.subheader("요약 결과")
        st.write(result[0]['summary_text'])
