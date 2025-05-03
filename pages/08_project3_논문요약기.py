import streamlit as st
import fitz  # PyMuPDF
from openai import OpenAI
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from kiwipiepy import Kiwi
from io import BytesIO

# 형태소 분석기 초기화
kiwi = Kiwi()

# ✅ 시스템 한글 폰트 탐색 함수
def get_korean_font():
    font_names = ["Malgun Gothic", "AppleGothic", "NanumGothic", "맑은 고딕"]
    for font_name in font_names:
        font_list = [f.fname for f in fm.fontManager.ttflist if font_name in f.name]
        if font_list:
            return font_list[0]
    return None

korean_font_path = get_korean_font()

# ✅ 워드클라우드 생성 함수
def generate_wordcloud(text, font_path, width=800, height=400):
    wordcloud = WordCloud(
        font_path=font_path,
        background_color="white",
        width=width,
        height=height
    ).generate(text)
    buf = BytesIO()
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return buf

# ✅ 명사만 추출
def extract_nouns(text):
    tokens = kiwi.analyze(text)
    nouns = [word.form for sentence in tokens for word in sentence[0] if word.tag.startswith('NN')]
    return ' '.join(nouns)

# ✅ GPT 클라이언트 설정
client = OpenAI(api_key=st.secrets["openai"]["api_key"])

# ✅ 페이지 설정
st.set_page_config(page_title="논문 요약 + 워드클라우드", layout="centered")
st.title("📄 GPT 기반 논문 요약 + 워드클라우드")

# ✅ 세션 상태 초기화
for key in ["text", "summary", "show_summary", "show_wordcloud"]:
    if key not in st.session_state:
        st.session_state[key] = ""

# ✅ 논문 업로드
uploaded_file = st.file_uploader("논문 PDF 파일을 업로드하세요", type=["pdf"])

if uploaded_file:
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        full_text = "".join([page.get_text() for page in doc])

    if len(full_text) > 8000:
        st.warning("논문이 길어 앞부분만 요약됩니다.")
        full_text = full_text[:8000]

    st.session_state.text = full_text

# ✅ 요약 생성 버튼
if st.session_state.text and st.button("요약 생성하기"):
    with st.spinner("GPT가 논문을 요약 중입니다..."):
        try:
            prompt = f"다음 논문 내용을 800자 이내로 간결하게 요약해줘:\n\n{st.session_state.text}"
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}],
                timeout=60
            )
            st.session_state.summary = response.choices[0].message.content
            st.session_state.show_summary = True
        except Exception as e:
            st.error(f"GPT 처리 중 오류 발생: {e}")

# ✅ 요약 출력
if st.session_state.show_summary:
    st.subheader("📝 논문 요약")
    st.write(st.session_state.summary)

# ✅ 워드클라우드 생성 버튼
if st.session_state.summary and korean_font_path:
    if st.button("워드클라우드 생성하기"):
        st.session_state.show_wordcloud = True

# ✅ 워드클라우드 출력
if st.session_state.show_wordcloud:
    original_buf = generate_wordcloud(st.session_state.summary, korean_font_path)
    noun_text = extract_nouns(st.session_state.summary)
    noun_buf = generate_wordcloud(noun_text, korean_font_path)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📌 원문 기반 워드클라우드")
        st.image(original_buf, use_container_width=True)

    with col2:
        st.subheader("📌 명사 기반 워드클라우드")
        st.image(noun_buf, use_container_width=True)

# ✅ 사이드바 안내
st.sidebar.info("📘 PDF 업로드 → 요약 생성 → 워드클라우드 생성 순으로 진행하세요.")
