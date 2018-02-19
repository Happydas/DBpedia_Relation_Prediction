s = 'lipsum'
n = 2
a, s = s[:n], s[n:]
print (a)
# lip
print (s)
# sum

fruit = "banana"
fruit[:3]
print(fruit)

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
fout = open("output.txt", "w+")
#delete_list = ['https://', 'http://', 'www.', "'"]
delete_list = ['http://dbpedia.org/resource/']
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()
print ('./ done')


'''
f = open( "test.txt", "r" )
text = f.read()
f.close()
newText = ""
for each in text:
    if each == ".":
        each = "" #Or replace it with whatever you like.
    newText += each
f = open( "output.txt", "w" )
f.write( newText )
f.close()
'''


f = open( "output.txt", "r" )
text = f.read()
f.close()
newText = ""
for each in text:
    if each == "-":
        each = "_" #Or replace it with whatever you like.
    newText += each
f = open( "output1.txt", "w" )
f.write( newText )
f.close()
