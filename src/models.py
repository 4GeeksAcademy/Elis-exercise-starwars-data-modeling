import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    last_name = Column(String(250))
    address = relationship("Address", back_populates="person")
    
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(400), nullable=False)
    user_name = Column(String(400))
    email = Column(String(400))
    password = Column(String(400))
    
    # Definiendo una relación con 'Favorites'
    favorites = relationship('Favorites', back_populates='user')

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    
    # Relacionando la dirección con la persona
    person = relationship('Person', back_populates='address')

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    description = Column(String(600))
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    climate = Column(String(600))
    terrain = Column(String(600))
    
    # Relación con 'Person' (puede ser opcional)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship("Person")

    # Relación con 'Favorites'
    favorites = relationship('Favorites', back_populates='planet')

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(300))
    description = Column(String(600))
    gender = Column(String(300))
    mass = Column(Integer)
    
    # Relación con 'Favorites'
    favorites = relationship('Favorites', back_populates='character')

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))
    
    # Relaciones con las entidades correspondientes
    user = relationship('User', back_populates='favorites')
    planet = relationship('Planets', back_populates='favorites')
    character = relationship('Characters', back_populates='favorites')

    def to_dict(self):
        return {}

# Generar el diagrama ER
render_er(Base, 'diagram.png')
