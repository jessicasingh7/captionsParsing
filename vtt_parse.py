import webvtt
from collections import defaultdict

file_name = "1_1x0b27pk-en_US.vtt"


#Class Transcribe caption files
vtt = webvtt.read("1_1x0b27pk-en_US.vtt")
dictionary = defaultdict(int)
for line in vtt:
    for words in line.text.split():
        dictionary[words] += 1

print(list(sorted(dictionary.items(), key = lambda x: x[1], reverse = True))[:5])

#Now comparing with DRES
# os.system("cd ExpertCaptioner-Captions")

os.chdir("ExpertCaptioner-Captions")

search = "ls " + str(file_name.split('-')[0]) + "-*meta.json"
print(search)

cands = os.popen(search).readlines()

for cand in cands:
    cand = cand.strip()
    with open(cand) as json_file:
        content = json.load(json_file)
        if content["displayOnPlayer"]:
            end = content["mediaId"]
            break
