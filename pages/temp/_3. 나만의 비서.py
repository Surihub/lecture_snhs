# pages/03_GPT_챗봇.py
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="GPT 챗봇", layout="centered")

st.header("3. GPT 챗봇 실습")

# 사용자 입력
prompt = st.text_input("🤖 GPT에게 무엇이든 물어보세요:")

# 응답 처리
if st.button("전송하기"):
    if not prompt.strip():
        st.warning("질문을 입력해 주세요.")
    else:
        try:
            # secrets.toml에서 API 키 불러오기
            client = OpenAI(api_key=st.secrets["openai"]["api_key"])

            # 응답 요청
            completion = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            st.markdown("#### 💡 GPT의 답변:")
            st.write(completion.choices[0].message.content)

        except Exception as e:
            st.error(f"GPT 호출 오류: {e}")



