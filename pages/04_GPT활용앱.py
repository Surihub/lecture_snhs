# 03_GPT챗봇.py
# 선택형 프롬프트 + 말투 옵션 적용 챗봇

import streamlit as st
from openai import OpenAI

# 페이지 설정
st.set_page_config(
    page_title="GPT 챗봇 (선택형 + 말투)",
    page_icon="🤖",
    layout="centered"
)

st.title("GPT 챗봇 실습")
st.markdown("요청 유형과 말투를 선택하여 GPT에게 질문해보세요.")

# 1. 프롬프트 유형 선택
mode = st.selectbox("📌 작업 유형을 선택하세요", ["자유 질문", "텍스트 요약", "영어로 번역", "개념 설명"])

# 2. 톤 선택
tone = st.selectbox("🎨 원하는 말투를 선택하세요", ["기본", "따뜻한", "차가운", "공손한", "친근한", "재미있는"])

# 3. 사용자 입력
user_input = st.text_area("✏️ 입력할 내용을 적어주세요", height=150)

# 4. GPT 요청 실행
if st.button("GPT에게 요청하기"):
    if not user_input.strip():
        st.warning("입력 내용이 비어 있습니다.")
    else:
        # 말투 문장 정의
        tone_map = {
            "기본": "",
            "따뜻한": "말투는 따뜻하게 해줘.",
            "차가운": "말투는 무미건조하고 간결하게 해줘.",
            "공손한": "존댓말로 공손하게 말해줘.",
            "친근한": "말투는 친구처럼 친근하게 해줘.",
            "재미있는": "말투는 재치있고 유쾌하게 해줘."
        }

        # 요청 내용 생성
        if mode == "자유 질문":
            prompt = f"{user_input}\n{tone_map[tone]}"
        elif mode == "텍스트 요약":
            prompt = f"다음 글을 한 문장으로 요약해줘:\n\n{user_input}\n{tone_map[tone]}"
        elif mode == "영어로 번역":
            prompt = f"다음 문장을 영어로 자연스럽게 번역해줘:\n\n{user_input}\n{tone_map[tone]}"
        elif mode == "개념 설명":
            prompt = f"'{user_input}'에 대해 초등학생도 이해할 수 있게 설명해줘.\n{tone_map[tone]}"

        # GPT 호출
        try:
            client = OpenAI(api_key=st.secrets["openai"]["api_key"])
            completion = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}]
            )
            st.markdown("### 💡 GPT의 답변:")
            st.write(completion.choices[0].message.content)

        except Exception as e:
            st.error(f"GPT 호출 오류: {e}")
