import io

fin = open("spouse.txt", encoding="utf-8")
fout = open("Spouse_output.txt", "w+", encoding="utf-8")
#delete_list = ['https://', 'http://', 'www.']
delete_list = ['http://dbpedia.org/resource/']
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()
print ('Processing Finished')