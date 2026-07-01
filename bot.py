import requests

BOT_TOKEN = "8735457027:AAEuaa_2lqs9CY09-o0LXE_UCVXLAOQymnk"
CHAT_ID = "1653546996"

message = "✅ Naresh Alert Bot Working!"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message
})
