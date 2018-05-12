
f = open('../Data/Spouse_Before_Filtered.txt_2', 'w', encoding="utf-8")
with open('../Data/Spouse_Before_Filtered.txt', 'r', encoding="utf-8") as fin:
    for line in fin:
        sen = line.strip()
        if sen[-1:] == '_':
            sen = sen[:-1]
            f.write(sen +"\n")
        else:
            f.write(sen + "\n")
