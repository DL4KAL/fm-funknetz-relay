from flask import Flask, Response, render_template_string
import requests

app = Flask(__name__)

# Ersetze dies durch die echte Stream-URL aus dem FM-Funknetz
STREAM_URL = "HIER_DEINE_FM_FUNKNETZ_STREAM_URL_EINFUEGEN"

@app.route('/stream')
def stream():
    def generate():
        try:
            # stream=True ist wichtig, damit der Audiostream kontinuierlich fließt
            r = requests.get(STREAM_URL, stream=True, timeout=10)
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    yield chunk
        except Exception as e:
            print(f"Fehler beim Streamen: {e}")
            
    return Response(generate(), mimetype="audio/mpeg")

@app.route('/')
def index():
    return "FM-Funknetz Relay läuft einwandfrei."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
