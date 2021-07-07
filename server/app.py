from flask import Flask

app = Flask(__name__)

# home route here
# must query the animal API for an animal and a noise – the noise should be based on the animal

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)