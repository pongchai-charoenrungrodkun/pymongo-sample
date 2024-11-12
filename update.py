import pymongo


# Create a MongoClient 
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create a database 
db = client["documentdb"]

# Create a collection 
collection = db["person"]

# Update a single document
query = {"name": "John"}
new_value = {"$set": {"age": 32}}
result = collection.update_one(query, new_value)
print(result.modified_count)

# Update multiple documents
query = {"age": {"$lt": 30}}
new_value = {"$inc": {"age": 1}}
result = collection.update_many(query, new_value)
print(result.modified_count)
