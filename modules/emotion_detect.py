import google.generativeai as genai

def detect_emotion(text):
    prompt = f"""
    너는 감정 분석 AI다.
    입력 문장에서 사용자의 감정을 한두 단어로만 추출해라.
    예: 슬픔, 우울, 불안, 기쁨, 외로움, 분노, 지침, 설렘 등.

    출력 형식:
    감정: <감정명>

    문장: {text}
    """

    result = genai.GenerativeModel("gemini-2.5-flash").generate_content(prompt)
    out = result.text.strip().replace("감정:", "").strip()
    return out