Usage

1. 

Documentation
=============

Dependencies

Python >= 3.8

Python Libraries:
=================
json
avro
rdflib
pyld

Purpose
=======

In today’s fast paced data driven landscape, enterprises strive to process large volumes of data streamed across multiple systems to deliver real-time events and signals which enable superior customer experiences, automation, and efficient operations. However, they face challenges in seamlessly connecting diverse data from disparate systems in real-time to build linked data products such as 360-degree views of customer or account. Linked Data, a method to structure and interconnect disparate data sources solves this problem and can be encoded with data interchange formats such as JSON (JavaScript Object Notation). Linked Data encoded with JSON is known as JSON-LD (JavaScript Object Notation for Linked Data). 
  While JSON-LD can help link the data, the most popular choice for data streams is Avro which is a data serialization framework renowned for schema evolution and binary compaction. Avro does not support embedding semantic information and Linked Data specifications, thereby limiting the ability to use Avro for generating linked data streams. But since Avro allows data to be defined using JSON datatypes, we leverage it to introduce semantics and Linked Data concepts with Avro schema and its binary payload. This is achieved by referencing standardized Open vocabularies and vocabulary URIs (Uniform Resource Identifiers) to provide context, embedding instance URIs to reference identifiers for the data and finally, designing the data into objects, organized as “things of data” which allows a modular way to process and store data entities and domains. We call this “Modernized Avro for Linked Data.” 
  Thus, modernized Avro allows consumers to seamlessly listen to multiple data streams and link them to build a 360-degree views of data in a near real-time fashion. Modernized Avro shall open doors to enable seamless data interoperability across various systems and platforms. It shall allow data from disparate Avro events to integrate effortlessly, creating a cohesive and unified data ecosystem and allowing for sophisticated data discovery mechanisms. Linked Data facilitates more effective data analytics. We can now apply powerful semantic reasoning and query capabilities to Avro event data, enabling advanced analytics and more precise data-driven decision-making. 
