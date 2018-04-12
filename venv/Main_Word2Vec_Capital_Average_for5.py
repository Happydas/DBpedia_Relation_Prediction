
count=0
f1 = open("Main_Word2Vec_Capital_Average.txt", 'a')
with open ('Main_Word2Vec_Capital_Counter.txt','r') as f:
    lines = f.readlines()
    total = 0
    for line in lines[10:20]:
        count += 1
        Type = line.split()
        if len(Type) > 1:
            # print(int(line))
            num = 0

            try:
                num += float(Type[0])
                total += num
            except ValueError:
                print("Invalid Syntax:", ValueError)
            #print(Type[0])
print(count)
# print(total)

print("The sum is: ", total)
Average = total / count
print(Average)
print(Type[1])
f1.write(str(Average) + " ")
f1.write(str(Type[1]) + "\n")