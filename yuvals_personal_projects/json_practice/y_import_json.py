import json

with open("data_to_load2.json", "r") as load_file:
    data_from_json2 = json.load(load_file)

print(data_from_json2["total"])

for item in data_from_json2["data"]:
    print("||" + item["email"], end=" ||\n")