import webvtt
import datetime
import json
import os
from collections import defaultdict

file_name = "1_1x0b27pk-en_US.vtt"


#Class Transcribe caption files
vtt = webvtt.read("1_1x0b27pk-en_US.vtt")
ct_dictionary = defaultdict(int)
ct_array = []
f = open("CT.txt", "w")
def conv_time(time):
    hour, minute, second = time.split(":")
    # print(hour, minute, second)
    hour = int(float(hour) * 3600 * 1000)
    minute = int(float(minute) * 60 * 1000)
    second = int(float(second) * 1000)
    # print(hour, minute, second)
    converted = second + minute + hour
    return str(float(converted) * 1000)

lineNumber = 0
for line in vtt:
    f.write(line.text)
    f.write("\n")
    f.write(conv_time(line.start))
    f.write("\n")
    f.write(conv_time(line.end))
    f.write("\n")

    ct_array.append((conv_time(line.start), conv_time(line.end), []))
    # print(line.text)
    # print(line.start)
    # print(line.end)

    for words in line.text.split():
        try: 
            ct_array[lineNumber][2].append(words)
            ct_dictionary[words] += 1
        except:
            KeyError("keyword error")
        lineNumber += 1
f.close()

# for item in ct_array:
#     print(item[0], item[1])
#     for word in item[2]:
#         print(word)
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
            # print(content)
            suffix = content["captionId"]
            break
active_file = file_name.split('-')[0] + "-" + suffix + "-captions.json"

f = open("../DRES.txt", "w")
with open(active_file) as json_file:
    content = json.load(json_file)
content = list(content["objects"])

dres_dictionary = defaultdict(int)
dres_array = []

lineNumber = 0
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
        dres_array.append((str(lines["startTime"]), str(lines["endTime"]), []))
        for words in lines["content"][0]["text"].split():
            try: 
                # print("added")
                dres_dictionary[words] += 1
                dres_array[lineNumber][2].append(words)
            except:
                KeyError("keyword error")
        lineNumber += 1
f.close()
# print("done")

# print(dres_dictionary)
# print(ct_dictionary)

def checkFreq():
    errors = 0
    for key, values in ct_dictionary.items():
        if key in dres_dictionary:
            # print("found")
            errors += abs(dres_dictionary[key] - ct_dictionary[key])
        else:
            # print("not found")
            errors += ct_dictionary[key]
    total_words = sum(ct_dictionary.values())
    return errors / total_words

print(dres_dictionary)
print(ct_dictionary)
# def checkFreq():
#     for key, values in ct_dictionary.items():
#         if key 
