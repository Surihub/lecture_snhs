import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="🧰 외부 도구 모음", page_icon="🧩", layout="centered")

st.title("🧩 수업에 바로 활용하는 외부 도구")
st.markdown("Desmos 계산기, 이름 추첨기, 타이머를 한 화면에 모았습니다.")

tabs = st.tabs([
    "🧮 공학용 계산기", 
    "📈 그래프 계산기",
    "🎲 이름 추첨기",
    "⏱️ 타이머"
])

with tabs[0]:
    st.subheader("🧮 Desmos 공학용 계산기")
    st.info("복잡한 계산을 빠르게 수행할 수 있어요. 수학 수업의 계산기 대용으로 활용해보세요.")
    components.iframe("https://www.desmos.com/scientific?lang=ko", width=800, height=600, scrolling=True)

with tabs[1]:
    st.subheader("📈 Desmos 그래핑 계산기")
    st.info("함수를 직접 입력해 그래프를 실시간으로 그릴 수 있어요. 함수의 성질을 탐구하는 활동에 적합해요.")
    components.iframe("https://www.desmos.com/calculator?lang=ko", width=800, height=600, scrolling=True)

with tabs[2]:
    st.subheader("🎲 Prevl 이름 추첨기")
    st.info("이름을 입력한 후 '추첨 시작' 버튼을 누르면 랜덤으로 선택해줘요. 발표자 선정에 적합해요.")
    components.iframe("https://prevl.org/", width=800, height=600, scrolling=True)

with tabs[3]:
    st.subheader("⏱️ VClock 타이머")
    st.info("시간 제한 활동에 유용해요. 실시간 타이머로 학습 몰입도를 높여보세요.")
    components.iframe("https://vclock.kr/timer/", width=800, height=600, scrolling=True)



