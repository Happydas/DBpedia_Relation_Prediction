from random import shuffle
import random

fin = open("../Data/Country_Currency_filtered.txt", 'r')
Train = open("../Data/Currency_Train.txt", 'w+')
Test = open("../Data/Currency_Test.txt", 'w+')
for line in fin:
    r = random.random()
    if r < 0.50:
        Train.write(line)
    else:
        Test.write(line)
fin.close()
Train.close()
Test.close()