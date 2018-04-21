import warnings

warnings.filterwarnings(action="ignore", category=UserWarning, module='gensim')
import random
import gensim, re
import numpy as np

#warnings.filterwarnings(action="ignore", category=UserWarning, module='gensim')

f2 = open("../Results/Main_Capital.txt", "w+", encoding="utf-8")
f3 = open("../Results/Main_Capital_Final.txt", "w+", encoding="utf-8")

f4 = open("../Results/Main_Capital_Counter.txt", "a", encoding="utf-8")
f5 = open("../Results/Main_Capital_11.txt", "w+", encoding="utf-8")
vec = gensim.models.KeyedVectors.load_word2vec_format(
    'D:/dl4j-files/GoogleNews-vectors-negative300.bin/GoogleNews-vectors-negative300.bin', binary=True)

f6 = open("../Results/Main_Capital_Average.txt", "w+", encoding="utf-8")
f7 = open("../Results/Main_Capital_Final_Average.txt", "w+", encoding="utf-8")

f8 = open("../Results/Main_Capital_Counter_Average.txt", "a", encoding="utf-8")
f9 = open("../Results/Main_Capital_11_Average.txt", "w+", encoding="utf-8")

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


i = 0
line_number = sum(1 for line in open('Capital_Test.txt'))

while i < 20:
    i += 1
    counter = 0
    cum_accuracy = 0
    accuracy = 0

    while counter < 10:
        counter += 1
        corr_result = 0
        correct_result = 0

        city_super, country_super = createSuperVectorAdditive(i)
        city_average_super, country_average_super = createSuperVectorAverage(i)

        for line in test_lines:
                Data_Test = line.split()
                if len(Data_Test) > 1:
                    Super_Vector = vec[Data_Test[1]] + country_super
                    Result = vec.similar_by_vector((Super_Vector - city_super), topn=3)
                    # print(Result[0][0])
                    if Result[0][0] == Data_Test[1]:
                        Final_Result = Result[1][0]
                    elif Result[1][0] == Data_Test[0]:
                         Final_Result = Result[1][0]
                    elif Result[2][0] == Data_Test[0]:
                        Final_Result = Result[2][0]
                    else:
                        Final_Result = Result[0][0]

                    if Final_Result == Data_Test[0]:
                        corr_result+= 1
                    f2.write(str(Result) + " " + Data_Test[1] + "\n")
                    f3.write(str(Final_Result) + " " + Data_Test[1] + "\n")


        for line in test_lines:
                Data_Test = line.split()
                if len(Data_Test) > 1:
                    Super_Vector_Average = vec[Data_Test[1]] + country_average_super
                    Result_Average = vec.similar_by_vector((Super_Vector_Average - city_average_super), topn=3)
                    if Result_Average[0][0] == Data_Test[1]:
                        Final_Result_Average = Result_Average[1][0]
                    elif Result_Average[1][0] == Data_Test[0]:
                        Final_Result_Average = Result_Average[1][0]
                    elif Result_Average[2][0] == Data_Test[0]:
                        Final_Result_Average = Result_Average[2][0]
                    else:
                        Final_Result_Average = Result_Average[0][0]

                    if Final_Result_Average == Data_Test[0]:
                        correct_result+= 1
                    f6.write(str(Result_Average) + " " + Data_Test[1] + "\n")
                    f7.write(str(Final_Result_Average) + " " + Data_Test[1] + "\n")

        print(corr_result)
        cum_accuracy += corr_result/line_number
        print(cum_accuracy)
        f5.write((str(cum_accuracy)) + "\n")
        print(correct_result)
        accuracy += correct_result / line_number
        print(accuracy)
        f9.write((str(accuracy)) + "\n")

    Average_Accuracy = (cum_accuracy/10)
    print("Average Accuracy for Additive", i, ": ", Average_Accuracy)
    f4.write(str(i) + " " + (str(Average_Accuracy)) + "\n")
    Avg_Accuracy = (accuracy/10)
    print("Average Accuracy for Average ", i, ": ", Avg_Accuracy)
    f8.write(str(i) + " " + (str(Avg_Accuracy)) + "\n")
