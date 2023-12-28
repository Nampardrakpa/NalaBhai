import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
nltk.download('punkt')

sia = SentimentIntensityAnalyzer()

def analyze_satisfaction(conversation, confidence_score, sentiment_score):
    messages = [msg['content'] for msg in conversation]
    message_text = ' '.join(messages)
    
    conversation_sentiment = sia.polarity_scores(message_text)['compound']
    
    confidence_threshold = 0.7
    sentiment_threshold = 0.5
    
    if confidence_score >= confidence_threshold and conversation_sentiment >= sentiment_threshold:
        return 'Satisfactory'
    else:
        dissatisfaction_phrases = ["I'm sorry, but I cannot", "I am not sure", "I don't know", "I couldn't find the information", "I apologize for the inconvenience", "I'm afraid I cannot assist with that", "I'm not able to help with that", "Unfortunately, I cannot provide the requested", "I'm sorry if my response is not helpful", "I'm unable to fulfill your request"]
        if any(phrase.lower() in message_text.lower() for phrase in dissatisfaction_phrases):
            return 'Not Satisfactory'
        else:
            return 'Satisfactory'