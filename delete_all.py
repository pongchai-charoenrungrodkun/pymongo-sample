import pymongo


# Create a MongoClient 
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create a database 
db = client["documentdb"]

# Create a collection 
collection = db["person"]

# Find all documents
print("\nFind all documents")
query = {}
documents = collection.find(query)
for document in documents:
   print(document)
if documents.retrieved == 0: print("No matching documents found")

# Delete a single document
print("\nDelete all document")
query = {}
result = collection.delete_many(query)
print(result.deleted_count)

