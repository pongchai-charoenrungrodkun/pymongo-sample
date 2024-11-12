import pymongo


# Create a MongoClient 
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create a database 
db = client["documentdb"]

# Create a collection 
collection = db["person"]

# Insert a single document
document = {"name": "John", "age": 30}
result = collection.insert_one(document)
print(result.inserted_id)

# Insert multiple documents
documents = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 35},
    {"name": "Charlie", "age": 45}
]
result = collection.insert_many(documents)
print(result.inserted_ids)
