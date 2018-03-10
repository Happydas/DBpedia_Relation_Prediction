import linecache
import random
import sys


# number of line to get.
LINES_GET = 1
fout = open("Capital_Random_TestData.txt", 'a', encoding="utf-8")
# Get number of line in the file.
with open('Capital_Test.txt') as fin:
    number_of_lines = len(fin.readlines())

if LINES_GET > number_of_lines:
     print ("Are you sick!!!!")
     sys.exit(1)

# Choose a random number of a line from the file.
for i in random.sample(range(1,  number_of_lines+1), LINES_GET):
    #print("1st random number")
    fout.write("1st random number:\n\n")
    fout.write(linecache.getline('Capital_Test.txt', i) + "\n")
    #print (linecache.getline('Capital_filtered.txt', i))

linecache.clearcache()



LINES_GET = 5
fout = open("Capital_Random_TestData.txt", 'a', encoding="utf-8")
# Get number of line in the file.
with open('Capital_Test.txt') as fin:
    number_of_lines = len(fin.readlines())

if LINES_GET > number_of_lines:
     print ("Are you sick!!!!")
     sys.exit(1)

# Choose a random number of a line from the file.
fout.write("5 random number:\n\n")
for i in random.sample(range(1,  number_of_lines+1), LINES_GET):
    fout.write(linecache.getline('Capital_Test.txt', i) + "\n")
    #print (linecache.getline('Capital_filtered.txt', i))

linecache.clearcache()


# to get 10
LINES_GET = 10
fout = open("Capital_Random_TestData.txt", 'a', encoding="utf-8")
# Get number of line in the file.
with open('Capital_Test.txt') as fin:
    number_of_lines = len(fin.readlines())

if LINES_GET > number_of_lines:
     print ("Are you sick!!!!")
     sys.exit(1)

# Choose a random number of a line from the file.
fout.write("10 random number:\n\n")
for i in random.sample(range(1,  number_of_lines+1), LINES_GET):
    fout.write(linecache.getline('Capital_Test.txt', i) + "\n")
    #print (linecache.getline('Capital_filtered.txt', i))

linecache.clearcache()

#To get 15
LINES_GET = 15
fout = open("Capital_Random_TestData.txt", 'a', encoding="utf-8")
# Get number of line in the file.
with open('Capital_Test.txt') as fin:
    number_of_lines = len(fin.readlines())

if LINES_GET > number_of_lines:
     print ("Are you sick!!!!")
     sys.exit(1)

# Choose a random number of a line from the file.
fout.write("15 random number:\n\n")
for i in random.sample(range(1,  number_of_lines+1), LINES_GET):
    fout.write(linecache.getline('Capital_Test.txt', i) + "\n")
    #print (linecache.getline('Capital_filtered.txt', i))

linecache.clearcache()


#To get 20
LINES_GET = 20
fout = open("Capital_Random_TestData.txt", 'a', encoding="utf-8")
# Get number of line in the file.
with open('Capital_Test.txt') as fin:
    number_of_lines = len(fin.readlines())

if LINES_GET > number_of_lines:
     print ("Are you sick!!!!")
     sys.exit(1)

# Choose a random number of a line from the file.
fout.write("20 random number:\n\n")
for i in random.sample(range(1,  number_of_lines+1), LINES_GET):
    fout.write(linecache.getline('Capital_Test.txt', i) + "\n")
    #print (linecache.getline('Capital_filtered.txt', i))

linecache.clearcache()

#To get 25
LINES_GET = 25
fout = open("Capital_Random_TestData.txt", 'a', encoding="utf-8")
# Get number of line in the file.
with open('Capital_Test.txt') as fin:
    number_of_lines = len(fin.readlines())

if LINES_GET > number_of_lines:
     print ("Are you sick!!!!")
     sys.exit(1)

# Choose a random number of a line from the file.
fout.write("25 random number:\n\n")
for i in random.sample(range(1,  number_of_lines+1), LINES_GET):
    fout.write(linecache.getline('Capital_Test.txt', i) + "\n")
    #print (linecache.getline('Capital_filtered.txt', i))

linecache.clearcache()

#To get 30
LINES_GET = 30
fout = open("Capital_Random_TestData.txt", 'a', encoding="utf-8")
# Get number of line in the file.
with open('Capital_Test.txt') as fin:
    number_of_lines = len(fin.readlines())

if LINES_GET > number_of_lines:
     print ("Are you sick!!!!")
     sys.exit(1)

# Choose a random number of a line from the file.
fout.write("30 random number:\n\n")
for i in random.sample(range(1,  number_of_lines+1), LINES_GET):
    fout.write(linecache.getline('Capital_Test.txt', i) + "\n")
    #print (linecache.getline('Capital_filtered.txt', i))

linecache.clearcache()


#To get 35
LINES_GET = 35
fout = open("Capital_Random_TestData.txt", 'a', encoding="utf-8")
# Get number of line in the file.
with open('Capital_Test.txt') as fin:
    number_of_lines = len(fin.readlines())

if LINES_GET > number_of_lines:
     print ("Are you sick!!!!")
     sys.exit(1)

# Choose a random number of a line from the file.
fout.write("35 random number:\n\n")
for i in random.sample(range(1,  number_of_lines+1), LINES_GET):
    fout.write(linecache.getline('Capital_Test.txt', i) + "\n")
    #print (linecache.getline('Capital_filtered.txt', i))

linecache.clearcache()

#To get 40
LINES_GET = 40
fout = open("Capital_Random_TestData.txt", 'a', encoding="utf-8")
# Get number of line in the file.
with open('Capital_Test.txt') as fin:
    number_of_lines = len(fin.readlines())

if LINES_GET > number_of_lines:
     print ("Are you sick!!!!")
     sys.exit(1)

# Choose a random number of a line from the file.
fout.write("40 random number:\n\n")
for i in random.sample(range(1,  number_of_lines+1), LINES_GET):
    fout.write(linecache.getline('Capital_Test.txt', i) + "\n")
    #print (linecache.getline('Capital_filtered.txt', i))

linecache.clearcache()

#To get 45
LINES_GET = 45
fout = open("Capital_Random_TestData.txt", 'a', encoding="utf-8")
# Get number of line in the file.
with open('Capital_Test.txt') as fin:
    number_of_lines = len(fin.readlines())

if LINES_GET > number_of_lines:
     print ("Are you sick!!!!")
     sys.exit(1)

# Choose a random number of a line from the file.
fout.write("45 random number:\n\n")
for i in random.sample(range(1,  number_of_lines+1), LINES_GET):
    fout.write(linecache.getline('Capital_Test.txt', i) + "\n")
    #print (linecache.getline('Capital_filtered.txt', i))

linecache.clearcache()

#To get 50
LINES_GET = 50
fout = open("Capital_Random_TestData.txt", 'a', encoding="utf-8")
# Get number of line in the file.
with open('Capital_Test.txt') as fin:
    number_of_lines = len(fin.readlines())

if LINES_GET > number_of_lines:
     print ("Are you sick!!!!")
     sys.exit(1)

# Choose a random number of a line from the file.
fout.write("50 random number:\n\n")
for i in random.sample(range(1,  number_of_lines+1), LINES_GET):
    fout.write(linecache.getline('Capital_Test.txt', i) + "\n")
    #print (linecache.getline('Capital_filtered.txt', i))

linecache.clearcache()

