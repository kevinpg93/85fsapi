from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from typing import List

db = SQLAlchemy()

class Usuarios(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(Integer, primary_key=True)
    nombre = db.Column(String(50), nullable=True)
    correo = db.Column(String(100), nullable=False)
    contraseña = db.Column(String(20), nullable=False)
    suscripcion = db.Column(String(10), nullable=True)
    favoritosper=db.relationship("Favoritos_personajes", backref="usuarios")
    favoritospla=db.relationship("Favoritos_planetas", backref="usuarios")
    def serialize(self):#Cada modelo tiene método serialize() para convertir el objeto en un diccionario serializable (para JSON), no incluir contraseñas
        return {
            "id": self.id,
            "correo": self.correo,
            "contraseña": self.contraseña
            # do not serialize the password, its a security breach
        }
class Planetas(db.Model):
    __tablename__ = "planetas"
    id = db.Column(Integer, primary_key=True)
    nombre_planeta = db.Column(String(50), nullable=False)
    poblacion = db.Column(String(20), nullable=False)
    extension = db.Column(String(10), nullable=False)
    favoritospla=db.relationship("Favoritos_planetas", backref="planetas")
    def serialize(self):
        return {
            "id_planeta": self.id,
            "nombre_planeta": self.nombre_planeta
            # do not serialize the password, its a security breach
        }
class Personajes(db.Model):
    __tablename__ = "personajes"
    id = db.Column(Integer, primary_key=True)
    nombre_personaje = db.Column(String(50), nullable=False)
    color_de_ojos = db.Column(String(100), nullable=False)
    color_de_pelo = db.Column(String(20), nullable=False)
    altura_de = db.Column(String(10), nullable=False)
    favoritosper =db.relationship("Favoritos_personajes", backref="personajes")
    def serialize(self):
        return {
            "id": self.id,
            "nombre_personaje": self.nombre_personaje
            # do not serialize the password, its a security breach
        }
class Favoritos_personajes(db.Model):
    __tablename__ = "favoritos_personajes"
    id = db.Column(Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"))
    personaje_id= db.Column(db.Integer, db.ForeignKey("personajes.id"))
    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "personaje_id": self.personaje_id
        }
class Favoritos_planetas(db.Model):
    __tablename__ = "favoritos_planetas"
    id = db.Column(Integer, primary_key=True)
    usuario_id= db.Column(db.Integer, db.ForeignKey("usuarios.id"))
    planeta_id= db.Column(db.Integer, db.ForeignKey("planetas.id"))
    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "planeta_id": self.planeta_id
        }