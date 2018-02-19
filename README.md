Abstract
Vector representation of words has been learned by word2vec and
useful in many natural language processing and information retrieval.
Though, surprising fact is that word2vec have not been applied for
Dbpedia data. In this paper, I am focusing on how word2vec can
be applied for Dbpedia properties in order to get missing informa-
tion. The main goals of Extracting Vector Representation of Dbpedia
Properties are to nd corresponding resources from the Dbpedia and
to apply Word2Vec technique to nd missing information.
1 Introduction
1.1 Background
Word2vec is a neural network, which takes text corpus as input and produces
a set of vectors as a result. In the beginning word2vec build a vocabulary from
a large text corpus and then produces group of vectors. It rst constructs a
vocabulary from the training text data and then learns vector representation
of words. There are two ways to represent word2vec model architecture 1.
continuous bag-of-words (predicts a missing word given a window of context
words or word sequence) and 2. skip-gram ( predict the neighboring window
of target context by using a word) These word2vec model architecture used
in machine learning areas, natural language processing and advance research
areas. [1].
Continuous bag-of-words (CBOW) and continuous skip-gram model ar-
chitecture are very popular nowadays in the machine learning areas and fur-
ther research. Another depiction of words is dense vector came to know by
word2vec. Dense vector have exceptionally been displayed to demonstrate
same sense and it is benecent in the immense range from data analytics to
natural language processing.
As an example, words that have equivalent explanation will have analo-
gous vectors because of cosine similarity and the words whose doesn't have
equivalent explanation will have unalike vectors. It is quite surprising that,
word vectors follow the likeness rule. For instance, presume the likeness
"Berlin is to Germany as Paris is to France". It gives us the result like
following
vGermany 􀀀 vBerlin + vParis = vFrance
1
where vGermany; vBerlin; vParisandvFrance are the word vectors for Germany,
Berlin, Paris, and France respectively. [2].
1.2 Project Description
This project is focused on the Extracting Vector Representation of DBPe-
dia Properties from word2vec. Word2Vec has been applied in several areas
with the purpose of detect similarity and to nd out nearest word. However,
Word2Vec has not been applied for DBPedia properties. The main goal of
this project is to introduce techniques that can be used for learning DBPe-
dia data and to nd out corresponding missing information from DBPedia.
DBpedia ("DB" stand for "database") is a crowd-sourced community eort
to extract structured information from Wikipedia and make this information
available on the Web [dened by http://wiki.dbpedia.org/about].
If the user has two sentences like-
1. Berlin is the capital
2. Paris is the capital.
The result of the Word2vec similarity will be the words ending up near to
one another. Suppose, if we train a model with (input:Berlin,output:Capital)
and (input:Paris,output:Capital) this will eventually give insight the model
to understand that, Berlin and Paris both as connected to capital, thus Berlin
and Paris closely in the Word2Vec similarity.
The Extracting Vector Representation of DBPedia Properties from word2vec
is developed in python which takes DBPedia properties as input and returns
nearest or similar missing information as output.                         
