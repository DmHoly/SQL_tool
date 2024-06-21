from sqlalchemy import create_engine, inspect

# Connexion à la base de données SQLite
engine = create_engine('sqlite:///mydatabase.db')

# Inspecteur pour extraire les métadonnées
inspector = inspect(engine)

# Lecture et affichage des tables
tables = inspector.get_table_names()


# Génération d'une requête SQL SELECT pour une table spécifique (par exemple, 'central_table')
def generate_select_query(table_name):
    columns = inspector.get_columns(table_name)
    column_names = [column['name'] for column in columns]

    # Création de la requête SELECT de base
    query = f"SELECT {', '.join(column_names)} FROM {table_name}"

    # Ajout des jointures pour les clés étrangères
    foreign_keys = inspector.get_foreign_keys(table_name)
    if foreign_keys:
        for foreign_key in foreign_keys:
            referred_table = foreign_key['referred_table']
            referred_columns = foreign_key['referred_columns']
            constrained_columns = foreign_key['constrained_columns']
            join_condition = ' AND '.join([f"{table_name}.{constrained} = {referred_table}.{referred}"
                                           for constrained, referred in zip(constrained_columns, referred_columns)])
            query += f" LEFT JOIN {referred_table} ON {join_condition}"

    return query


# Exemple d'utilisation pour 'central_table'
query = generate_select_query('central_table')
print(query)

# Fermeture de la connexion à la base de données
engine.dispose()
