

#f = open("filename.txt")
#for line in f:
'''
fin = open("input.txt")
fout = open("output.txt", "w+")
delete_list = ['https://', 'http://', 'www.']
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()
print ('./ done')
'''


fin = open("Capital.txt")
fout = open("Capital1.txt", "w+")
delete_list = ['http://dbpedia.org/resource/']
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()
print ('./ done')





f = open( "output.txt", "r" )
text = f.read()
f.close()
newText = ""
for each in text:
    if each == "-":
        each = "_" #Or replace it with whatever you like.
    newText += each
f = open( "Capital_Clean.txt", "w" )
f.write( newText )
f.close()
