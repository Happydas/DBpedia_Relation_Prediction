f2 = open('../Data/Country_Currency_Data_3.txt', 'w+', encoding="utf-8")
f3 = open("../Data/Currency_Test.txt", 'r', encoding="utf-8")
lines = f3.readlines()
for line in lines:
    data = line.split()
    if data[1].find("_") == -1:
        print(data[0], data[1])
        f2.write(data[0] + " " + data[1] + "\n")
    else:
        string = data[1].split("_")
        if len(data) > 1 and len(string) > 1:
            print(data[0], string[1])
            f2.write(data[0] + " " + string[1] + "\n")















