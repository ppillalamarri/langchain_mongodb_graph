# langchain_mongodb_graph

This code will convert Graph based nodes and relationships into JSON documents that can be stored in MongoDB collections and leverage graphlookup

Nodes:[Node(id='The Matrix', properties={'label': 'movie', 'title': 'The Matrix'}), Node(id='Keanu Reeves', properties={'label': 'actor', 'name': 'Keanu Reeves'}), Node(id='Laurence Fishburne', properties={'label': 'actor', 'name': 'Laurence Fishburne'}), Node(id='Carrie-Anne Moss', properties={'label': 'actor', 'name': 'Carrie-Anne Moss'})]
Relationships:[Relationship(source=Node(id='Keanu Reeves', properties={'label': 'actor', 'name': 'Keanu Reeves'}), target=Node(id='The Matrix', properties={'label': 'movie', 'title': 'The Matrix'}), type='ActedIn', properties={'label': 'ActedIn'}), Relationship(source=Node(id='Laurence Fishburne', properties={'label': 'actor', 'name': 'Laurence Fishburne'}), target=Node(id='The Matrix', properties={'label': 'movie', 'title': 'The Matrix'}), type='ActedIn', properties={'label': 'ActedIn'}), Relationship(source=Node(id='Carrie-Anne Moss', properties={'label': 'actor', 'name': 'Carrie-Anne Moss'}), target=Node(id='The Matrix', properties={'label': 'movie', 'title': 'The Matrix'}), type='ActedIn', properties={'label': 'ActedIn'}), Relationship(source=Node(id='The Matrix', properties={'label': 'movie', 'title': 'The Matrix'}), target=Node(id='Keanu Reeves', properties={'label': 'actor', 'name': 'Keanu Reeves'}), type='Starring', properties={'label': 'Strarring'}), Relationship(source=Node(id='The Matrix', properties={'label': 'movie', 'title': 'The Matrix'}), target=Node(id='Laurence Fishburne', properties={'label': 'actor', 'name': 'Laurence Fishburne'}), type='Starring', properties={'label': 'Strarring'}), Relationship(source=Node(id='The Matrix', properties={'label': 'movie', 'title': 'The Matrix'}), target=Node(id='Carrie-Anne Moss', properties={'label': 'actor', 'name': 'Carrie-Anne Moss'}), type='Straring', properties={'label': 'Strarring'})]
Printing........................................ {'lc': 1, 'type': 'not_implemented', 'id': ['langchain_community', 'graphs', 'graph_document', 'GraphDocument'], 'repr': "GraphDocument(nodes=[Node(id='The Matrix', properties={'label': 'movie', 'title': 'The Matrix'}), Node(id='Keanu Reeves', properties={'label': 'actor', 'name': 'Keanu Reeves'}), Node(id='Laurence Fishburne', properties={'label': 'actor', 'name': 'Laurence Fishburne'}), Node(id='Carrie-Anne Moss', properties={'label': 'actor', 'name': 'Carrie-Anne Moss'})], relationships=[Relationship(source=Node(id='Keanu Reeves', properties={'label': 'actor', 'name': 'Keanu Reeves'}), target=Node(id='The Matrix', properties={'label': 'movie', 'title': 'The Matrix'}), type='ActedIn', properties={'label': 'ActedIn'}), Relationship(source=Node(id='Laurence Fishburne', properties={'label': 'actor', 'name': 'Laurence Fishburne'}), target=Node(id='The Matrix', properties={'label': 'movie', 'title': 'The Matrix'}), type='ActedIn', properties={'label': 'ActedIn'}), Relationship(source=Node(id='Carrie-Anne Moss', properties={'label': 'actor', 'name': 'Carrie-Anne Moss'}), target=Node(id='The Matrix', properties={'label': 'movie', 'title': 'The Matrix'}), type='ActedIn', properties={'label': 'ActedIn'}), Relationship(source=Node(id='The Matrix', properties={'label': 'movie', 'title': 'The Matrix'}), target=Node(id='Keanu Reeves', properties={'label': 'actor', 'name': 'Keanu Reeves'}), type='Starring', properties={'label': 'Strarring'}), Relationship(source=Node(id='The Matrix', properties={'label': 'movie', 'title': 'The Matrix'}), target=Node(id='Laurence Fishburne', properties={'label': 'actor', 'name': 'Laurence Fishburne'}), type='Starring', properties={'label': 'Strarring'}), Relationship(source=Node(id='The Matrix', properties={'label': 'movie', 'title': 'The Matrix'}), target=Node(id='Carrie-Anne Moss', properties={'label': 'actor', 'name': 'Carrie-Anne Moss'}), type='Straring', properties={'label': 'Strarring'})], source=Document(page_content='Matrix is a movie where Keanu Reeves, Laurence Fishburne and Carrie-Anne Moss acted.'))"}
