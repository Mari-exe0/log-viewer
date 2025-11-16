from flask import Flask, request, jsonify

app = Flask(__name__)

logs = []  # store logs in memory

@app.route('/')
def home():
    return "<h1>Log Viewer</h1><p>POST /log to add logs. Visit /logs to see them.</p>"

@app.route('/log', methods=['POST'])
def add_log():
    data = request.get_json()
    message = data.get("message")
    if not message:
        return jsonify({"error": "Missing 'message'"}), 400

    logs.append(message)
    return jsonify({"status": "ok"})

@app.route('/logs')
def view_logs():
    return "<br>".join(logs)
