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

f= io.open("Capital.txt","w+", encoding="utf-8")
#for i in range(10):
    # f.write("This is line %d\r\n" % (i+1))
# interpret the results:
for res in results["results"]["bindings"] :
 f.write("{0}       {1}\n\n" .format(res['country']['value'],  res['capital']['value']))
    #f.write( "'%s'       '%s'\n\n" %  (res['country']['value'] + ' ' + res['capital']['value'] + '\n\n'))
  #f.write("%s       %s\n\n" %  res['country']['value'],  res['capital']['value'])

   # print("%s --> %s\n\n" % (res['country']['value'],  res['capital']['value']))

#f.write(res['country']['value']+' '+res['capital']['value']+'\n\n')

#instr = "'%s', '%s', '%d', '%s', '%s', '%s', '%s'" % softname, procversion, int(percent), exe, description, company, procurl
#instr = "'{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}'".format(softname, procversion, int(percent), exe, description, company, procurl)
#instr = "'%s', '%s', '%d', '%s', '%s', '%s', '%s'" % (softname, procversion, int(percent), exe, description, company, procurl)
    #print (res['country']['value'],   res['capital']['value'])


    #f.write("%i %5.2f\n" % (a[i], b[i]))
   # file.write("InputOne: %s \n InputTwo: %s" % input1, input2)