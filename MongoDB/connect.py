from pymongo import MongoClient

# MongoDB connection string
mongodb_uri = "mongodb://<username>:<password>@<mongodb-host>:<mongodb-port>/<database>"

# Connect to MongoDB
client = MongoClient(mongodb_uri)

# Access a specific database
db = client['your_database']
