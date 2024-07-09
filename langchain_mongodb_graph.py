import os
import json
import getpass

from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_openai import ChatOpenAI
from langchain_core.documents import Document
from langchain_community.graphs.graph_document import GraphDocument, Node, Relationship
from pymongo import MongoClient

#os.environ["OPENAI_API_KEY"] = getpass.getpass()
os.environ["OPENAI_API_KEY"] = ""

text = """
Marie Curie, born in 1867, was a Polish and naturalised-French physicist and chemist who conducted pioneering research on radioactivity.
She was the first woman to win a Nobel Prize, the first person to win a Nobel Prize twice, and the only person to win a Nobel Prize in two scientific fields.
Her husband, Pierre Curie, was a co-winner of her first Nobel Prize, making them the first-ever married couple to win the Nobel Prize and launching the Curie family legacy of five Nobel Prizes.
She was, in 1906, the first woman to become a professor at the University of Paris.
"""

#llm = ChatOpenAI(temperature=0, model_name="gpt-4-turbo")
#llm_transformer = LLMGraphTransformer(llm=llm)

#documents = [Document(page_content=text)]
#graph_documents = llm_transformer.convert_to_graph_documents(documents)
#print(f"Nodes:{graph_documents[0].nodes}")
#print(f"Relationships:{graph_documents[0].relationships}")

source_doc = Document(
    page_content="Matrix is a movie where Keanu Reeves, Laurence Fishburne and Carrie-Anne Moss acted."
)
movie = Node(id="The Matrix", properties={"label": "movie", "title": "The Matrix"})
actor1 = Node(id="Keanu Reeves", properties={"label": "actor", "name": "Keanu Reeves"})
actor2 = Node(
    id="Laurence Fishburne", properties={"label": "actor", "name": "Laurence Fishburne"}
)
actor3 = Node(
    id="Carrie-Anne Moss", properties={"label": "actor", "name": "Carrie-Anne Moss"}
)
rel1 = Relationship(
    id=5, type="ActedIn", source=actor1, target=movie, properties={"label": "ActedIn"}
)
rel2 = Relationship(
    id=6, type="ActedIn", source=actor2, target=movie, properties={"label": "ActedIn"}
)
rel3 = Relationship(
    id=7, type="ActedIn", source=actor3, target=movie, properties={"label": "ActedIn"}
)
rel4 = Relationship(
    id=8,
    type="Starring",
    source=movie,
    target=actor1,
    properties={"label": "Strarring"},
)
rel5 = Relationship(
    id=9,
    type="Starring",
    source=movie,
    target=actor2,
    properties={"label": "Strarring"},
)
rel6 = Relationship(
    id=10,
    type="Straring",
    source=movie,
    target=actor3,
    properties={"label": "Strarring"},
)
graph_doc = GraphDocument(
    nodes=[movie, actor1, actor2, actor3],
    relationships=[rel1, rel2, rel3, rel4, rel5, rel6],
    source=source_doc,
)


print(f"Nodes:{graph_doc.nodes}")
print(f"Relationships:{graph_doc.relationships}")

# Convert to JSON
#graph_json = json.dumps(graph_dict, ensure_ascii=False)
graph_json = graph_doc.to_json()

# Print or use the JSON string
print("Printing........................................",graph_json)

try:
  uri = "mongodb+srv://<<username>>:<<password>>@cluster0.s0plv.mongodb.net/"
  client = MongoClient(uri)
  database = client["test_database"]
  collection = database["test_collection"]

  result = collection.insert_one(graph_json)
  print("Inserted:",result.acknowledged)

  #result = collection.insert_one(graph_documents[0].to_json())
  #print("Inserted:",result.acknowledged)

  client.close()
except Exception as e:
    raise Exception(
       "The following error occurred: ", e)
