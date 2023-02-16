import os
from avro import schema, protocol

# Construct the file paths relative to the current working directory
schema1_path = os.path.join('avro','files','schema-1.avsc')
schema2_path = os.path.join('avro','files','schema-2.avsc')

# Parse the schemas from the files
with open(schema1_path, 'r') as file1, open(schema2_path, 'r') as file2:
    schema1 = schema.parse(file1.read())
    schema2 = schema.parse(file2.read())

# Compare the fields in the schemas
for field1, field2 in zip(schema1.fields, schema2.fields):
    if field1.name != field2.name:
        print(f"Field names do not match: {field1.name} vs. {field2.name}")
    elif field1.type != field2.type:
        print(f"Data type changed for field {field1.name}: {field1.type} vs. {field2.type}")
