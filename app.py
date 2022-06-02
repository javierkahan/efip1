from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from secrets import token_urlsafe
from routes.pacientes import pacientes
from routes.inicio import inicio
from routes.profesionales import profesionales
from routes.turnos import turnos

app = Flask(__name__)

"""
Parámetros de configuración
"""
app.secret_key = token_urlsafe(16)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite+pysqlite:///database/base_de_datos.db'
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Deshabilitado para las pruebas
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

SQLAlchemy(app)

"""
Registro de los routes
"""
app.register_blueprint(pacientes)
app.register_blueprint(inicio)
app.register_blueprint(profesionales)
app.register_blueprint(turnos)
