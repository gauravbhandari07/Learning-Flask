from flask import Flask, render_template, request
from sentiment import analyze_sentiment

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    sentiment = None
    polarity = None

    if request.method == "POST":
        text = request.form["text"]
        sentiment, polarity = analyze_sentiment(text)

    return render_template("index.html",
                           sentiment=sentiment,
                           polarity=polarity)

if __name__ == "__main__":
    app.run(debug=True)