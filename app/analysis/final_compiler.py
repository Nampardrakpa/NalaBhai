import pandas as pd

def final_compiler(df):

    df.drop(['Technical synonymity', 'Billing and Payments', 'Customer Service', 
         'Product synonymity', 'Delivery and Logistics', 'Legal synonymity', 
         'Service synonymity', 'sentiment_scores', 'average_sentiment'], axis=1, inplace=True)
    
    return df