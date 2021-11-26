from collections import Counter
import urllib3
from bs4 import BeautifulSoup
import lxml
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
def make_lines():
    with open("2020.txt.mecab",mode="r")as f:
        morphemes=[]
        for line in f:
            cols=line.split("\t")
            if len(cols)<2:
                return
            res_cols=cols[1].split(",")

            morpheme={
                "surface":cols[0],
                "base":res_cols[6],
                "pos":res_cols[0],
                "pos1":res_cols[1]
            }
            morphemes.append(morpheme)

            if res_cols[1]=="句点":
                yield morphemes
                morphemes=[]
def stop():
    slothlib="http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt"
    http=urllib3.PoolManager()
    slothlib_file=http.request("GET",slothlib)
    soup=BeautifulSoup(slothlib_file.data,"lxml")
    mydict=['いる','安倍','内閣','総理','大臣','ところ','おり','ない','あり','ある','いく','なっ','する','あっ']
    soup.extend(mydict)
    return soup
word=Counter()
stop_word=stop()
for line in make_lines():
    for morpheme in line:
        if morpheme["pos"]=="名詞":
            if len(morpheme["surface"])>2:
                if not morpheme["surface"] in stop_word:
                    word.update([morpheme["surface"]])

size=30
list_word=word.most_common(size)
print(list_word)

list_zipped=list(zip(list_word))
words=list_zipped[0]
counts=list_zipped[1]

fp=FontProperties(fname='/usr/share/fonts/truetype/takao-gothic/TakaoGothic.ttf')
plt.bar(
    1,
    size,
    counts,
    linewidth=1
)

plt.xticks(
    0,
    size,
    words,
    fontproperties=fp
)

plt.xlim(
    xmin=-1,xmax=size
)

plt.title(
    "TOP30",
    fontproperties=fp
)
plt.xlabel(
    "出現頻度が高い30語",
    fontproperties=fp
)
plt.ylabel(
    "出現頻度",
    fontproperties=fp
)
plt.grid(axis="y")
plt.show()
