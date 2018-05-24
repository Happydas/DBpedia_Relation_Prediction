# -*- coding: utf-8 -*-
import io

from SPARQLWrapper import SPARQLWrapper, JSON

# wrap the dbpedia SPARQL end-point
endpoint = SPARQLWrapper("http://dbpedia.org/sparql")

# set the query string
endpoint.setQuery("""
SELECT DISTINCT ?x ?y WHERE {
?x dbo:spouse ?y.
?y dbo:spouse ?x.
?x dbo:spouse|^dbo:spouse ?y .
FILTER (?x < ?y)
}  order by ?x

""")

# select the retur format (e.g. XML, JSON etc...)
endpoint.setReturnFormat(JSON)

# execute the query and convert into Python objects
# Note: The JSON returned by the SPARQL endpoint is converted to nested Python dictionaries, so additional parsing is not required.
results = endpoint.query().convert()

f= open("../Data/Spouse/spouse.txt","w+", encoding="utf-8")

# interpret the results:
for res in results["results"]["bindings"] :
    f.write("%s %s\n" %  (res['x']['value'],  res['y']['value']))

