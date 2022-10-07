import webvtt
import datetime
import json
import os
from collections import defaultdict

file_name = "1_1x0b27pk-en_US.vtt"


#Class Transcribe caption files
vtt = webvtt.read("1_1x0b27pk-en_US.vtt")
dictionary = defaultdict(int)
f = open("CT.txt", "w")
for line in vtt:
    f.write(line.text)
    f.write("\n")
    f.write(line.start)
    f.write("\n")
    f.write(line.end)
    f.write("\n")
    # print(line.text)
    # print(line.start)
    # print(line.end)
    for words in line.text.split():
        dictionary[words] += 1
f.close()
#print(list(sorted(dictionary.items(), key = lambda x: x[1], reverse = True))[:5])

#Now comparing with DRES

os.chdir("ExpertCaptioner-Captions")
search = "ls " + str(file_name.split('-')[0]) + "-*meta.json"
#print(search)

cands = os.popen(search).readlines()

for cand in cands:
    cand = cand.strip()
    with open(cand) as json_file:
        content = json.load(json_file)
        if content["displayOnPlayer"]:
            print(content)
            suffix = content["captionId"]
            break
active_file = file_name.split('-')[0] + "-" + suffix + "-captions.json"

f = open("../DRES.txt", "w")
with open(active_file) as json_file:
    content = json.load(json_file)
content = list(content["objects"])
def convert_to_datetime(x):
    datetime.datetime.fromtimestamp(x/1000.0)
for lines in content:
    if("content" in lines):
        # print(lines["content"][0]["text"])
        # print(lines["startTime"])
        # print(lines["endTime"])
        f.write(lines["content"][0]["text"])
        f.write("\n")
        f.write(str(lines["startTime"]))
        f.write("\n")
        f.write(str(lines["endTime"]))
        f.write("\n")
f.close()
print("done")