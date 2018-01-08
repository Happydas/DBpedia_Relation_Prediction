#from gensim.models import KeyedVectors
import warnings
warnings.filterwarnings(action="ignore", category=UserWarning, module='gensim')

import gensim


model =  gensim.models.KeyedVectors.load_word2vec_format('D:/dl4j-files/GoogleNews-vectors-negative300.bin/GoogleNews-vectors-negative300.bin', binary=True)

#print(model["South_Africa"])


result = model.most_similar(positive=['Germany', 'France'], negative=['Berlin'], topn=1)
print(result)

#result1 = model.most_similar(positive=['woman', 'king'], negative=['man'])
#print(result1)

#result2 = model.most_similar(positive=['South_Africa', 'Berlin'], negative=['Germany'], topn=2)
#print(result2)

#vec = model.similar_by_vector(vector, topn=10, restrict_vocab=None)
#word = model.similar_by_word(word, topn=10, restrict_vocab=None)