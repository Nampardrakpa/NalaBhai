import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd

nltk.download('vader_lexicon')

def analyze_sentiment(df):
    sia = SentimentIntensityAnalyzer()

    df['sentiment_scores'] = df['messages'].apply(lambda x: [sia.polarity_scores(msg['content'])['compound'] for msg in x])

    df['average_sentiment'] = df['sentiment_scores'].apply(lambda x: sum(x) / len(x) if len(x) > 0 else 0)

    def assign_sentiment_label(score):
        if score >= 0.05:
            return 'positive'
        elif score <= -0.05:
            return 'negative'
        else:
            return 'neutral'

    df['sentiment_label'] = df['average_sentiment'].apply(assign_sentiment_label)

    result_df = df[['id', 'average_sentiment', 'sentiment_label']]

    return result_df