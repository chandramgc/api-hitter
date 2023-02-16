import fastavro

# Define the schema for the Avro file
schema = {
    "type": "record",
    "name": "Example",
    "fields": [
        {"name": "name", "type": "string"},
        {"name": "age", "type": "int"},
        {"name": "email", "type": "string"}
    ]
}

# Create some sample data for the Avro file
data = [
    {"name": "John Doe", "age": 30, "email": "johndoe@example.com"},
    {"name": "Jane Smith", "age": 25, "email": "janesmith@example.com"},
    {"name": "Bob Johnson", "age": 40, "email": "bobjohnson@example.com"}
]

# Open a file for writing in binary mode
with open('example.avro', 'wb') as out:
    # Create a fastavro writer object
    fastavro.writer(out, schema, data)

# Read the Avro file to make sure it was generated correctly
with open('example.avro', 'rb') as fo:
    avro_reader = fastavro.reader(fo)
    for record in avro_reader:
        print(record)
