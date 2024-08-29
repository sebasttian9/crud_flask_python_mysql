# logica de negocio
from app import db
from app.models import Curso

def get_all_cursos():
    return Curso.query.all()

def get_curso_by_id(curso_id):
    return Curso.query.get_or_404(curso_id)

def create_curso(curso_data):
    curso = Curso(
        curso = curso_data['curso']
        lenguaje = curso_data['lenguaje']
        nivel = curso_data['nivel']
    )
    db.session.add(curso)
    db.session.commit()


def update_curso(curso_id, curso_data):
    curso = Curso.query.get_or_404(curso_id)
        curso.curso = curso_data['curso']
        curso.lenguaje = curso_data['lenguaje']
        curso.nivel = curso_data['nivel']
    db.session.commit()

def delete_curso(curso_id):
    curso = Curso.query.get_or_404(curso_id)
    db.session.delete(curso)
    db.session.commit()