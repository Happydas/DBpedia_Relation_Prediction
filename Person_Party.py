# -*- coding: utf-8 -*-
import io

from SPARQLWrapper import SPARQLWrapper, JSON

# wrap the dbpedia SPARQL end-point
endpoint = SPARQLWrapper("http://dbpedia.org/sparql")

# set the query string
endpoint.setQuery("""
SELECT  DISTINCT  ?person ?party
 {{
SELECT  DISTINCT  ?person ?party {   
?person rdf:type  dbo:Person .
?person dbo:party ?party.
} 
ORDER BY ?person
}}
offset 6000
LIMIT 5000

""")

# select the retur format (e.g. XML, JSON etc...)
endpoint.setReturnFormat(JSON)

# execute the query and convert into Python objects
# Note: The JSON returned by the SPARQL endpoint is converted to nested Python dictionaries, so additional parsing is not required.
results = endpoint.query().convert()

f= open("Person_Party.txt","w+", encoding="utf-8")
#for i in range(10):
    # f.write("This is line %d\r\n" % (i+1))
# interpret the results:
for res in results["results"]["bindings"] :
    f.write("%s      %s\n\n" %  (res['person']['value'],  res['party']['value']))


#Clean data
fin = open("Person_Party.txt", encoding="utf-8")
fout = open("Person_Party_Clean.txt", "w+", encoding="utf-8")
#delete_list = ['https://', 'http://', 'www.']
delete_list = ['http://dbpedia.org/resource/']
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()
print ('Processing Finished')