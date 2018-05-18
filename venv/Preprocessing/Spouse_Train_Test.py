from random import shuffle
import random

f = open("../Data/Spouse_filtered.txt", 'r')
train = open("../Data/Spouse/Spouse_Train.txt", 'w+')
test = open("../Data/Spouse/Spouse_Test.txt", 'w+')
for line in f:
    r = random.random()
    if r < 0.50:
        train.write(line)
    else:
        test.write(line)
f.close()
train.close()
test.close()
