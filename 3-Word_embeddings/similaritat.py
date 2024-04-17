from gensim.models import Word2Vec
model = Word2Vec.load("CBOW.model")
similaritat1=model.wv.similarity('perro', 'gato')
print("similaridad entre perro y gato:",similaritat1)
similaritat2=model.wv.similarity('perro', 'grifo')
print("similaridat entre perro y grifo:",similaritat2)
