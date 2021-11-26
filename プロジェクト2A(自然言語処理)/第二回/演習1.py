import MeCab as me
m=me.Tagger("-Ochasen")    #あとで使う
ex="abcdefg"
print(ex[1:4])    #1番目から4番目まで
print(ex[:4])      #0～4まで
print(ex[3:])      #3~最後
print(ex[::-2])   #端っこから
print(ex[::2])    #最初から最後まで2つおきに
print(ex[1:5:2])   #1~4まで2つおきに



#ここから演習1
print(ex[::-1])
