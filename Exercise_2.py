#from gensim.models import KeyedVectors
import warnings
warnings.filterwarnings(action="ignore", category=UserWarning, module='gensim')

import gensim

#filename = 'raw_sentences.txt'
model =  gensim.models.KeyedVectors.load_word2vec_format('D:/dl4j-files/GoogleNews-vectors-negative300.bin/GoogleNews-vectors-negative300.bin', binary=True)

#print(model["Germany"])
#result = model.similarity('woman', 'man')
#print(result)

#result2 = model.most_similar(['Germany'], topn=3)
#print(result2)

#result1 = model.most_similar(positive=['Canada', 'Berlin'], negative=['Germany'], topn=2)
#print(result1)


vec = model.similar_by_vector('woman', topn=10, restrict_vocab=None)
print(vec)
#result1 = model.most_similar(positive=['woman', 'king'], negative=['man'])
#print(result1)
#word = model.similar_by_word(woman, topn=10, restrict_vocab=None)
#print(word)