import google.generativeai as genai
import json

def psychological_recommend_base(emotion):
    emotion = emotion.replace(" ", "")

    mapping = {
        "슬픔": "위로 + 안정 + 희망",
        "우울": "위로 + 공감",
        "외로움": "따뜻함 + 연결감",
        "불안": "안정 + 자신감",
        "분노": "진정 + 안정",
        "지침": "회복 + 편안함",
        "스트레스": "편안함 + 안정",
        "기쁨": "신남 + 진취성",
        "설렘": "긍정 + 에너지"
    }

    return mapping.get(emotion, "감정 기반 음악")


def build_recommend_prompt(emotion, psycho_goal):
    return f"""
    너는 감정 기반 + 스포츠심리 기반 음악 추천 AI다.

    사용자 감정: {emotion}
    심리적 목표: {psycho_goal}

    한국 대중가요 10곡을 아래 JSON 형식으로만 추천해라.

    {{
      "songs": [
        {{
          "title": "",
          "artist": "",
          "reason": "",
          "lyric": "",
          "interpretation": ""
        }}
      ]
    }}

    코드블록 사용 금지.
    설명 금지.
    """

def psychological_recommend_with_history(current_emotion, history):
    prompt = f"""
    사용자의 현재 감정: {current_emotion}
    과거 감정 흐름 데이터: {history}

    패턴을 분석해서,
    '지금 감정에서 가장 도움이 될 음악 성향'을 설명하고,
    왜 이런 음악을 추천하는지 심리학적으로 정당화해줘.
    """

    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text