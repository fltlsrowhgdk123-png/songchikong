import streamlit as st

def song_card(title, url, thumbnail, channel):
    # HTML 카드 템플릿
    card_html = f"""
        <div style="
            border:1px solid #ccc;
            padding:12px;
            border-radius:10px;
            margin-bottom:15px;
            background:#fafafa;
            width:320px;
        ">
            <img src="{thumbnail}" width="300" style="border-radius:10px;">
            <h4 style="margin-top:10px;">{title}</h4>
            <p style="margin:0; color:#555;">채널: {channel}</p>
            <a href="{url}" target="_blank" style="color:#0066cc; font-weight:bold;">
                ▶ 유튜브로 이동
            </a>
        </div>
    """

    st.markdown(card_html, unsafe_allow_html=True)