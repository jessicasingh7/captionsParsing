import webvtt
from collections import defaultdict

vtt = webvtt.read("1_1x0b27pk-en_US.vtt")
dictionary = defaultdict(int)
for line in vtt:
    # print(line.start)
    # print(line.end)
    # print(line.text)
    for words in line.text.split():
        dictionary[words] += 1
        
print(list(sorted(dictionary.items(), key = lambda x: x[1], reverse = True))[:5])