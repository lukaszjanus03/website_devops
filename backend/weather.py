from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
# TO JEST NOWOSC: Pozwalamy na komunikacje z innych portow
CORS(app)

@app.route('/')
def get_weather():
    # Kraków
    url = "https://api.open-meteo.com/v1/forecast?latitude=50.06&longitude=19.94&current_weather=true"

    try:
        response = requests.get(url)
        data = response.json()
        current = data.get('current_weather', {})

        return jsonify({
            "miasto": "Krakow",
            "temperatura": current.get('temperature'),
            "wiatr": current.get('windspeed'),
            "kod_pogody": current.get('weathercode')
        })
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
