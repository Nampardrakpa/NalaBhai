# app/analysis/intent_analysis.py

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import word_tokenize
import pandas as pd

# Download NLTK resources
nltk.download('vader_lexicon')
nltk.download('punkt')

sia = SentimentIntensityAnalyzer()

def analyze_intent(messages):
    user_messages = [msg['content'] for msg in messages if msg['role'] == 'user']
    message_text = ' '.join(user_messages)
    
    tokens = word_tokenize(message_text.lower())
    
    request_keywords = ['seek', 'inquire', 'demand', 'plead', 'beseech', 'implore', 'entreat', 'petition', 'beg', 'ask for', 'request', 'call for', 'petition for', 'urge', 'solicit', 'wish for', 'crave', 'desire', 'covet', 'hope for', 'appeal', 'plea', 'query', 'question', 'interrogate', 'pose', 'probe', 'inquisition', 'where', 'when', 'how', 'what', 'please', 'kindly', 'could you', 'would you', 'can you', 'may I', 'mind if I', 'help', 'assist', 'guide', 'advise', 'provide', 'supply', 'render', 'grant', 'favor', 'accommodate', 'facilitate', 'support']
    issue_keywords = ['concern', 'trouble', 'matter', 'difficulty', 'challenge', 'hitch', 'obstacle', 'hurdle', 'hiccup', 'snag', 'dilemma', 'predicament', 'setback', 'bug', 'glitch', 'error', 'fault', 'flaw', 'defect', 'issue', 'grievance', 'annoyance', 'discrepancy', 'problematic', 'complication', 'headache', 'quandary', 'nuisance', 'drawback', 'impediment', 'snag', 'pitfall', 'shortcoming', ' snag', 'trouble', 'pickle', 'woe', 'predicament', 'mishap', 'challenge', 'difficulty', 'obstacle', 'hassle', 'hitch', 'dilemma', 'conundrum', 'predicament', 'pitfall', 'obstacle', 'hurdle', 'quandary', 'setback', 'hiccup', 'misstep', 'bug', 'glitch', 'snag', 'error', 'fault', 'defect', 'trouble', 'headache', 'nuisance', 'complication', 'discrepancy', 'concern', 'grievance', 'annoyance', 'issue']
    greeting_keywords = ['hi', 'hello', 'kuzu', 'goodbye', 'hey', 'yo', "what's up", 'howdy', 'greetings', 'sup', 'hiya', 'aloha', 'hola', 'hey there', 'hiyah', "how's it going", "how's tricks", 'hi there', "how's everything", "how's life", "what's going on", "what's happening", 'hi-ya', 'how do you do', 'hi-de-ho', 'hail', 'salutations', 'cheerio', 'ciao', 'later', 'see you', 'see ya', 'bye', 'goodbye', 'farewell', 'ta-ta', 'so long', 'take care', 'catch you later', 'adios', 'peace out', 'laters', "g'day"]
    
    if any(keyword in tokens for keyword in request_keywords):
        return 'Request'
    elif any(keyword in tokens for keyword in issue_keywords):
        return 'Issue'
    elif any(keyword in tokens for keyword in greeting_keywords):
        return 'Greeting'
    else:
        return 'Opinion'

def perform_intent_analysis(df):
    df['intent'] = df['messages'].apply(analyze_intent)

    return df[['intent']]