from gensim.models import KeyedVectors
# you can get GoogleNews-vectors-negative300.bin from https://docs.google.com/open?id=0B7XkCwpI5KDYNlNUTTlSS21pQmM

# Load the pre-trained Google News model
model_path = 'GoogleNews-vectors-negative300.bin'
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

# Find the words most similar to the given query
similars = model.most_similar(positive=['king', 'woman'], negative=['man'], topn=10)

# Print the results
for similar in similars:
    print(similar[0], similar[1])