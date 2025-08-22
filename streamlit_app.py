import os
import streamlit as st
import requests
import streamlit.components.v1 as components

# ---------------------------------------------
# 기본 설정
# ---------------------------------------------
st.set_page_config(page_title="도깨비 팬 사이트", layout="wide")

# 색상 테마 (검정 + 남색 + 노란색 포인트)
PRIMARY_COLOR = "#0A1F44"   # 남색
SECONDARY_COLOR = "#FFD700"  # 고급 노란색
BACKGROUND_COLOR = "#000000" # 블랙

# 에셋 경로 (Codespaces/로컬 모두 동작하도록 레포 안의 상대 경로 사용)
ASSETS_DIR = "assets"
IMG_HERO = f"{ASSETS_DIR}/hero.jpg"          # 마지막에 준 사진(연기+안개씬)을 hero로 사용
IMG_GONG = f"{ASSETS_DIR}/gongyoo.jpg"       # 공유 1번 사진
IMG_KIM  = f"{ASSETS_DIR}/kimgoeun.jpg"      # 김고은 2번 사진
IMG_YOO  = f"{ASSETS_DIR}/yoinna.jpg"        # 유인나 3번 사진
IMG_LEE  = f"{ASSETS_DIR}/leedongwook.jpg"   # 이동욱 4번 사진
AUDIO_MP3 = f"{ASSETS_DIR}/stay_with_me.mp3" # (선택) 로컬 mp3를 넣으면 자동 재생 시도

# ---------------------------------------------
# 스타일
# ---------------------------------------------
st.markdown(
    f"""
    <style>
        .stApp {{ background-color: {BACKGROUND_COLOR}; color: #ffffff; }}
        .title {{ text-align:center; font-size:56px; color:{SECONDARY_COLOR}; font-weight:800; }}
        .subtitle {{ text-align:center; font-size:20px; color:{PRIMARY_COLOR}; }}
        .character-name {{ font-size:20px; color:{SECONDARY_COLOR}; text-align:center; margin-top:8px; }}
        .section-title {{ font-size:26px; color:{SECONDARY_COLOR}; font-weight:700; margin: 8px 0 4px; }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------
# 배경 음악 (자동 재생 시도 + 플레이어 백업)
#  - 브라우저 정책상 자동 재생이 차단될 수 있음 (특히 iOS/Safari). 그 경우 아래 st.audio 플레이어로 수동 재생.
# ---------------------------------------------
if os.path.exists(AUDIO_MP3):
    # iFrame 안에서 <audio autoplay> 시도 (일부 브라우저에서만 동작)
    components.html(
        f"""
        <audio autoplay loop>
            <source src='{AUDIO_MP3}' type='audio/mpeg'>
        </audio>
        """,
        height=0,
    )
    st.audio(AUDIO_MP3, format="audio/mp3")  # 사용자 수동 재생용 플레이어
else:
    # 로컬 mp3가 없으면 유튜브 임베드(공식 MV 링크를 넣어 사용자가 재생)
    # 자동재생은 정책상 막히는 경우가 많아 버튼 재생을 권장
    YOUTUBE_ID = "y-C22fFaYvE"  # 예: (사용자가 원하는 공식 영상 ID로 교체 가능)
    components.html(
        f"""
        <div style='display:flex; justify-content:center;'>
            <iframe width="560" height="315" src="https://www.youtube.com/embed/{YOUTUBE_ID}" 
                title="YouTube video player" frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen>
            </iframe>
        </div>
        """,
        height=330,
    )

# ---------------------------------------------
# Hero 섹션 (맨 앞장)
# ---------------------------------------------
if os.path.exists(IMG_HERO):
    st.image(IMG_HERO, use_container_width=True)
else:
    st.warning("hero.jpg가 assets 폴더에 없습니다. 이미지를 업로드해 주세요.")

st.markdown("<div class='title'>도깨비 (Goblin)</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>공유 · 김고은 · 유인나 · 이동욱</div>", unsafe_allow_html=True)

st.divider()
st.markdown("<div class='section-title'>주요 등장인물</div>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    if os.path.exists(IMG_GONG):
        st.image(IMG_GONG, use_container_width=True)
    else:
        st.error("gongyoo.jpg가 없어요")
    st.markdown("<div class='character-name'>김신 (공유)</div>", unsafe_allow_html=True)

with col2:
    if os.path.exists(IMG_KIM):
        st.image(IMG_KIM, use_container_width=True)
    else:
        st.error("kimgoeun.jpg가 없어요")
    st.markdown("<div class='character-name'>지은탁 (김고은)</div>", unsafe_allow_html=True)

with col3:
    if os.path.exists(IMG_YOO):
        st.image(IMG_YOO, use_container_width=True)
    else:
        st.error("yoinna.jpg가 없어요")
    st.markdown("<div class='character-name'>써니 (유인나)</div>", unsafe_allow_html=True)

with col4:
    if os.path.exists(IMG_LEE):
        st.image(IMG_LEE, use_container_width=True)
    else:
        st.error("leedongwook.jpg가 없어요")
    st.markdown("<div class='character-name'>저승사자 (이동욱)</div>", unsafe_allow_html=True)

# ---------------------------------------------
# 줄거리
# ---------------------------------------------
st.divider()
st.markdown("<div class='section-title'>📖 드라마 줄거리</div>", unsafe_allow_html=True)
st.write(
    """
    불멸의 삶을 살고 있는 도깨비 김신은 저승사자와 함께 기묘한 동거를 시작한다.
    그리고 어느 날, 자신의 신부라는 운명을 가진 소녀 지은탁을 만나면서 이야기가 전개된다.
    사랑, 운명, 죽음을 둘러싼 판타지 로맨스 드라마.
    """
)

# ---------------------------------------------
# API 연동 (OTT/글로벌 평점 예시: TMDB)
#  - 사용 API: TMDB (The Movie Database) TV 상세 API
#  - 엔드포인트 예: https://api.themoviedb.org/3/tv/67415?api_key=...&language=ko-KR
#  - TV id 67415는 "도깨비"(Goblin)
# ---------------------------------------------
API_KEY = st.secrets.get("TMDB_API_KEY", "YOUR_TMDB_API_KEY")
url = f"https://api.themoviedb.org/3/tv/67415?api_key={API_KEY}&language=ko-KR"
try:
    response = requests.get(url, timeout=10)
    if response.ok:
        data = response.json()
        rating = data.get("vote_average", "N/A")
        vote_count = data.get("vote_count", "N/A")
        st.divider()
        st.markdown("<div class='section-title'>⭐ 드라마 평점 (TMDB 기준)</div>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            st.metric(label="평균 평점", value=f"{rating}/10")
        with c2:
            st.metric(label="투표 수", value=vote_count)
    else:
        st.warning("TMDB API 응답을 가져오지 못했습니다. API Key를 확인하세요.")
except Exception as e:
    st.warning(f"API 호출 중 오류: {e}")

# ---------------------------------------------
# Footer
# ---------------------------------------------
st.divider()
st.markdown("<div style='text-align:center; color:gray;'>© 도깨비 팬 사이트 | 제작: Streamlit</div>", unsafe_allow_html=True)
