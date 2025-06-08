# kg_utils.py
from rdflib import Graph, URIRef, Literal, RDF, Namespace
from rdflib.namespace import XSD

MED = Namespace("http://example.org/medical#")

def build_knowledge_graph(df, client_id="default"):
    g = Graph()
    g.bind("med", MED)

    for idx, row in df.iterrows():
        patient_uri = URIRef(f"http://example.org/{client_id}/patient/{idx}")
        g.add((patient_uri, RDF.type, MED.Patient))

        for feature in df.columns:
            if feature == "Outcome":
                outcome_uri = URIRef(f"http://example.org/outcome/{row[feature]}")
                g.add((outcome_uri, RDF.type, MED.Outcome))
                g.add((patient_uri, MED.hasOutcome, outcome_uri))
            else:
                g.add((
                    patient_uri,
                    MED[feature],
                    Literal(row[feature], datatype=XSD.float if isinstance(row[feature], float) else XSD.string)
                ))

    return g
 

