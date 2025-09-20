import json

# Need path to data file
file_path = 'iteration_02/assignments/day_01/json_intro/'

# --- Step 1: Load JSON data into a Python dictionary ---
with open(f"{file_path}school_data.json", "r") as file:
    data = json.load(file)  # json.load reads JSON into a dict

print(f"Data loaded from JSON file:\n{data}")
print(f"\nType of loaded data: {type(data)}")  # should be <class 'dict'>

# --- Step 2: Access and modify the dictionary ---
print(f"\nSemester: {data['semester']}")
print(f"First student name: {data['students'][0]['name']}")
print(f"Original grade in first course: {data['students'][0]['courses'][0]['grade']}")

# Update grade for first student's first course
data['students'][0]['courses'][0]['grade'] = "A+"
print(f"Updated grade: {data['students'][0]['courses'][0]['grade']}")

# --- Step 3: Write dictionary back to JSON file ---
with open(f"{file_path}school_data_updated.json", "w") as file:
    json.dump(data, file, indent=4)  # json.dump writes data dict to new JSON file with formatting indentation

print(f"\nUpdated data written to school_data_updated.json")

# --- Step 4: Demonstrate json.dumps and json.loads ---
# Convert dictionary to JSON string
json_string = json.dumps(data)
print(f"\nDictionary as JSON string (first 100 chars): {json_string[:100]} ...")

# Convert JSON string back to dictionary
dict_from_string = json.loads(json_string)
print(f"\nType after json.loads: {type(dict_from_string)}")
print(f"First student from loaded string: {dict_from_string['students'][0]['name']}")