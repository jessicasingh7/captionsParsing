import webvtt

for caption in webvtt.read('1_1x0b27pk-en_US.vtt'):
    print(caption.start)
    print(caption.end)
    print(caption.text)