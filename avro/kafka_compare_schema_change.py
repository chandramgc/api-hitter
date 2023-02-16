import json
from collections import deque
from avro.schema import parse
import os

def compare_schemas(schema1, schema2, path=""):
    # Convert the schemas to dicts
    schema_dict1 = json.loads(str(schema1))
    schema_dict2 = json.loads(str(schema2))

    # Initialize a queue to traverse the schema recursively
    queue = deque([("", schema_dict1, schema_dict2)])

    # Initialize a list to store the changed fields
    changed_fields = []

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
                    queue.append((path + field1["name"] + ".", child1, {"name": ""}))
            elif "fields" in field2:
                for child2 in field2["fields"]:
                    queue.append((path + field2["name"] + ".", {"name": ""}, child2))
        else:
            # This field has been deleted or added
            if path == "":
                # The field is at the top level
                if field1["name"] in schema_dict1:
                    queue.append((field1["name"] + ".", field1, {"name": ""}))
                else:
                    queue.append((field2["name"] + ".", {"name": ""}, field2))
            else:
                # The field is nested
                if field1["name"] in schema_dict1[path[:-1]]["fields"]:
                    queue.append((path + field1["name"] + ".", field1, {"name": ""}))
                else:
                    queue.append((path + field2["name"] + ".", {"name": ""}, field2))

    # Return the changed fields
    return changed_fields

# Construct the file paths relative to the current working directory
schema1_path = os.path.join('avro','files','schema-1.avsc')
schema2_path = os.path.join('avro','files','schema-2.avsc')

# Load the Avro JSON schemas
with open(schema1_path, "r") as f:
    schema1 = parse(f.read())

with open(schema2_path, "r") as f:
    schema2 = parse(f.read())

# Compare the schemas and print the results
changed = compare_schemas(schema1, schema2)
print("Changed fields:", changed)
