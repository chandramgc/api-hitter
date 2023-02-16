from avro.datafile import DataFileReader
from avro.io import DatumReader
from avro.schema import parse

# Path to the Avro file
avro_file_path = 'example.avro'

# Open the Avro file for reading
with open(avro_file_path, 'rb') as avro_file:
    # Create a DataFileReader object
    reader = DataFileReader(avro_file, DatumReader())

    # Get the schema of the Avro file
    schema_str = reader.meta.get('avro.schema')

    # Parse the schema string into a schema object
    schema = parse(schema_str)

    # Convert the schema to a string
    schema_str = str(schema)

    # Print the schema
    print(schema_str)

    # Close the DataFileReader
    reader.close()

