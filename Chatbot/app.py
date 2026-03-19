from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from langi import chat
from memory import memory
from bg import getImg
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
    return jsonify({"messages": memory})

@app.route("/background", methods=["GET"])
def background():
    img_url = getImg()
    return jsonify({"img_url": img_url})

if __name__ == "__main__":
    app.run(debug=False)