import streamlit as st
import webbrowser
from openai import OpenAI

# 페이지 설정
st.set_page_config(
    page_title="GPT 영화 추천기",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 GPT 기반 영화 추천기")

# 추천 기준 선택
criterion = st.radio(
    "🎯 추천 기준을 선택하세요",
    ["MBTI 기반", "평점 높은 영화", "신선한 소재의 영화", "요즘 화제인 영화"]
)

# MBTI 입력
mbti_type, mbti_desc = "", ""
if criterion == "MBTI 기반":
    mbti_type = st.selectbox("🧬 MBTI를 선택하세요", [
        "INTJ", "INTP", "ENTJ", "ENTP",
        "INFJ", "INFP", "ENFJ", "ENFP",
        "ISTJ", "ISFJ", "ESTJ", "ESFJ",
        "ISTP", "ISFP", "ESTP", "ESFP"
    ])
    mbti_desc = st.text_area("📄 성격을 한 줄로 설명해 주세요", placeholder="예: 분석적이고 조용하지만 몰입할 때 열정적입니다.")

# 프롬프트 생성
def make_prompt(criterion, mbti_type="", mbti_desc=""):
    if criterion == "MBTI 기반":
        return f"""
MBTI가 {mbti_type}이고, 성격은 "{mbti_desc}"인 사람에게 어울리는 영화를 아래 형식으로 한 편 추천해줘.

제목: (한글 제목)
추천 이유: (짧고 강렬하게)
줄거리 요약: (재미있고 생생하게)
"""
    elif criterion == "평점 높은 영화":
        return """
평점이 매우 높은 명작 영화를 아래 형식으로 한 편 추천해줘.

제목: (한글 제목)
추천 이유: (짧고 강렬하게)
줄거리 요약: (재미있고 생생하게)
"""
    elif criterion == "신선한 소재의 영화":
        return """
최근에 나온 신선하고 독특한 소재의 영화를 아래 형식으로 한 편 추천해줘.

제목: (한글 제목)
추천 이유: (짧고 강렬하게)
줄거리 요약: (재미있고 생생하게)
"""
    elif criterion == "요즘 화제인 영화":
        return """
요즘 화제가 되고 있는 인기 있는 영화를 아래 형식으로 한 편 추천해줘.

제목: (한글 제목)
추천 이유: (짧고 강렬하게)
줄거리 요약: (재미있고 생생하게)
"""

# 추천 요청
if st.button("🎁 영화 추천받기"):

    with st.spinner("GPT가 영화를 고르고 있어요..."):
        prompt = make_prompt(criterion, mbti_type, mbti_desc)

        try:
            client = OpenAI(api_key=st.secrets["openai"]["api_key"])
            completion = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}]
            )
            response = completion.choices[0].message.content.strip()

            # 내용 파싱
            lines = response.splitlines()
            title, reason, summary = "", "", ""
            for line in lines:
                if line.startswith("제목:"):
                    title = line.replace("제목:", "").strip()
                elif line.startswith("추천 이유:"):
                    reason = line.replace("추천 이유:", "").strip()
                elif line.startswith("줄거리 요약:"):
                    summary = line.replace("줄거리 요약:", "").strip()

            # 링크 생성
            search_url = f"https://www.google.com/search?q={title}+영화"

            # 출력
            st.markdown(f"# 🎬 {title}")
            st.markdown(f"### ✅ 추천 이유\n{reason}")
            st.markdown(f"### 📝 줄거리 요약\n{summary}")
            st.markdown(
                f'<a href="{search_url}" target="_blank"><button style="background-color:#4CAF50;color:white;padding:10px 20px;border:none;border-radius:5px;cursor:pointer;">🔗 영화 정보 검색하러 가기</button></a>',
                unsafe_allow_html=True
            )

            if st.button("🔁 다시 추천받기"):
                st.rerun()

        except Exception as e:
            st.error(f"GPT 호출 오류: {e}")
