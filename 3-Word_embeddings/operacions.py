from gensim.models import Word2Vec
model = Word2Vec.load("CBOWlarge.model")

similars=model.wv.most_similar(positive=['Madrid','Francia'],negative=['España'], topn=10)

for similar in similars:
    print(similar[0],similar[1])
