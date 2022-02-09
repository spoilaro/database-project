from flask import Flask, render_template



app = Flask(__name__)


# Routes

@app.route("/")
def home():

    html = render_template("index.html")

    return html

if __name__ == "__main__":
    app.run(debug=True)
