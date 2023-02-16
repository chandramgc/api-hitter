import json
import avro.schema
import os

# Construct the file paths relative to the current working directory
schema1_path = os.path.join('avro','files','schema-1.avsc')
schema2_path = os.path.join('avro','files','schema-2.avsc')

# Load the Avro schema files
with open(schema1_path, 'r') as f:
    schema1 = avro.schema.parse(json.load(f))
with open(schema2_path, 'r') as f:
    schema2 = avro.schema.parse(json.load(f))

# Compare the schemas for a specific field
field_name = 'address'
field_parts = field_name.split('.')
for part in field_parts:
    if isinstance(schema1, avro.schema.RecordSchema):
        for field in schema1.fields:
            if field.name == part:
                schema1 = field.type
                break
    if isinstance(schema2, avro.schema.RecordSchema):
        for field in schema2.fields:
            if field.name == part:
                schema2 = field.type
                break

if schema1.to_json() != schema2.to_json():
    print(f"Data type changed for field {field_name}")
