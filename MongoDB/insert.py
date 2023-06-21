# Assuming you have received data from Kafka in a variable called `data`

# Access a specific collection
collection = db['your_collection']

# Insert a single document
collection.insert_one(data)

# Insert multiple documents
collection.insert_many(data_list)
