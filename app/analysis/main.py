# app/analysis/main.py

from app.analysis.data_cleaning import clean_data
from app.analysis.intent_analysis import analyze_intent
from app.analysis.satisfaction_rating import analyze_satisfaction
from app.analysis.sentiment_analysis import analyze_sentiment
from app.analysis.topic_analysis import analyze_topic
from app.analysis.final_compiler import final_compiler

def text_classifier(data):
    try:
        if data is not None:
            cleaned_data = clean_data(data)
            intent_result = analyze_intent(cleaned_data)
            sentiment_result = analyze_sentiment(intent_result)
            topic_result = analyze_topic(sentiment_result)
            satisfaction_result = analyze_satisfaction(topic_result)
            final_compiled = final_compiler(satisfaction_result)

            return {
                final_compiled
            }
        else:
            print("Failed to retrieve conversations from the external API.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
