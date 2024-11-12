import pymongo


# Create a MongoClient 
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create a database 
db = client["documentdb"]

# Create a collection 
collection = db["person"]

# Find a single document
print("\nFind a single document")
query = {"name": "John"}
document = collection.find_one(query)
print(document)

# Find multiple documents
print("\nFind multiple documents age > 30")
query = {"age": {"$gt": 30}}
documents = collection.find(query)
for document in documents:
   print(document)
if documents.retrieved == 0: print("No matching documents found")

# Find all documents
print("\nFind all documents")
query = {}
documents = collection.find(query)
for document in documents:
   print(document)
if documents.retrieved == 0: print("No matching documents found")
