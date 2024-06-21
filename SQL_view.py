from sqlalchemy import create_engine, inspect

# Connexion à la base de données SQLite
engine = create_engine('sqlite:///mydatabase.db')

# Inspecteur pour extraire les métadonnées
inspector = inspect(engine)

# Lecture et affichage des tables
tables = inspector.get_table_names()
print("Tables in the database:")
for table in tables:
    print(f"\nTable: {table}")

    # Lecture et affichage des colonnes pour chaque table
    columns = inspector.get_columns(table)
    for column in columns:
        print(f"Column: {column['name']} - Type: {column['type']}")

    # Lecture et affichage des clés primaires
    primary_keys = inspector.get_pk_constraint(table)
    print(f"Primary Keys: {primary_keys['constrained_columns']}")

    # Lecture et affichage des clés étrangères
    foreign_keys = inspector.get_foreign_keys(table)
    if foreign_keys:
        for foreign_key in foreign_keys:
            print(
                f"Foreign Key: {foreign_key['constrained_columns']} references {foreign_key['referred_table']}({foreign_key['referred_columns']})")
    else:
        print("No Foreign Keys")

# Fermeture de la connexion à la base de données
engine.dispose()

#----- Graphical output -----
from sqlalchemy import create_engine, inspect
import networkx as nx
import matplotlib.pyplot as plt

# Connexion à la base de données SQLite
engine = create_engine('sqlite:///mydatabase.db')

# Inspecteur pour extraire les métadonnées
inspector = inspect(engine)

# Création d'un graphe
G = nx.DiGraph()

# Lecture et ajout des tables au graphe
tables = inspector.get_table_names()
for table in tables:
    G.add_node(table)

    # Lecture des clés étrangères
    foreign_keys = inspector.get_foreign_keys(table)
    for foreign_key in foreign_keys:
        referred_table = foreign_key['referred_table']
        G.add_edge(table, referred_table)

# Fermeture de la connexion à la base de données
engine.dispose()

# Visualisation du graphe
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)  # Ajout d'un seed pour des positions reproductibles
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='skyblue')
nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=20)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

plt.title("Database Schema Relationship Graph")
plt.axis('off')  # Cacher les axes
plt.show()


