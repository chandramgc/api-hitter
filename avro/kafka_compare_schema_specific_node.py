import os
import json
from collections import deque
from avro.schema import parse

def compare_schemas(schema1, schema2, path=""):
    # Convert the schemas to dicts
    schema_dict1 = json.loads(str(schema1))
    schema_dict2 = json.loads(str(schema2))

    # Initialize a queue to traverse the schema recursively
    queue = deque([("", schema_dict1, schema_dict2)])

    # Initialize lists to store the fields that have changed
    changed_fields = []
    deleted_fields = []
    added_fields = []

    # Traverse the schema recursively
    while queue:
        path, field1, field2 = queue.popleft()

        # Check if the field is present in both schemas
        if field1["name"] == field2["name"]:
            # Check if the field types are the same
            if field1["type"] != field2["type"]:
                changed_fields.append(path + field1["name"])
            
            # Recurse on child fields
            if "fields" in field1 and "fields" in field2:
                for child1, child2 in zip(field1["fields"], field2["fields"]):
                    queue.append((path + field1["name"] + ".", child1, child2))
            elif "fields" in field1:
                for child1 in field1["fields"]:
                    deleted_fields.append(path + field1["name"] + "." + child1["name"])
            elif "fields" in field2:
                for child2 in field2["fields"]:
                    added_fields.append(path + field2["name"] + "." + child2["name"])
        else:
            # This field has been deleted or added
            if path == "":
                # The field is at the top level
                if field1["name"] in schema_dict1:
                    deleted_fields.append(field1["name"])
                else:
                    added_fields.append(field2["name"])
            else:
                # The field is nested
                if field1["name"] in schema_dict1[path[:-1]]["fields"]:
                    deleted_fields.append(path + field1["name"])
                else:
                    added_fields.append(path + field2["name"])

    # Return the changed, deleted, and added fields
    return changed_fields, deleted_fields, added_fields

# Construct the file paths relative to the current working directory
schema1_path = os.path.join('avro','files','schema-1.avsc')
schema2_path = os.path.join('avro','files','schema-2.avsc')

# Load the Avro JSON schemas
with open(schema1_path, "r") as f:
    schema1 = parse(f.read())

with open(schema2_path, "r") as f:
    schema2 = parse(f.read())

# Compare the schemas and print the results
changed, deleted, added = compare_schemas(schema1, schema2)
print("Changed fields:", changed)
print("Deleted fields:", deleted)
print("Added fields:", added)
