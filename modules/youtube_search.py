import requests

def search_youtube_music(query, api_key, max_results=3):
    url = "https://www.googleapis.com/youtube/v3/search"

    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": 10,
        "key": api_key
    }

    response = requests.get(url, params=params)
    data = response.json()

    # 너무 명확한 팬메이드/플리/잡음만 제외
    banned_words = [
        "fanmade", "fan made", "playlist", "mix", "remix",
        "sped up", "slowed", "reaction", "edit", "shorts"
    ]

    results = []

    for item in data.get("items", []):
        snippet = item["snippet"]
        title = snippet["title"].lower()
        channel = snippet["channelTitle"].lower()
        video_id = item["id"]["videoId"]
        thumbnail = snippet["thumbnails"]["high"]["url"]

        # 팬메이드/플리 글자 포함되면 제외
        if any(b in title for b in banned_words):
            continue

        results.append({
            "title": snippet["title"],
            "channel": snippet["channelTitle"],
            "url": f"https://www.youtube.com/watch?v={video_id}",
            "thumbnail": thumbnail
        })

        if len(results) >= max_results:
            break

    return results