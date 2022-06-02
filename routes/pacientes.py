from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.paciente import Paciente

pacientes = Blueprint("pacientes", __name__)


@pacientes.route('/listar_paciente', methods=['GET', 'POST'])
def index():
    pacientes = Paciente.listar_todos()
    if request.method == 'POST':
        dni = request.form['dni']
        resultado = Paciente.listar_dni(dni)
        if resultado:
            pacientes = resultado
    return render_template('paciente/paciente.html', pacientes=pacientes)


@pacientes.route('/nuevo_paciente', methods=['GET', 'POST'])
def nuevo_paciente():
    pacientes = Paciente.listar_ultimos()
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        dni = request.form['dni']
        fecha_nacimiento = request.form['fecha_nacimiento']
        email = request.form['email']
        telefono = request.form['telefono']
        estado = Paciente(nombre, apellido, dni, fecha_nacimiento, email, telefono).nuevo()
        flash(estado)

    return render_template('paciente/nuevo_paciente.html', pacientes=pacientes)


@pacientes.route("/actualizar_paciente/<string:id_paciente>", methods=["GET", "POST"])
def actualizar_paciente(id_paciente):
    paciente = Paciente.listar(id_paciente)

    if request.method == "POST":
        paciente.nombre = request.form['nombre']
        paciente.apellido = request.form['apellido']
        paciente.dni = request.form['dni']
        paciente.fecha_nacimiento = request.form['fecha_nacimiento']
        paciente.email = request.form['email']
        paciente.telefono = request.form['telefono']
        estado = paciente.actualizar()
        flash(estado)
        return redirect(url_for('pacientes.index'))

    return render_template("paciente/actualizar_paciente.html", paciente=paciente)


@pacientes.route("/eliminar_paciente/<id_paciente>", methods=["GET"])
def eliminar_paciente(id_paciente):
    paciente = Paciente.listar(id_paciente)
    estado = Paciente.eliminar(paciente)

    flash(estado)

    return redirect(url_for('pacientes.index'))
