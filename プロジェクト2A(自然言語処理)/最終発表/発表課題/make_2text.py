import MeCab

def make_mecab(input_file,output_file):
    m=MeCab.Tagger()
    m.parse(" ")
    with open(input_file)as inp:
        with open(output_file,mode="w")as out:
            out.write(m.parse(inp.read()))

make_mecab("後半.txt","後半.txt.mecab")