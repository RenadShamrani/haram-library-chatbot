from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import aiohttp

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# رابط Rasa المنشور على Render
RASA_SERVER_URL = "https://haram-library-chatbot.onrender.com/webhooks/rest/webhook"

class UserMessage(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
async def main():
    return """
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <title>مساعد مكتبة الحرم</title>
        <style>
            body { font-family: 'Arial', sans-serif; background: #f0f2f5; margin: 0; padding: 0; display: flex; flex-direction: column; align-items: center; }
            .container { max-width: 600px; width: 100%; padding: 20px; background: white; margin-top: 50px; box-shadow: 0 0 10px rgba(0,0,0,0.1); border-radius: 8px; }
            img { width: 120px; margin-bottom: 20px; }
            h2 { color: #1c3b5a; }
            .chat-box { max-height: 400px; overflow-y: auto; border: 1px solid #ccc; padding: 10px; margin-top: 20px; background: #fafafa; border-radius: 5px; }
            .msg { margin: 10px 0; }
            .user { color: #1c3b5a; font-weight: bold; }
            .bot { color: #444; }
            input[type="text"] { width: 80%; padding: 10px; font-size: 16px; border: 1px solid #ccc; border-radius: 5px; }
            button { padding: 10px 15px; background: #1c3b5a; color: white; border: none; border-radius: 5px; margin-right: 5px; cursor: pointer; }
        </style>
    </head>
    <body>
        <div class="container">
            <img src="/static/logo.jpg" alt="شعار الهيئة" />
            <h2>مرحبًا بكم في خدمة الرد الآلي لمكتبة الحرم</h2>
            <div class="chat-box" id="chat-box"></div>
            <form id="chat-form" onsubmit="sendMessage(event)">
                <input id="user-input" type="text" placeholder="اكتب سؤالك هنا..." required />
                <button type="submit">إرسال</button>
            </form>
        </div>
        <audio id="notif-sound" src="/static/notification.mp3" preload="auto"></audio>
        <script>
            async function sendMessage(event) {
                event.preventDefault();
                const input = document.getElementById("user-input");
                const chatBox = document.getElementById("chat-box");
                const message = input.value.trim();
                if (!message) return;

                chatBox.innerHTML += `<div class="msg user">🧑‍💼 أنت: ${message}</div>`;
                input.value = "";
                chatBox.scrollTop = chatBox.scrollHeight;

                const response = await fetch("/chat", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ message })
                });

                const data = await response.json();
                const reply = data.reply;

                chatBox.innerHTML += `<div class="msg bot">🤖 البوت: ${reply}</div>`;
                chatBox.scrollTop = chatBox.scrollHeight;

                document.getElementById("notif-sound").play();
            }
        </script>
    </body>
    </html>
    """

@app.post("/chat")
async def chat_with_bot(user_message: UserMessage):
    async with aiohttp.ClientSession() as session:
        async with session.post(
            url=RASA_SERVER_URL,
            json={"sender": "user", "message": user_message.message},
        ) as resp:
            bot_response = await resp.json()

    reply = bot_response[0]['text'] if bot_response else "لم أفهم، من فضلك أعد المحاولة."
    return {"reply": reply}