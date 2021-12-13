from pymongo import MongoClient
import csv

HOST = 'cluster0.flket.mongodb.net'
USER = 'vvk'
PASSWORD = 'vvk1004'
DATABASE_NAME = 'stock'
COLLECTION_NAME = '005930'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)

database = client[DATABASE_NAME]
collection = database[COLLECTION_NAME]
docs = collection.find()

raw_data = []

for doc in docs:
    raw_data.append(doc)

field_names = ['date', 'close_price', 'open_price', 'high_price', 'low_price', 'up', 'down', 'trading_volume']

with open('rawdata.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=field_names, extrasaction='ignore')
    w.writeheader()
    w.writerows(raw_data)