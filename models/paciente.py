from utils.db import db
from sqlalchemy.exc import SQLAlchemyError


class Paciente(db.Model):
    id_paciente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    dni = db.Column(db.Integer, nullable=False, unique=True)
    fecha_nacimiento = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=True)
    telefono = db.Column(db.String(100), nullable=True)
    turno = db.relationship('Turno', backref='paciente', lazy='dynamic')

    def __init__(self, nombre, apellido, dni, fecha_nacimiento, email, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.email = email
        self.telefono = telefono

    def nuevo(self):
        try:
            db.session.add(self)
            db.session.commit()
            return 'Paciente agregado'
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f'ERROR:{e}')
            return 'No pudo completarse la operación'

    @staticmethod
    def listar_todos():
        """Lista todos los pacientes en la DB"""
        return Paciente.query.all()

    @staticmethod
    def listar_ultimos():
        """Lista los ultimos 3 pacientes en la DB"""
        return Paciente.query.order_by(Paciente.id_paciente.desc()).limit(3)

    @classmethod
    def listar(cls, id_paciente):
        """Lista datos de un paciente por su id_paciente"""
        return Paciente.query.get(id_paciente)

    @staticmethod
    def listar_dni(dni):
        """Lista datos de un paciente por dni"""
        return Paciente.query.filter(Paciente.dni == dni).all()

    def actualizar(self):
        """Realiza el commit del actualizado"""
        try:
            db.session.commit()
            return 'Actualización exitosa'
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f'ERROR:{e}')
            return 'No pudo completarse la operación'

    @classmethod
    def eliminar(cls, paciente):
        try:
            db.session.delete(paciente)
            db.session.commit()
            return 'Eliminación exitosa'
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f'ERROR:{e}')
            return 'No pudo completarse la operación'
