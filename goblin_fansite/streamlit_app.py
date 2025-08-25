import streamlit as st
import requests
import os

# 페이지 설정
st.set_page_config(page_title="도깨비 팬사이트", page_icon="✨", layout="wide")

# 제목
st.title("도깨비 (Goblin) 팬사이트")

# -----------------------------
# 캐릭터 정보
# -----------------------------
st.header("주요 등장인물")

characters = [
    {"name": "김신 (공유)", "image": "gongyoo.jpg"},
    {"name": "지은탁 (김고은)", "image": "kimgoeun.jpg"},
    {"name": "써니 (유인나)", "image": "yoina.jpg"},
    {"name": "저승사자 (이동욱)", "image": "leedongwook.jpg"},
]

col1, col2 = st.columns(2)
for i, char in enumerate(characters):
    with [col1, col2][i % 2]:
        img_path = os.path.join("assets", char["image"])
        if os.path.exists(img_path):
            st.image(img_path, width=250)
        else:
            st.error(f"{char['name']} 이미지가 assets 폴더에 없습니다.")
        st.write(char["name"])

# -----------------------------
# 드라마 줄거리
# -----------------------------
st.header("📖 드라마 줄거리")
st.write("""
불멸의 삶을 살고 있는 도깨비 김신은 저승사자와 함께 기묘한 동거를 시작한다.  
그러던 어느 날, 자신의 신부라는 운명을 가진 소녀 지은탁을 만나면서 이야기가 전개된다.  
사랑, 운명, 죽음을 둘러싼 판타지 로맨스 드라마.
""")

# -----------------------------
# TMDB API 연결 (드라마 정보 가져오기)
# -----------------------------
st.header("🎬 TMDB에서 불러온 정보")

api_key = st.secrets["272f14ae01185e887d38bc686d56098f"]
url = f"https://api.themoviedb.org/3/tv/67915?api_key={api_key}&language=ko-KR"  # 도깨비 TMDB ID = 67915
res = requests.get(url)

if res.status_code == 200:
    data = res.json()
    st.subheader(data["name"])
    st.write(data["overview"])
    st.image("https://image.tmdb.org/t/p/w500" + data["poster_path"])
else:
    st.error("TMDB API 호출 실패. API Key를 확인하세요.")
