import spacy
import pandas as pd

def analyze_topic(df):
    nlp = spacy.load("en_core_web_lg")

    industry_keywords = {
        'Technical synonymity': ['technical', 'support', 'troubleshooting', 'IT assistance', 'software help', 'system maintenance', 'tech aid', 'software troubleshooting', 'technical assistance', 'IT support'],
        
        'Billing and Payments': ['billing', 'payment', 'invoice', 'invoicing', 'financial transactions', 'account billing', 'fee collection', 'payment processing', 'financial settlement', 'transaction billing'],
        
        'Customer Service': ['customer service', 'helpdesk', 'assistance', 'client support', 'user assistance', 'consumer care', 'support desk', 'client relations', 'service help', 'user support'],
        
        'Product synonymity': ['product', 'item', 'inventory', 'merchandise', 'goods', 'articles', 'commodities', 'assets', 'stock', 'materials'],
        
        'Delivery and Logistics': ['delivery', 'shipping', 'logistics', 'shipment', 'transport', 'supply chain', 'distribution', 'freight', 'cargo', 'dispatch'],
        
        'Legal synonymity': ['legal', 'law', 'regulation', 'juridical', 'compliance', 'legislative', 'statutory', 'constitutional', 'legal framework', 'regulatory compliance'],
        
        'Service synonymity': ['service', 'maintenance', 'repair', 'assistance', 'support', 'care', 'servicing', 'repairs and maintenance', 'technical service', 'customer support']
    }

    for index, row in df.iterrows():
        user_messages = [message['content'] for message in row['messages'] if message.get('role') == 'user']
        clump_text = ' '.join(user_messages)

        synonymity_scores = {key: 0 for key in industry_keywords}

        clump_tokens = nlp(clump_text.lower())
        for industry, keywords in industry_keywords.items():
            keyword_tokens = nlp(' '.join(keywords))
            similarity_score = clump_tokens.similarity(keyword_tokens)
            synonymity_scores[industry] = similarity_score

        max_industry = max(synonymity_scores, key=synonymity_scores.get)

        for industry, score in synonymity_scores.items():
            df.at[index, industry] = score

        df.at[index, 'industry'] = max_industry

    return df