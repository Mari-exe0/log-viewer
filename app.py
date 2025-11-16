from flask import Flask, request, render_template_string

app = Flask(__name__)

logs = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Log Viewer</title>
    <style>
        body { font-family: Arial; background: #121212; color: white; padding: 20px; }
        .log { background: #1f1f1f; padding: 10px; margin-bottom: 10px; border-radius: 5px; }
    </style>
</head>
<body>
    <h1>Live Log Viewer</h1>

    {% for log in logs %}
        <div class="log">{{ log }}</div>
    {% endfor %}
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML, logs=logs)

@app.route('/log', methods=['POST'])
def receive_log():
    data = request.json
    msg = data.get("message", "No message")
    logs.append(msg)
    print("Log received:", msg)
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
