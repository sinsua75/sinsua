import streamlit as st
import requests
from PIL import Image

# 색상 테마
st.set_page_config(page_title="도깨비 팬 사이트", layout="wide")

# 컬러 스타일 (검정 + 남색 + 노란색 포인트)
PRIMARY_COLOR = "#0A1F44"  # 남색
SECONDARY_COLOR = "#FFD700"  # 고급 노란색
BACKGROUND_COLOR = "#000000"  # 블랙

st.markdown(
    f"""
    <style>
        body {{
            background-color: {BACKGROUND_COLOR};
            color: white;
        }}
        .title {{
            text-align: center;
            font-size: 60px;
            color: {SECONDARY_COLOR};
            font-weight: bold;
        }}
        .subtitle {{
            text-align: center;
            font-size: 25px;
            color: {PRIMARY_COLOR};
        }}
        .character-name {{
            font-size: 22px;
            color: {SECONDARY_COLOR};
            text-align: center;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- 배경 음악 (Stay With Me - 찬열, 펀치)
st.audio("https://docs.google.com/uc?export=download&id=1r2jPOT9KZt3L1Tf3vR4oWnqgkXec5B0g", format="audio/mp3", start_time=0)

# --- 헤더 이미지 (앞장)
st.image("/mnt/data/c9aec3e6-3eee-4dc2-bb9d-401d0b829093.png", use_column_width=True)

st.markdown("<div class='title'>도깨비 (Goblin)</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>공유 · 김고은 · 유인나 · 이동욱</div>", unsafe_allow_html=True)

# --- 캐릭터 슬라이드 느낌 (Streamlit Carousel 대체)
st.write("---")
st.markdown("### 주요 등장인물")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image("/mnt/data/7749c1ae-1471-46a6-9a86-addf8bbae60e.png")
    st.markdown("<div class='character-name'>김신 (공유)</div>", unsafe_allow_html=True)

with col2:
    st.image("/mnt/data/bbad706b-31a1-436b-930b-60be7f838855.png")
    st.markdown("<div class='character-name'>지은탁 (김고은)</div>", unsafe_allow_html=True)

with col3:
    st.image("/mnt/data/86fee342-8ba1-428a-abaa-9ba554796bff.png")
    st.markdown("<div class='character-name'>써니 (유인나)</div>", unsafe_allow_html=True)

with col4:
    st.image("/mnt/data/e27d9976-c9f2-4fe1-956b-e15be3b66235.png")
    st.markdown("<div class='character-name'>저승사자 (이동욱)</div>", unsafe_allow_html=True)

# --- 줄거리 섹션
st.write("---")
st.markdown("## 📖 드라마 줄거리")
st.write("""
불멸의 삶을 살고 있는 도깨비 김신은 저승사자와 함께 기묘한 동거를 시작한다. 
그리고 어느 날, 자신의 신부라는 운명을 가진 소녀 지은탁을 만나면서 이야기는 전개된다. 
사랑, 운명, 죽음을 둘러싼 판타지 로맨스 드라마.
""")

# --- API 연동 (OTT 별점, 순위)
# 여기서는 예시로 TMDB API 사용
API_KEY = "YOUR_TMDB_API_KEY"
url = f"https://api.themoviedb.org/3/tv/67415?api_key={API_KEY}&language=ko-KR"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    rating = data.get("vote_average", "N/A")
    vote_count = data.get("vote_count", "N/A")
    st.write("---")
    st.markdown("## ⭐ 드라마 평점 (TMDB 기준)")
    st.metric(label="평균 평점", value=f"{rating}/10")
    st.metric(label="투표 수", value=vote_count)
else:
    st.warning("API 정보를 불러올 수 없습니다.")

# --- Footer
st.write("---")
st.markdown("<div style='text-align:center; color:gray;'>© 도깨비 팬 사이트 | 제작: Streamlit</div>", unsafe_allow_html=True)
