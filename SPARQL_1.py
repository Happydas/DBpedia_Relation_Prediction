from SPARQLWrapper import SPARQLWrapper, JSON

# wrap the dbpedia SPARQL end-point
endpoint = SPARQLWrapper("http://dbpedia.org/sparql")

# set the query string
endpoint.setQuery("""
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbpr: <http://dbpedia.org/resource/>
SELECT ?label
WHERE { dbpr:Asturias rdfs:label ?label }
""")

# select the retur format (e.g. XML, JSON etc...)
endpoint.setReturnFormat(JSON)

# execute the query and convert into Python objects
# Note: The JSON returned by the SPARQL endpoint is converted to nested Python dictionaries, so additional parsing is not required.
results = endpoint.query().convert()

# interpret the results:
for res in results["results"]["bindings"] :
    print (res['label']['value'])