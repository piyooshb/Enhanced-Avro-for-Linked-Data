import os
import json
import avro
from avro.datafile import DataFileWriter
from avro.io import DatumWriter


'''
    Publisher :- Serialize Avro schema and Avro Payload to write Person Event Avro File 
'''

schema = avro.schema.parse(open(name_and_address.avsc, "rb").read())
payload_data = json.load(open(name_and_address_payload.json))

writer = DataFileWriter(open(person_event.avro, "wb"), DatumWriter(), schema)
writer.append(payload_data)
writer.close()
