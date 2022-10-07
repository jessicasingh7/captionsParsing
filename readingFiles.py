import json
import os

path = "testFiles/"
files = os.listdir(path)

print(files)

captionsBeingDisplayed = ""

for file in files:
    with open(path+file) as json_file:
        metadata = json.load(json_file)
        if metadata["displayOnPlayer"] == True:
            captionsBeingDisplayed = file

captionsBeingDisplayed = captionsBeingDisplayed.replace("meta", "captions")     
print(captionsBeingDisplayed)