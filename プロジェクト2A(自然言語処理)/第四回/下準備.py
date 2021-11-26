with open("neko.text.mecab",mode="r",encoding="UTF-8")as text:
    for line in text:
        if line=="名詞":
            print(line)
