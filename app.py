from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

with open("words.txt", "r") as file:
    words = [line.strip() for line in file]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_word")
def get_word():
    random_word = random.choice(words)
    return jsonify({"word": random_word})

if __name__ == "__main__":
    app.run(debug=True)
