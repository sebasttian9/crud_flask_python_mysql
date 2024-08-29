# vistas de la aplicacion , maneja solicitudes http
from flask import render_template, request, redirect, url_for
from app import app,db
from app.models import Curso

@app.route('/')
def index():
    cursos = Curso.query.all()
    return render_template('index.html',cursos=cursos)


@app.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        curso = request.form['curso']
        lenguaje = request.form['lenguaje']
        nivel = request.form['nivel']
        new_curso = Curso(curso=curso, lenguaje=lenguaje, nivel=nivel)
        db.session.add(new_curso)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create.html')



@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    curso = Curso.query.get_or_404(id)
    if request.method == 'POST':
        curso.curso = request.form['curso']
        curso.lenguaje = request.form['lenguaje']
        curso.nivel = request.form['nivel']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html',curso=curso)


@app.route('/delete/<int:id>')
def delete(id):
    curso = Curso.query.get_or_404(id)
    db.session.delete(curso)
    db.session.commit()
    return redirect(url_for('index'))