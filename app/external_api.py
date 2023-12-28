# TextClassificationAPI/app/external_api.py

import requests

def get_all_conversations(chatbot_id, secret_key, start_date, end_date):
    url = 'https://www.chatbase.co/api/v1/get-conversations'
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {secret_key}'
    }
    params = {
        'chatbotId': chatbot_id,
        'startDate': start_date,
        'endDate': end_date,
    }

    try:
        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data.get('data', [])
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None