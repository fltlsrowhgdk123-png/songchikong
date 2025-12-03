import streamlit as st
import google.generativeai as genai
import json
import re
import matplotlib.pyplot as plt
import pandas as pd
from modules.emotion_detect import detect_emotion
from modules.recommend_model import psychological_recommend_base, psychological_recommend_with_history
from modules.youtube_search import search_youtube_music
from modules.history import save_emotion, get_recent_emotions, get_history_list
from modules.ui_cards import song_card

# ======================================
# API KEY
# ======================================
GEMINI_API_KEY = ""GEMINI_API_KEY""
YOUTUBE_API_KEY = "YOUTUBE_API_KEY"
genai.configure(api_key="GEMINI_API_KEY")

# ======================================
# Streamlit UI
# ======================================
st.set_page_config(page_title="감정 기반 음악 추천 v3", layout="centered")
st.title("🎵 감정 기반 음악 추천 풀버전 v3")
st.caption("나의 감정을 분석하고 맞춤 음악을 추천해주는 AI 서비스")

st.markdown("---")

# 입력받기
user_text = st.text_input("지금 기분이나 상황을 알려줘", "")

if st.button("음악 추천받기"):
    with st.spinner("감정 분석 중..."):
        emotion = detect_emotion(user_text)

    st.subheader("1) 감정 분석 결과")
    st.write(f"감정: **{emotion}**")

    # 감정 저장
    save_emotion(emotion)

    # 히스토리 가져오기
    history_list = get_history_list()

    # 심리 분석
    with st.spinner("심리 기반 추천 생성 중..."):
        analysis_text = psychological_recommend_with_history(emotion, history_list)
    st.subheader("🧠 심리 기반 음악 분석")
    st.write(analysis_text)

    # 유튜브 검색
    st.subheader("🎧 추천 음악 3곡")
    songs = search_youtube_music(emotion + " 음악", YOUTUBE_API_KEY)

    for s in songs:
        song_card(
            title=s["title"],
            channel=s["channel"],
            thumbnail=s["thumbnail"],
            url=s["url"]
        )

    # 히스토리 그래프
    st.markdown("---")
    st.subheader("📈 감정 변화 히스토리")
    history = get_history_list()
    if history:
        df = pd.DataFrame(history, columns=["emotion"])
        df["index"] = range(1, len(df)+1)
        st.line_chart(df.set_index("index"))
    else:
        st.info("아직 감정 히스토리가 없습니다!")

    # 감정 통계
    st.subheader("🎯 감정 비율 통계")
    if history:
        emotion_count = df["emotion"].value_counts()
        st.bar_chart(emotion_count)
    else:

        st.info("감정 데이터가 부족합니다.")
