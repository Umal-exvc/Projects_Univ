from collections import Counter
import urllib3
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
import MeCab
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
copus1,copus2=[],[]

w=Counter()
def make_lines1():
    with open("前半.txt.mecab",mode="r")as f:
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

def make_lines2():
    with open("後半.txt.mecab",mode="r")as f:
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


for line in make_lines1():
    for morpheme in line:
        if morpheme["pos"]=="名詞":
            if len(morpheme["surface"])>2:
                w.update([morpheme["surface"]])
                copus1.append(morpheme["surface"])
                copus1.append(" ")
a="".join(copus1)

for line in make_lines2():
    for morpheme in line:
        if morpheme["pos"]=="名詞":
            if len(morpheme["surface"])>2:
                w.update([morpheme["surface"]])
                copus2.append(morpheme["surface"])
                copus2.append(" ")
b="".join(copus2)

count=CountVectorizer()
docs=np.array([a,b])
bag=count.fit_transform(docs)

print(count.vocabulary_)

print(bag.toarray())

tfidf=TfidfTransformer(use_idf=True,norm="l2",smooth_idf=True)
np.set_printoptions(precision=2)

features=count.get_feature_names()
result=tfidf.fit_transform(count.fit_transform(docs))
result_arr=tfidf.fit_transform(count.fit_transform(docs)).toarray()

data={
    "index":features,
    "num1":result_arr[0],
    "num2":result_arr[1]
}
df=pd.DataFrame(data)
df.to_excel("出力結果.xlsx",sheet_name="半年のデータ")