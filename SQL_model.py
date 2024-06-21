from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

# Table centrale
class CentralTable(Base):
    __tablename__ = 'central_table'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    first_level_tables = relationship('FirstLevelTable', back_populates='central_table')

# Premier niveau de tables
class FirstLevelTable(Base):
    __tablename__ = 'first_level_table'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    central_table_id = Column(Integer, ForeignKey('central_table.id'))
    central_table = relationship('CentralTable', back_populates='first_level_tables')
    second_level_tables = relationship('SecondLevelTable', back_populates='first_level_table')

# Deuxième niveau de tables
class SecondLevelTable(Base):
    __tablename__ = 'second_level_table'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    first_level_table_id = Column(Integer, ForeignKey('first_level_table.id'))
    first_level_table = relationship('FirstLevelTable', back_populates='second_level_tables')

# Création du moteur de base de données SQLite
engine = create_engine('sqlite:///mydatabase.db')

# Création des tables
Base.metadata.create_all(engine)

# Création d'une session pour interagir avec la base de données
Session = sessionmaker(bind=engine)
session = Session()

# Insertion de données d'exemple
central = CentralTable(name='Central Table 1')
session.add(central)
session.commit()

first_level = FirstLevelTable(name=f'First Level Table {0}', central_table=central)
session.add(first_level)
session.commit()

second_level = SecondLevelTable(name=f'Second Level Table {0}-{1}', first_level_table=first_level)
session.add(second_level)
session.commit()

# Fermeture de la session
session.close()
