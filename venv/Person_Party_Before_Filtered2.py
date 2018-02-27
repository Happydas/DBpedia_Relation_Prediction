'''
string="infile.txt";
#for line in fin:
    #for word in delete_list:
       # line = line.replace(word, "")
while string[-1] == '_':
    string = string[:-1]
    for line in string:
        line = line.replace(word, "")
        print(string)

    #print(string)
'''
#while string[-1]=='\\':
   # string = string[:-1]
'''
string="mystring_";
if string[-1] == '_':
    string = string[:-1]
    print(string)
'''

fin = ('Person_Party_Before_Filtered.txt', 'r')
fout = ('Person_Party_Before_Filtered.txt', 'w')
if string[-1] == '_':
    string = string[:-1]
    for line in fin:
        for word in string:
            line = line.replace(word, "")
            print(line)

            # print(string)



