# 03_GPT챗봇.py — 핑퐁 채팅형 GPT 챗봇

import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="GPT 채팅",
    page_icon="💬",
    layout="centered"
)

st.title("GPT 채팅봇")

# GPT API 클라이언트 초기화
client = OpenAI(api_key=st.secrets["openai"]["api_key"])

# 채팅 기록 초기화
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "안녕하세요! 무엇을 도와드릴까요?"}
    ]

# 이전 메시지 출력
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])

# 사용자 입력 받기
user_prompt = st.chat_input("질문을 입력하세요")
if user_prompt:
    # 사용자 메시지 추가
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    st.chat_message("user").write(user_prompt)

    # GPT 응답 생성
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=st.session_state.messages
        )
        reply = response.choices[0].message.content

    except Exception as e:
        reply = f"[오류] {e}"

    # GPT 메시지 추가 및 출력
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)
