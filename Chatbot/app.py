from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from langi import chat
from memory import memory
app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat_route():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"response": "No message received"})
    response = chat(user_input)
    return jsonify({"response": response})

@app.route("/history", methods=["GET"])
def history():
    clean = [
        {"role": msg["role"], "content": msg.get("display") or msg.get("content")}
        for msg in memory
    ]

    return jsonify({"messages": clean})


if __name__ == "__main__":
    app.run(debug=False)