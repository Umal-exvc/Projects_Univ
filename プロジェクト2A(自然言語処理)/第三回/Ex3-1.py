import re
content="hello python,123,end."
pattern="he"
#コンパイルしてからmatch
repatter=re.compile(pattern)
result=repatter.match(content)

print(result.group())



#-------------ここからEx3-2-------------#
#()で取りたい文字を
patt='.*?(\d+).*'
resul=re.match(patt,content)

if resul:    #matchした時のみ
    print(resul.group())    #group()で全文字をprint
    print(resul.group(1))  #123
    

#-------------ここからEx3-3-------------#

s="aaa@xxx.com,bbb@yyy.com,ccc@zzz.net"
m=re.search("[a-z]+@[a-z]+\.net",s)
print(m.group())
