import gensim
from gensim.models import Word2Vec
import codecs

entrada=codecs.open("corpus-tok-spa.txt","r",encoding="utf-8")

data=[]

for linia in entrada:
    linia=linia.rstrip()
    tokens=linia.split(" ")
    data.append(tokens)
    
modelCBOW = gensim.models.Word2Vec(data, min_count = 10,vector_size = 300, window = 5)
modelCBOW.save("CBOWlarge.model")
modelCBOW.wv.save_word2vec_format("CBOWlarge.wordvectors", binary= False)
