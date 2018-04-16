import linecache
import random
import sys


# number of line to get.
LINES_GET = 73
fout = open("../Results/Main_Word2Vec_Capital_Random.txt", 'w', encoding="utf-8")
# Get number of line in the file.
with open('../Data/Capital_Train.txt') as fin:
    number_of_lines = len(fin.readlines())

if LINES_GET > number_of_lines:
     print ("Are you out of your mind!!!!")
     sys.exit(1)

# Choose a random number of a line from the file.
for i in random.sample(range(1,  number_of_lines+1), LINES_GET):
    #print("1st random number")
    #fout.write("1st random number:\n\n")
    fout.write(linecache.getline('../Data/Capital_Train.txt', i))

linecache.clearcache()