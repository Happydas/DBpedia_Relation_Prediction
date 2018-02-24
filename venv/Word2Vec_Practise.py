#from gensim.models import KeyedVectors
import warnings
warnings.filterwarnings(action="ignore", category=UserWarning, module='gensim')

import gensim


model =  gensim.models.KeyedVectors.load_word2vec_format('D:/dl4j-files/GoogleNews-vectors-negative300.bin/GoogleNews-vectors-negative300.bin', binary=True)

#print(model["Germany"])

#vec = model.similar_by_vector('Berlin', topn=10, restrict_vocab=None)
#print(vec)


#vocabword = sort_vocab()
#print(vocabword)

#vocabw = model.vocab["Germany"].count
#print(vocabw)

#print('vocab:', model.vocab.keys())

# to get the total word
#print(len(model.vocab))


if 'word' in model.vocab:
    size = 300  # word vector size
    word = 'Aaron_Spelling'  # word token

    try:
        wordVector = model[word].reshape((1, size))
        print("Word found! ", word)
    except KeyError:
        print("Word not found! ", word)


