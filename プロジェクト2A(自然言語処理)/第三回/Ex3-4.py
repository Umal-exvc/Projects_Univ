import json
                                                                    #encoding="UTF-8"をつけよう 
with open(r"jawiki-country.json",encoding="UTF-8") as f:    #Ω
    articals=f.readlines()                                                     #L J
    for con in articals:                                                         # π
        a_dic=json.loads(con)
        if a_dic["title"]=="イギリス":
            texts=a_dic["text"]
            print(texts)


#--------------Ex3-5-----------
categories=[]
for c in texts.split("\n"):
    if "Category" in c:
        categories.append(c)
print(categories)
