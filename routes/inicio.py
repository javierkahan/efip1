from flask import Blueprint, render_template, flash
from models.paciente import Paciente
from models.profesional import Profesional

inicio = Blueprint("inicio", __name__)


@inicio.route('/')
def info():
    return render_template('info.html')


@inicio.route('/cargar_db')
def cargar_db():
    """Cargar algunos datos para pruebas"""
    for num in range(1, 21):

        Paciente(f'Paciente{num}', f'Paciente_Ape{num}', f'2222222{num}', '05/05/1990', f'Paciente{num}@email.com',
                 f'15456367{num}').nuevo()

        if num < 8:
            especialidad = 'Psiquiatría'
        elif 8 <= num < 13:
            especialidad = 'Psicología'
        else:
            especialidad = 'Nutrición'

        Profesional(f'Profesional{num}', f'Profesional_Ape{num}', f'3333333{num}', f'Profesional{num}@email.com',
                    f'15456367{num}', especialidad).nuevo()

    flash('Datos de prueba cargados')
    return render_template('info.html')
