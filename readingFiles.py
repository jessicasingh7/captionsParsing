import json
import os
 
# Get the list of all files and directories
path = "testFiles/"
files = os.listdir(path)

print(files)

captionsBeingDisplayed = ""

for file in files:
    with open(path+file) as json_file:
        metadata = json.load(json_file)
        if metadata["displayOnPlayer"] == True:
            captionsBeingDisplayed = file
        
print(captionsBeingDisplayed)
