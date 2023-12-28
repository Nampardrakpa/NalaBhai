# TextClassificationAPI/tasks/midnight_task.py

import schedule
import time
from datetime import datetime, timedelta
from app.analysis.main import text_classifier
from app.database.mongodb import save_to_mongodb
from app.external_api import get_all_conversations

def get_date_range():
    # Calculate the date range from tonight's midnight till yesterday's midnight
    today_midnight = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    start_date = (today_midnight - timedelta(days=1)).strftime('%Y-%m-%d')
    end_date = today_midnight.strftime('%Y-%m-%d')
    return start_date, end_date

def midnight_task(data):
    try:
        if data is not None:
            send_to_mongoDB = text_classifier(data)

            save_to_mongodb({
                send_to_mongoDB
            })
        else:
            print("Failed to retrieve conversations from the external API.")
    except Exception as e:
        print(f"An error occurred: {e}")

chatbot_id = 'JXDhULUtu9dRHu0LmJIKh'
secret_key = 'fa49ddc3-5b60-4353-90fe-92cf341daae2'
start_date, end_date = get_date_range()
data = get_all_conversations(chatbot_id, secret_key, start_date, end_date)

schedule.every().day.at("00:00").do(midnight_task, data)

while True:
    schedule.run_pending()
    time.sleep(1)
