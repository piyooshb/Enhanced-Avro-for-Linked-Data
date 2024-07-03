import os
import json
import avro
from avro.datafile import DataFileReader
from avro.io import DatumReader
from rdflib import Graph
import pyld.jsonld as jsonld


'''
    Consumer :- 
        1. Read Avro schema, payload & context to write JSON-LD document
        2. Convert JSON-LD document to N-Triples 
'''

context = json.load(open(name_and_address_context.json))

reader = DataFileReader(open(person_event.avro, "rb"), DatumReader(name_and_address.avsc))

for avro_payload in reader:
  jsonld_data = {"@context": context, "@graph": [avro_payload]}
  
reader.close()

# Write JSON-LD document to a file
with open(name_and_address.jsonld, 'w') as output_file:
    output_file.write(json.dumps(jsonld_data, indent=4))
  
# Convert JSON-LD to RDF format (Turtle)
rdf_data = jsonld.to_rdf(jsonld_data, {'format': 'application/nquads'})

# Create an RDF graph
graph = Graph()
graph.parse(data=rdf_data, format='nquads')

# Serialize the graph to N-Triples format
nt_data = graph.serialize(format='nt')

# Write N-Triples to a file
with open(name_and_address.nt, "w") as outfile:
    outfile.write(nt_data)
