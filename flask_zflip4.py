from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

MONGO_URI = "mongodb+srv://khairunnyisa:Nisa1006!@cluster0.qmxek.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "SIC-ZFlip4"
COLLECTION_NAME = "iot"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

@app.route('/save', methods=['POST'])
def save_data():
    data = request.get_json()

    suhu = data.get("temperature", {}).get("value")
    kelembaban = data.get("humidity", {}).get("value")
    light = data.get("light", {}).get("value")
    motion = data.get("motion", {}).get("value")
    
    if suhu is None or kelembaban is None or light is None or motion is None:
        return jsonify({"error": "Data suhu, kelembaban, light, dan motion wajib disertakan."}), 400

    record = {
        "suhu": suhu,
        "kelembaban": kelembaban,
        "light": light,
        "motion": motion
    }
    collection.insert_one(record)
    
    return jsonify({"message": "Data berhasil disimpan."}), 201

if __name__ == '__main__':
    app.run(host="192.168.115.68", port=7000)
