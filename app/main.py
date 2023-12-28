# TextClassificationAPI/app/main.py

from flask import Flask, request, jsonify
from app.config import Config
from app.database.mongodb import save_to_mongodb

app = Flask(__name__)
app.config.from_object(Config)

mongodb_uri = app.config['MONGODB_URI']

@app.route('/classify', methods=['POST'])
def classify_text():
    try:
        data = request.get_json()

        save_to_mongodb(data, database_name='your_database_name', collection_name='your_collection_name')

        return jsonify({"message": "Text classified and saved successfully!"}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True)