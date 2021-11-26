'''import MeCab
def make_mecab_file(input_file_name, output_file_name):
    m = MeCab.Tagger()
    with open(input_file_name, encoding='utf-8') as input_file:
        with open(output_file_name, mode='w', encoding='utf-8') as output_file: output_file.write(m.parse(input_file.read()))

make_mecab_file("neko.txt", "neko.txt.mecab")'''

import re
with open("./neko.txt.mecab","r",encoding="utf-8") as fp:
    col=[]
    sent=[]
    Keys=["surface", "base", "pos", "pos1"]
    for line in fp:
        Values=[]
        words=re.split("\t|,|\n", line)
        if words[0]=="EOS":
            if sent:
                col.append(sent)
                sent=[]
            continue
        Values.append(words[0]) 
        Values.append(words[0])
        Values.append(words[7])
        Values.append(words[1])
        Values.append(words[2])
        sent.append(dict(zip(Keys,Values)))

print(col)
