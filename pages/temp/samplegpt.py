import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="GPT 텍스트 실습", layout="wide")
st.title("텍스트 입력으로 GPT 호출 실습")

# 텍스트 입력
prompt = st.text_input("GPT에게 보낼 질문을 입력하세요")

# 전송 버튼
if st.button("전송하기"):
    if not prompt.strip():
        st.warning("질문을 입력해 주세요.")  # 입력이 없을 때 경고
    else:
        try:
            client = OpenAI(api_key=st.secrets["openai"]["api_key"])
            completion = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}]
            )
            st.success("GPT 응답 성공")
            st.write(completion.choices[0].message.content)  # GPT 답변 출력
        except Exception as e:
            st.error(f"오류 발생: {e}")  # 에러가 있을 때 출력
