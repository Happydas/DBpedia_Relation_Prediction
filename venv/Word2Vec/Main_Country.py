import warnings

warnings.filterwarnings(action="ignore", category=UserWarning, module='gensim')
import random
import gensim, re
import numpy as np

#warnings.filterwarnings(action="ignore", category=UserWarning, module='gensim')

f2 = open("../Results/Main_Word2Vec_Capital.txt", "w+", encoding="utf-8")
f3 = open("../Results/Main_Word2Vec_Capital_11.txt", "w+", encoding="utf-8")

f4 = open("../Results/Main_Word2Vec_Capital_Counter.txt_2", "a", encoding="utf-8")
vec = gensim.models.KeyedVectors.load_word2vec_format(
    'D:/dl4j-files/GoogleNews-vectors-negative300.bin/GoogleNews-vectors-negative300.bin', binary=True)

train  = open("../Data/Capital_Train.txt", 'r', encoding="utf-8")
test = open("../Data/Capital_Test.txt", 'r', encoding="utf-8")

train_lines = train.readlines()
test_lines = test.readlines()


def createSuperVectorAdditive(number):
    counter = 0
    city, country = np.zeros(300), np.zeros(300)
    while counter < number:
        counter += 1
        line = random.choice(train_lines).split()
        country += vec[line[0]]
        city += vec[line[1]]
    return city, country


def createSuperVectorAverage(number):
    counter = 0
    city_arr, country_arr = [], []
    while counter < number:
        counter += 1
        line = random.choice(train_lines).split()
        country_arr.append(vec[line[0]])
        city_arr.append(vec[line[1]])
    city = np.average(city_arr, axis=0)
    country = np.average(country_arr, axis=0)
    return city, country


def createSuperVectorMean(number):
    counter = 0
    city_arr = []
    country_arr = []
    while counter < number:
        counter += 1
        line = random.choice(train_lines).split()
        country_arr.append(vec[line[0]])
        city_arr.append(vec[line[1]])
    city = np.mean(city_arr, axis=0)
    country = np.mean(country_arr, axis=0)
    return city, country


i = 0
line_number = sum(1 for line in open('../Data/Capital_Test.txt'))

while i < 50:
    i += 1
    counter = 0
    cum_accuracy = 0

    while counter < 10:
        counter += 1
        corr_result = 0

        city_super, country_super = createSuperVectorAverage(i)

        #country = country_super
        #city = city_super


        for line in test_lines:
                Type_Test = line.split()
                if len(Type_Test) > 1:
                    # TargetVector = SuperVector + vec[Type[0]]
                    Super_Vector = vec[Type_Test[1]] + country
                    Result = vec.similar_by_vector((Super_Vector - city), topn=3)
                    # print(Result[0][0])
                    if Result[0][0] == Type_Test[1]:
                        Final_Result = Result[1][0]
                    elif Result[0][0] == Type_Test[0]:
                        Final_Result = Result[0][0]
                    # elif Result[1][0] == Type_Test[0]:
                    # Final_Result = Result[1][0]
                    elif Result[2][0] == Type_Test[0]:
                        Final_Result = Result[2][0]
                    else:
                        Final_Result = Result[0][0]

                    if Final_Result == Type_Test[0]:
                        corr_result+= 1
                    print(Final_Result)
print(corr_result)
            # get test data
            # create super vector
            # check whether result of analogy is in one of the topn=3 results
            # get number of correct results over whole test set

        #This variable adds together the individual accuracies for each run over the test set
cum_accuracy += corr_result/line_number

    #This is the average accuracy for all 10 test runs for one specific supervector version
    #(e.g. 1 vector in the super_vector, 2 vectors in the super_vector, etc. )
#print("Average Accuracy ", i, ": ", cummulative_result/10)

