from flask import Flask

app = Flask(__name__)

# animal generator route here

# animal noise generator route here

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)