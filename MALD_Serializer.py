import os
import json
import avro
from avro.datafile import DataFileWriter
from avro.io import DatumWriter

'''
    Publisher :- Serialize Avro schema and Avro Payload to write Person Event Avro File 
'''

schema_fnm = 'name_and_address.avsc'
payload_fnm = 'name_and_address_payload.json'
serialized_avro_fnm = 'person_event.avro'

curr_path = os.path.dirname(os.path.abspath(__file__))
schema_input = '{}\{}'.format(curr_path, schema_fnm)
payload_input = '{}\{}'.format(curr_path, payload_fnm)
serialized_avro = '{}\{}.avro'.format(curr_path, serialized_avro_fnm)

schema = avro.schema.parse(open(schema_input, "rb").read())
payload_data = json.load(open(payload_input))

writer = DataFileWriter(open(serialized_avro, "wb"), DatumWriter(), schema)
writer.append(payload_data)
writer.close()
