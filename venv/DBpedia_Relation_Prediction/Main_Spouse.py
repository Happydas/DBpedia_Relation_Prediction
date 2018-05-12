import warnings

warnings.filterwarnings(action="ignore", category=UserWarning, module='gensim')
import random
import gensim, re
import numpy as np

#warnings.filterwarnings(action="ignore", category=UserWarning, module='gensim')

f2 = open("../Results/Main_Spouse.txt", "w+", encoding="utf-8")
f3 = open("../Results/Main_Spouse_Final.txt", "w+", encoding="utf-8")

f4 = open("../Results/Main_Spouse_Accuracy.txt", "w", encoding="utf-8")
f5 = open("../Results/Main_Spouse_Average_Accuracy.txt", "w+", encoding="utf-8")
vec = gensim.models.KeyedVectors.load_word2vec_format(
    'D:/dl4j-files/GoogleNews-vectors-negative300.bin/GoogleNews-vectors-negative300.bin', binary=True)


train  = open("../Data/Spouse_Train.txt", 'r', encoding="utf-8")
test = open("../Data/Spouse_Test.txt", 'r', encoding="utf-8")

train_lines = train.readlines()
test_lines = test.readlines()

def createSuperVector(number):
    counter = 0
    f_spouse_arr, m_spouse_arr = [], []
    while counter < number:
        counter += 1
        line = random.choice(train_lines).split()
        m_spouse_arr.append(vec[line[0]])
        f_spouse_arr.append(vec[line[1]])
    f_spouse = np.average(f_spouse_arr, axis=0)
    m_spouse = np.average(m_spouse_arr, axis=0)
    return f_spouse, m_spouse


i = 0
line_number = sum(1 for line in open('../Data/Spouse_Test.txt'))
print(line_number)

while i < 20:
    i += 1
    counter = 0
    accuracy = 0

    while counter < 10:
        counter += 1
        correct_result = 0

        f_spouse_super, m_spouse_super = createSuperVector(i)

        for line in test_lines:
                Data_Test = line.split()
                if len(Data_Test) > 1:
                    Super_Vector = vec[Data_Test[1]] + m_spouse_super
                    Result = vec.similar_by_vector((Super_Vector - f_spouse_super), topn=3)
                    if Result[1][0] == Data_Test[0]:
                         Final_Result = Result[1][0]
                    elif Result[2][0] == Data_Test[0]:
                        Final_Result = Result[2][0]
                    else:
                        Final_Result = Result[0][0]
                    if Final_Result == Data_Test[0]:
                        correct_result+= 1
                    f2.write(str(Result) + " " + Data_Test[0] + "\n")
                    f3.write(str(Final_Result) + " " + Data_Test[0] + "\n")
        print(correct_result)
        accuracy += correct_result / line_number
        print(accuracy)
        f4.write(str(correct_result) + " " + (str(accuracy)) + "\n")
    Avg_Accuracy = (accuracy / 10)
    print("Average Accuracy for Average ", i, ": ", Avg_Accuracy)
    f5.write(str(i) + " " + (str(Avg_Accuracy)) + "\n")