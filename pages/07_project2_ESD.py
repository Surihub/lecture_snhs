import streamlit as st
import pandas as pd
from PIL import Image
from openai import OpenAI
import base64

# ✅ GPT 클라이언트 설정
client = OpenAI(api_key=st.secrets["openai"]["api_key"])

# ✅ 페이지 설정
st.set_page_config(page_title="ESD 프로젝트 사례", layout="wide")
st.title("🌿 ESD 프로젝트 결과 공유 예시")

# ------------------------
st.header("📌 프로젝트명: 전자폐기물 재활용 캠페인")
st.markdown("""
전자폐기물이 환경에 미치는 영향을 탐구하고, 교내에서 전자폐기물 분리배출 캠페인을 기획 및 실행함.  
AI 도구를 활용하여 환경 오염 정보를 시각화하고, 학생 대상 인식 개선 포스터를 제작함.
""")

# ------------------------
st.subheader("🧩 프로젝트 개요")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
- **주제**: 전자폐기물의 재활용 가능성과 AI 기반 분리배출 홍보  
- **참여자**: 2학년 4명 팀 프로젝트  
- **활동 기간**: 2025년 4월 ~ 5월  
- **활용 도구**: Streamlit, DALL·E, Canva  
    """)
with col2:
    st.image("https://images.unsplash.com/photo-1593642532973-d31b6557fa68", caption="전자기기 분해 및 분리배출 활동 장면", use_container_width=True)

# ------------------------
st.subheader("🎥 활동 영상 기록")
with st.expander("📹 영상 보기"):
    st.video("https://www.youtube.com/watch?v=_6vAjG0JzqY")

# ------------------------
st.subheader("🎧 오디오 소개")
with st.expander("🎙️ 학생 음성 인터뷰"):
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

# ------------------------
st.subheader("🎯 실천 활동 내용")
st.markdown("""
- 중고 스마트폰, 노트북, 전자기기 등을 수거해 구성품별로 분해하고 **소재별로 재분류**함  
- AI 이미지 생성기를 활용해 **환경 인식 포스터 5종** 제작 → 교내 게시  
- Streamlit을 활용해 **전자폐기물의 위험성과 해결방안을 시각화한 웹페이지**를 만들고 홍보  

> 이 프로젝트를 통해 AI 활용 역량, 환경 문제에 대한 민감도, 협업 능력을 기를 수 있었음
""")

# ------------------------
st.subheader("🗺️ 캠페인 활동 지역")
data = pd.DataFrame({
    'lat': [37.4998, 37.5005],
    'lon': [127.0366, 127.0374]
})
st.map(data, zoom=15)

# ------------------------
st.subheader("📸 이미지로 분리배출 판단하기 (GPT Vision)")
uploaded_image = st.camera_input("사용한 전자제품을 촬영해보세요")
if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="📷 업로드된 이미지", use_container_width=True)

    with st.spinner("GPT가 이미지를 분석 중입니다..."):
        try:
            img_bytes = uploaded_image.getvalue()
            img_base64 = base64.b64encode(img_bytes).decode("utf-8")

            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "너는 이미지 분리배출 전문가야. 이 쓰레기가 재활용 가능한지 판단해줘."},
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": "이 이미지는 재활용이 가능한가요? 재활용/일반 중 하나로 명확히 판단하고, 이 이미지가 무엇인지 판단하고 그 이유를 한줄로 설명해주세요. "
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{img_base64}"
                                }
                            }
                        ]
                    }
                ],
                max_tokens=200
            )

            result = response.choices[0].message.content.strip()
            st.success(f"GPT 분석 결과: {result}")

        except Exception as e:
            st.error(f"이미지 분석 중 오류 발생: {e}")

# ------------------------
st.subheader("🧮 ESD 관련 수식 설명")

with st.expander("♻️ 재활용률 계산 수식"):
    st.latex(r"""
    \text{Recycling Rate} = \left( \frac{\text{Amount Recycled}}{\text{Total Waste Generated}} \right) \times 100
    """)
    st.markdown("""
    - **의미**: 전체 폐기물 중 얼마나 재활용되었는지를 백분율로 나타냅니다.  
    - **예시**: 50kg 중 35kg 재활용 시 → 재활용률 = 70%
    """)

with st.expander("🌍 환경영향 점수 산정"):
    st.latex(r"""
    \text{Impact Score} = \sum_{i=1}^{n} \left( E_i \times W_i \right)
    """)
    st.markdown("""
    - **의미**: 다양한 환경 부하 항목에 가중치를 곱해 총 환경 영향을 계산합니다.  
    - \(E_i\): 항목별 환경 부하량  
    - \(W_i\): 각 항목의 중요도 가중치  
    """)

with st.expander("🏭 탄소발자국 절감량 추정"):
    st.latex(r"""
    \Delta \text{CO}_2 = (\text{C}_{\text{new}} - \text{C}_{\text{recycle}}) \times N
    """)
    st.markdown("""
    - **의미**: 재활용을 통해 절감된 이산화탄소 배출량을 추정합니다.  
    - \(C_{new}\): 새 제품 생산 시 CO₂ 배출량  
    - \(C_{recycle}\): 재활용 시 CO₂ 배출량  
    - \(N\): 재활용된 제품 수량  
    - **예시**: 노트북 10대 재활용 → 2000 - 500 = 1500kg CO₂ 절감
    """)

st.success("이 수식들은 ESD 활동의 환경적 효과를 수치로 표현하는 데 활용됩니다.")

# ------------------------
st.subheader("📝 활동 결과 요약")
st.success("총 19kg의 전자폐기물이 분리배출되었고, 150여 명의 학생이 환경교육에 참여함")

# ------------------------
st.subheader("🚀 향후 확장 아이디어")
st.markdown("""
- **IoT 센서**를 활용한 실시간 분리배출 가이드 앱 개발  
- **AI 챗봇**을 통한 가정용 전자폐기물 처리방법 안내 서비스  
- 타학교와 연계한 **지속가능성 공동 캠페인** 추진  
""")
