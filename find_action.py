import os
import json

directory_path = "E:/ZewailCity/Grad Proj/Uefa Champions league/2014-2015"  # Replace with the path to the directory containing the JSON files
# Replace with the path to the directory containing the JSON files


def search_directory_for_keyword(directory_path, keyword):
    matching_file_paths = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file == "Labels-v2.json":
                file_path = os.path.join(root, file)
                with open(file_path, "r") as json_file:
                    data = json.load(json_file)
                    for annotation in data["annotations"]:
                        if keyword in annotation["label"]:
                            matching_file_paths.append(file_path)
    return matching_file_paths

# Example usage: search for all files containing the keyword "Kick-off"
result = search_directory_for_keyword(directory_path, "Penalty")
if result:
    print("Keyword found in the following files:")
    for file_path in result:
        print(file_path)
else:
    print("Keyword not found in any JSON file.")
