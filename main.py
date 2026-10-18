from flask import Flask, send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "MESTRE DAS CONFLUENCIAS VOZ ONLINE!"

@app.route("/falar/<texto>")
def falar(texto):
    tts = gTTS(text=texto, lang='pt', slow=False)
    tts.save("voz.mp3")
    return send_file("voz.mp3", mimetype="audio/mpeg")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
