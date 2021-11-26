import MeCab
#MeCabファイルの作成
def make_mecab_file(input_file_name,output_file_name):
    m=MeCab.Tagger()
    with open(input_file_name,encoding="UTF-8") as input_file:
        with open(output_file_name,mode="w",encoding="UTF-8") as output_file:
            output_file.write(m.parse(input_file.read()))

make_mecab_file("2020.txt","2020.text.mecab")
