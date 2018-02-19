#from gensim.models import KeyedVectors
import warnings
warnings.filterwarnings(action="ignore", category=UserWarning, module='gensim')

import gensim


model =  gensim.models.KeyedVectors.load_word2vec_format('D:/dl4j-files/GoogleNews-vectors-negative300.bin/GoogleNews-vectors-negative300.bin', binary=True)

#print(model["Germany"])
#print(model["Berlin"])

#Vec = model["Santa_Claus"]




#vec = model.similar_by_vector('Berlin', topn=10, restrict_vocab=None)
#print(vec)

#result = model.most_similar(positive=['Germany', 'Paris'], negative=['Berlin'], topn=1)
#print(result)

#result1 = model.most_similar(positive=['woman', 'king'], negative=['man'])
#print(result1)

#result3 = model.most_similar(positive=['woman'], negative=['man'], topn=2 )
#print(result3)
#result3 = model.most_similar(positive=['Berlin'], negative=['Germany'], topn=5 )
#print(result3)

result4 = model.most_similar(positive=['Republican', 'Narendra_Modi'], negative=['Donald_Trump'], topn=3)
print(result4)

#result2 = model.most_similar(positive=['Michelle_Obama', 'Caramuru'], negative=['Barack_Obama'], topn=1)
#print(result2)


