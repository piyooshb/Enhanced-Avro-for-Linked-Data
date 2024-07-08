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

schema_fnm = 'name_and_address.avsc'
serialized_avro_fnm = 'person_event.avro'
context_fnm = 'name_and_address_context.json'
jsonld_fnm = 'name_and_address.jsonld'
nt_fnm = 'name_and_address.nt'

curr_path = os.path.dirname(os.path.abspath(__file__))
avro_schema = '{}\{}'.format(curr_path, schema_fnm)
serialized_avro = '{}\{}.avro'.format(curr_path, serialized_avro_fnm)
context_input = '{}\{}'.format(curr_path, context_fnm)
jsonld_output = '{}\{}'.format(curr_path, jsonld_fnm)
nt_output = '{}\{}'.format(curr_path, nt_fnm)

context = json.load(open(context_input))

reader = DataFileReader(open(serialized_avro, "rb"), DatumReader(avro_schema))

for avro_payload in reader:
  jsonld_data = {"@context": context, "@graph": [avro_payload]}
  
reader.close()

# Write JSON-LD document to a file
with open(jsonld_output, 'w') as output_file:
    output_file.write(json.dumps(jsonld_data, indent=4))
  
# Convert JSON-LD to RDF format (Turtle)
rdf_data = jsonld.to_rdf(jsonld_data, {'format': 'application/nquads'})

# Create an RDF graph
graph = Graph()
graph.parse(data=rdf_data, format='nquads')

# Serialize the graph to N-Triples format
nt_data = graph.serialize(format='nt')

# Write N-Triples to a file
with open(nt_output, "w") as outfile:
    outfile.write(nt_data)
