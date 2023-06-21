# Find documents that match a specific criteria
result = collection.find({"field_name": "field_value"})

# Iterate over the query result
for document in result:
    # Process each document
    print(document)
