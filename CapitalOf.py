# -*- coding: utf-8 -*-
import io
from SPARQLWrapper import SPARQLWrapper, JSON

# wrap the dbpedia SPARQL end-point
endpoint = SPARQLWrapper("http://dbpedia.org/sparql")

# set the query string
endpoint.setQuery("""
SELECT DISTINCT ?country ?capital
 WHERE { 
?city rdf:type dbo:City ; 
rdfs:label ?label ; 
dbo:country ?country .
?country dbo:capital ?capital .
} order by ?country

""")

# select the retur format (e.g. XML, JSON etc...)
endpoint.setReturnFormat(JSON)

# execute the query and convert into Python objects
# Note: The JSON returned by the SPARQL endpoint is converted to nested Python dictionaries, so additional parsing is not required.
results = endpoint.query().convert()

f= open("Capital.txt","w+", encoding="utf-8")
#for i in range(10):
    # f.write("This is line %d\r\n" % (i+1))
# interpret the results:
for res in results["results"]["bindings"] :
    f.write("%s       %s\n\n" %  (res['country']['value'],  res['capital']['value']))


'''
    fin = open("Capital.txt")
    fout = open("output.txt", "w+")
    # delete_list = ['https://', 'http://', 'www.']
    delete_list = ['http://dbpedia.org/resource/']
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "")
        fout.write(line)
    fin.close()
    fout.close()
    print('./ done')
'''
    #print (res['country']['value'],   res['capital']['value'])


    #f.write("%i %5.2f\n" % (a[i], b[i]))
   # file.write("InputOne: %s \n InputTwo: %s" % input1, input2)