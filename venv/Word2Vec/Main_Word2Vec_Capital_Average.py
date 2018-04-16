f = open("../Results/Main_Word2Vec_Capital_Counter.txt", 'r')
f1 = open("../Results/Main_Word2Vec_Capital_Average.txt", 'w')
lines = f.readlines()

total = 0

for line in lines:
    Type = line.split()
    if len(Type) > 1:
    #print(int(line))
        num = 0

        try:
            num += float(Type[0])
            total += num
        except ValueError:
            print("Invalid Syntax:", ValueError)

print("The sum is: ", total)
num_lines = sum(1 for line in open('../Results/Main_Word2Vec_Capital_Counter.txt'))
print(num_lines)
Average = total / num_lines
print(Average)
print(Type[1])
f1.write(str(Average) + " ")
f1.write(Type[1] + "\n")