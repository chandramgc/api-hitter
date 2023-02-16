import json
from avro import schema
import os

# Define the Avro schema
avro_schema = schema.parse('''
    {
        "type": "record",
        "name": "User",
        "namespace": "com.example",
        "fields": [
            {"name": "name", "type": "string"},
            {"name": "age", "type": "string"},
            {"name": "email", "type": ["null", "string"], "default": null},
            {"name": "address", "type": {
                "type": "record",
                "name": "Address",
                "fields": [
                    {"name": "street", "type": "string"},
                    {"name": "city", "type": "string"},
                    {"name": "state", "type": "string"},
                    {"name": "zip", "type": "int"}
                ]
            }}
        ]
    }
''')

# Construct the file paths relative to the current working directory
user_path = os.path.join('avro','files','schema-2.avsc')


# Write the Avro schema to a file in the Avro JSON format
with open(user_path, 'w') as file:
    json.dump(avro_schema.to_json(), file, indent=2)
