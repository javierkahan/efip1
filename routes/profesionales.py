from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.profesional import Profesional

profesionales = Blueprint("profesionales", __name__)


@profesionales.route('/listar_profesional', methods=['GET', 'POST'])
def index():
    profesionales = Profesional.listar_todos()
    if request.method == 'POST':
        dni = request.form['dni']
        resultado = Profesional.listar_dni(dni)
        if resultado:
            profesionales = resultado
    return render_template('profesional/profesional.html', profesionales=profesionales)


@profesionales.route('/nuevo_profesional', methods=['GET', 'POST'])
def nuevo_profesional():
    profesionales = Profesional.listar_ultimos()
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        dni = request.form['dni']
        email = request.form['email']
        telefono = request.form['telefono']
        especialidad = request.form['especialidad']
        estado = Profesional(nombre, apellido, dni, email, telefono, especialidad).nuevo()
        flash(estado)

    return render_template('profesional/nuevo_profesional.html', profesionales=profesionales)


@profesionales.route("/actualizar_profesional/<string:id_profesional>", methods=["GET", "POST"])
def actualizar_profesional(id_profesional):
    profesional = Profesional.listar(id_profesional)

    if request.method == "POST":
        profesional.nombre = request.form['nombre']
        profesional.apellido = request.form['apellido']
        profesional.dni = request.form['dni']
        profesional.email = request.form['email']
        profesional.telefono = request.form['telefono']
        profesional.especialidad = request.form['especialidad']
        estado = profesional.actualizar()
        flash(estado)
        return redirect(url_for('profesionales.index'))

    return render_template("profesional/actualizar_profesional.html", profesional=profesional)


@profesionales.route("/eliminar_profesional/<id_profesional>", methods=["GET"])
def eliminar_profesional(id_profesional):
    profesional = Profesional.listar(id_profesional)
    estado = Profesional.eliminar(profesional)

    flash(estado)

    return redirect(url_for('profesionales.index'))
