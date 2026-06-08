from flask import Flask, request, jsonify
import requests
import config

app = Flask(__name__)

ml_access_token = None

@app.route("/")
def home():
    return "Webhook activo ✅"

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        return jsonify({"status": "ok"}), 200
    data = request.json
    print("Notificación recibida:", data)
    return jsonify({"status": "recibido"}), 200

@app.route("/callback")
def callback():
    global ml_access_token
    code = request.args.get("code")
    if not code:
        return "Error: no se recibió código", 400
    response = requests.post("https://api.mercadolibre.com/oauth/token", data={
        "grant_type": "authorization_code",
        "client_id": config.ML_APP_ID,
        "client_secret": config.ML_CLIENT_SECRET,
        "code": code,
        "redirect_uri": config.ML_REDIRECT_URI
    })
    tokens = response.json()
    ml_access_token = tokens.get("access_token")
    print("Token obtenido:", ml_access_token)
    return "✅ Autorización exitosa. Puedes cerrar esta ventana."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)