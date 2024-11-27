from gensim.models import KeyedVectors
# you can get GoogleNews-vectors-negative300.bin from https://docs.google.com/open?id=0B7XkCwpI5KDYNlNUTTlSS21pQmM

# Load the pre-trained Google News model
model_path = 'GoogleNews-vectors-negative300.bin'
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

# Calculate similarity between words
similarity1 = model.similarity('dog', 'cat')
print("Similarity between 'dog' and 'cat':", similarity1)

similarity2 = model.similarity('dog', 'tap')
print("Similarity between 'dog' and 'tap':", similarity2)
