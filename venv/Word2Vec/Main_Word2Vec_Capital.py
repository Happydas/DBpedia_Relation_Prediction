import warnings

warnings.filterwarnings(action="ignore", category=UserWarning, module='gensim')
import gensim, re
import numpy as np

f2 = open("../Results/Main_Word2Vec_Capital.txt", "w+", encoding="utf-8")
f3 = open("../Results/Main_Word2Vec_Capital_11.txt", "w+", encoding="utf-8")
f4 = open("../Results/Main_Word2Vec_Capital_Counter.txt", "a", encoding="utf-8")

vec = gensim.models.KeyedVectors.load_word2vec_format(
    'D:/dl4j-files/GoogleNews-vectors-negative300.bin/GoogleNews-vectors-negative300.bin', binary=True)

f = open("../Data/Capital_Train.txt", 'r', encoding="utf-8")
f1 = open("../Data/Capital_Test.txt", "r", encoding="utf-8")

'''
Super_Vector = vec["Kabul"] + vec["Rwanda"]
Target_Vector = vec.similar_by_vector((Super_Vector - vec["Kigali"]), topn=3)
print(Target_Vector)
'''
accuracy = 0
country = np.zeros(300)
City = np.zeros(300)
counter = 0
lines = f.readlines()
lines_1 = f1.readlines()
linesNew = []
# for line in lines.split('\n'):
for line in lines:
    counter += 1
    Type = line.split()
    #print(Type)
    #f2.write(Type)
    if len(Type) > 1:
        country = vec[Type[0]]
        City = vec[Type[1]]
        if counter == 1:
            break
for line_1 in lines_1:
    Type_Test = line_1.split()
    if len(Type_Test) > 1:
        #TargetVector = SuperVector + vec[Type[0]]
        Super_Vector =  vec[Type_Test[1]] + country
        Result = vec.similar_by_vector((Super_Vector - City), topn=3)
        #print(Result[0][0])
        if Result[0][0] == Type_Test[1]:
            Final_Result = Result[1][0]
        elif Result[0][0] == Type_Test[0]:
            Final_Result = Result[0][0]
        #elif Result[1][0] == Type_Test[0]:
           # Final_Result = Result[1][0]
        elif Result[2][0] == Type_Test[0]:
            Final_Result = Result[2][0]
        else:
            Final_Result = Result[0][0]

        if Final_Result ==Type_Test[0]:
             accuracy += 1
        print(Final_Result)
print(accuracy)

'''
        f2.write(str(Result)  + " "  + Type_Test[1] + "\n")
        f3.write(str(Final_Result) + " " + Type_Test[1] + "\n")
print(accuracy)
num_lines = sum(1 for line in open('../Data/Capital_Test.txt'))
print(num_lines)
Accuracy_Percentage = accuracy / num_lines
#Accuracy_Percentage = accuracy / len(f1.readlines())
print(Accuracy_Percentage)
#f4.write("Accuracy:" + " " + (str( Accuracy_Percentage)))
#+f5.write("Count:" + " " + (str( counter)) + "\n")
f4.write((str( Accuracy_Percentage)) + "   ")
f5.write((str( counter)) + "\n")
print(counter)
print("done")
'''


