
f = open('../Data/Person_Party_Before_filtered_2.txt', 'w', encoding="utf-8")
with open('../Data/Person_Party_Before_Filtered.txt', 'r', encoding="utf-8") as fin:
    for line in fin:
        sen = line.strip()
        if sen[-1:] == '_':
            sen = sen[:-1]
            line = line.replace(line, "")
            #print(sen)
            f.write(sen +"\n")
        else:
            f.write(sen + "\n")










