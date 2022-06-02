from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.profesional import Profesional
from models.paciente import Paciente
from models.turno import Turno

turnos = Blueprint("turnos", __name__)


@turnos.route('/nuevo_turno', methods=['GET', 'POST'])
def nuevo_turno():
    profesionales = Profesional.listar_todos()
    if request.method == 'POST':
        dni_paciente = request.form['dni']
        profesional_id = request.form['profesional_elegido']
        fecha_turno = request.form['fecha_turno']
        paciente = Paciente.listar_dni(dni_paciente)
        turno = Turno(paciente[0].id_paciente, profesional_id, fecha_turno, 'Asignado')
        estado = turno.nuevo()
        flash(estado)

    return render_template('turno/nuevo_turno.html', profesionales=profesionales)


@turnos.route('/listar_turnos', methods=['GET', 'POST'])
def index():
    lista_turnos = Turno.listar_turnos()
    if request.method == 'POST':
        dni = request.form['dni']
        resultado = Turno.listar_turnos_paciente(dni)
        if resultado:
            lista_turnos = resultado
    return render_template('turno/turno.html', lista_turnos=lista_turnos)


@turnos.route("/eliminar_turno/<id_turno>", methods=["GET"])
def eliminar_turno(id_turno):
    turno = Turno.listar(id_turno)
    estado = Turno.eliminar(turno)
    flash(estado)

    return redirect(url_for('turnos.index'))
