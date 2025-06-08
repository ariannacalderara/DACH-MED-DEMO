import rdflib
from rdflib.namespace import RDF
from gpt4all import GPT4All


# Uncomment if you want to use OpenAI API
# import openai
# import os
# openai.api_key = os.getenv("OPENAI_API_KEY")


# Load your knowledge graph
def load_kg(file_path):
    g = rdflib.Graph()
    g.parse(file_path, format="ttl")
    return g

# Summarize or extract key concepts from the KG
def extract_summary(graph):
    concepts = set()
    for s, p, o in graph.triples((None, RDF.type, None)):
        concepts.add(str(o))
    summary = "Medical concepts in KG:\n" + "\n".join(concepts)
    return summary


# -------- GPT4All setup --------

# Initialize the model once (avoid loading it every time)
MODEL_PATH = "data/ggml-gpt4all-l13b-snoozy.bin"  # put the downloaded model here
model = GPT4All(model_name=MODEL_PATH)

def query_llm(prompt):
    response = model.generate(prompt, max_tokens=200)
    return response


# -------- Optional: OpenAI API version --------
'''
def query_llm(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200,
        temperature=0.5,
    )
    return response.choices[0].message.content.strip()
'''


def main():
    kg_file = "../data/kg_diabetes.ttl"
    kg = load_kg(kg_file)
    summary = extract_summary(kg)

    print("KG Summary:\n", summary)

    prompt = f"Based on the following medical knowledge graph summary, please provide insights:\n{summary}\n\nInsights:"

    answer = query_llm(prompt)
    print("LLM Response:\n", answer)


if __name__ == "__main__":
    main()
