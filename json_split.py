import json
import os

# Path to the JSON file
json_file_path = "./products_ga.json"

# Directory to write the JSON documents to
output_dir = "./ga-data/"

# Open the JSON file and parse the JSON
with open(json_file_path, "r") as json_file:
    json_data = json.load(json_file)

# Iterate over the JSON documents
for i, json_doc in enumerate(json_data):
    # Create a filename for the output file
    filename = f"json_doc_{i}.json"
    # Create the full path for the output file
    output_path = os.path.join(output_dir, filename)
    # Write the JSON document to the output file
    with open(output_path, "w") as output_file:
        json.dump(json_doc, output_file)
