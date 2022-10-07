import json
with open("captionsParsing/testFiles/0_247k9qz7-0_34d7z15g-meta.json") as json_file:
    metadata = json.load(json_file)
    print(metadata)