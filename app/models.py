# Modelo de datos 
from app import db

class Curso(db.Model):
    __tablename__ = 'cursos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    curso = db.Column(db.String(100), nullable=False)
    lenguaje = db.Column(db.String(100), nullable=False)
    nivel = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Curso {self.curso}>'