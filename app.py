from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>🚀 My First Docker Flask App</h1>
    <h2>Running inside a Docker Container</h2>
    <p>Created by Akash Francis</p>
    """


@app.route("/health")
def health():
    return "Application is healthy"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
