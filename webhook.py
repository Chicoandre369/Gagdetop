from flask import Flask, request, jsonify

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    