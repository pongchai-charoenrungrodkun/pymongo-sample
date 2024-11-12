import pymongo


# Create a MongoClient 
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create a database 
db = client["documentdb"]

# Create a collection 
collection = db["person"]

# Delete a single document
print("\nDelete a single document")
query = {"name": "John"}
result = collection.delete_one(query)
print(result.deleted_count)

# Delete multiple documents
print("\nDelete multiple documents")
query = {"age": {"$gt": 40}}
result = collection.delete_many(query)
print(result.deleted_count)
