#from gensim.models import KeyedVectors
import warnings
warnings.filterwarnings(action="ignore", category=UserWarning, module='gensim')

import gensim

#filename = 'raw_sentences.txt'
model =  gensim.models.KeyedVectors.load_word2vec_format('D:/dl4j-files/GoogleNews-vectors-negative300.bin/GoogleNews-vectors-negative300.bin', binary=True)

print(model["South_Africa"])
person1 = model["Santa_Claus"]
location1 = model["South_Pole"]
newVector = person1 - location1

#result = model.most_similar(positive=['day', 'program'], negative=['night'], topn=1)
#print(result)


#vec = model.similar_by_vector(vector, topn=10, restrict_vocab=None)
#word = model.similar_by_word(word, topn=10, restrict_vocab=None)