import re

with open("./neko.txt.mecab","r",encoding="utf-8") as fp:
    col=[]
    sent=[]
    Keys=["surface","base","pos","pos1"]
    for line in fp:
        Values=[]
        words=re.split("\t|,|\n",line)
        if words[0]=="EOS":
            if len(sent)>0:
                col.append(sent)
                sent=[]
            continue
        Values.append(words[0])
        Values.append(words[7])
        Values.append(words[1])
        Values.append(words[2])
        sent.append(dict(zip(Keys,Values)))

print(col)
