from flask import Flask, Response
import requests

app = Flask(__name__)

# Trage hier die direkte Stream-URL oder die Quelle aus dem FM-Funknetz ein
STREAM_URL = "HIER_DIE_INTERNE_STREAM_ODER_RELAY_URL_EINTRAGEN"

@app.route('/stream')
def stream():
    def generate():
        try:
            # Verbindung zum Funknetz-Stream aufbauen
            r = requests.get(STREAM_URL, stream=True, timeout=10)
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    yield chunk
        except Exception as e:
            print(f"Fehler beim Streamen: {e}")
            
    return Response(generate(), mimetype="audio/mpeg")

@app.route('/')
def index():
    return "FM-Funknetz Relay Service läuft."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
