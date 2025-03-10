from textblob import TextBlob

def analyse_sentiment(text):
    blob = TextBlob(text)
    
    sentiment = blob.sentiment
    polarity = sentiment.polarity


    if polarity > 0:
        category = "Positive"
    elif polarity < 0:
        category = "Negative"
    else:
        category = "Neutral"

    return category

text = input("Enter your text: ")
result = analyse_sentiment(text)
print(f"Sentiment: {result}")