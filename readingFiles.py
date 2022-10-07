import json
<<<<<<< HEAD
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
=======
with open("testFiles/0_247k9qz7-0_34d7z15g-meta.json") as json_file:
    metadata = json.load(json_file)
    print(metadata)
>>>>>>> cb6c151 (vtt parsing)
