from flask import Flask, request, jsonify
import requests
import config
import json
import os

app = Flask(__name__)

TOKEN_FILE = "tokens.json"

def guardar_token(data):
    with open(TOKEN_FILE, "w") as f:
        json.dump(data, f)

def cargar_token():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r") as f:
            return json.load(f)
    return None

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
    guardar_token(tokens)
    print("Token guardado:", tokens.get("access_token"))
    return "✅ Autorización exitosa. Puedes cerrar esta ventana."

@app.route("/token")
def ver_token():
    tokens = cargar_token()
    if tokens:
        return jsonify({"access_token": tokens.get("access_token")})
    return jsonify({"error": "No hay token guardado"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)