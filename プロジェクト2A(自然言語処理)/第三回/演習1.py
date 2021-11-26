import json
import re                                                    #encoding="UTF-8"をつけよう 
with open(r"jawiki-country.json",encoding="UTF-8") as f:    #Ω
    articals=f.readlines()                                                     #L J
    for con in articals:                                                         # π
        a_dic=json.loads(con)
        if a_dic["title"]=="イギリス":
            texts=a_dic["text"]
            


#--------------Ex3-5-----------
categories=[]
for c in texts.split("\n"):
    if "Category" in c:
        categories.append(c)


#------演習1------

categories2=[]
for c in texts.split("\n"):
    c_obj=re.search("^\[\[Category:(.*?)(|\|.*)\]\]?",c)
    if not(c_obj==None):
        categories2.append(c_obj.group(1))
print(categories2)



#------演習2------

for x in texts.split("\n"):
    x_obj=re.search("(File|ファイル):(\S*)\|",x)
    if not(x_obj==None):
        #print(x_obj.group(2))

#------演習3-------

for sec in text.split("\n"):
    sec_obj=re.search("^(##)\s*(.*?)\s*(##)$",sec)
    if not(sec_obj==None):
        print(sec_obj.group(2),len(sec_obj.group(1))-1)
