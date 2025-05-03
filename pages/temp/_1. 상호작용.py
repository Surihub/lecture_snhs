# pages/01_상호작용_앱.py
import streamlit as st

st.set_page_config(page_title="내 MBTI 찾아보기", layout="centered")

st.header("1. 내 MBTI 찾아보기")
st.markdown("""
아래 4개의 재미있는 질문에 YES 또는 NO로 답해보세요.  
당신의 MBTI 유형을 추정해드립니다!
""")

# 질문
q1 = st.radio("💬 파티보다 혼자만의 시간이 더 좋다?", ["Yes", "No"])
q2 = st.radio("🔮 신기한 상상보다 구체적인 사실이 좋다?", ["Yes", "No"])
q3 = st.radio("⚖️ 감정보다 논리가 더 중요하다?", ["Yes", "No"])
q4 = st.radio("🗂 계획표 없이 당일치기 여행이 편하다?", ["Yes", "No"])

# 결과 계산
if st.button("👉 나의 MBTI는?"):
    code = ""
    code += "I" if q1 == "Yes" else "E"
    code += "S" if q2 == "Yes" else "N"
    code += "T" if q3 == "Yes" else "F"
    code += "P" if q4 == "Yes" else "J"

    explanation = {
        "ISTJ": "현실주의자형 - 책임감 있고 신뢰할 수 있는 관리자.",
        "ISFJ": "수호자형 - 헌신적이고 성실하며 섬세한 조력자.",
        "INFJ": "옹호자형 - 통찰력 있고 조용한 이상주의자.",
        "INTJ": "전략가형 - 독립적이며 분석적인 사고 설계자.",
        "ISTP": "장인형 - 융통성 있고 조용하며 논리적인 문제 해결사.",
        "ISFP": "모험가형 - 겸손하고 온화하며 예술적인 탐색가.",
        "INFP": "중재자형 - 순수하고 의미를 찾는 이상주의자.",
        "INTP": "논리술사형 - 호기심 많고 개념적인 발명가.",
        "ESTP": "사업가형 - 에너지 넘치고 즉흥적인 행동가.",
        "ESFP": "연예인형 - 사교적이고 유쾌한 분위기 메이커.",
        "ENFP": "활동가형 - 자유롭고 열정적인 아이디어 뱅크.",
        "ENTP": "변론가형 - 재치 있고 호기심 많은 토론가.",
        "ESTJ": "경영자형 - 실용적이고 강한 지도자.",
        "ESFJ": "집정관형 - 타인을 잘 챙기고 조화를 중요시함.",
        "ENFJ": "선도자형 - 카리스마 있고 사교적인 이끌이.",
        "ENTJ": "통솔자형 - 단호하고 전략적인 지도자."
    }

    st.subheader(f"🎯 당신의 MBTI 유형은: {code}")
    st.success(explanation.get(code, "아직 등록되지 않은 유형입니다."))

# 지도 입력 예시
st.subheader("📍 지도에 위치 표시해보기")
st.map(longitude=38, latitude=39)

# 카메라 입력 예시
st.subheader("📸 카메라 입력 체험")
st.camera_input("사진을 찍어보세요")