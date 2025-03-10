from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

def analyze_sentiment(text):
    blob = TextBlob(text)
    
    sentiment = blob.sentiment
    polarity = sentiment.polarity # from -1 to 1
    
    if polarity > 0:
        category = "Positive"
    elif polarity < 0:
        category = "Negative"
    else:
        category = "Neutral"

    return category

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None

    if request.method == "POST":
        text = request.form['text']
        sentiment = analyze_sentiment(text)

    print("Sentiment to be rendered:", sentiment)

    return render_template('index.html', sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)

