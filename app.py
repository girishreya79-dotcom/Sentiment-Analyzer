from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    sentiment = None
    polarity = None
    text = ""

    if request.method == "POST":
        text = request.form.get("text", "").strip()

        if text:
            analysis = TextBlob(text)
            polarity = round(analysis.sentiment.polarity, 2)

            if polarity > 0:
                sentiment = "Positive"
            elif polarity < 0:
                sentiment = "Negative"
            else:
                sentiment = "Neutral"

    return render_template(
        "index.html",
        sentiment=sentiment,
        polarity=polarity,
        text=text
    )


if __name__ == "__main__":
    app.run(debug=True)