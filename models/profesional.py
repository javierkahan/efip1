from utils.db import db
from sqlalchemy.exc import SQLAlchemyError


class Profesional(db.Model):
    id_profesional = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    dni = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=True)
    telefono = db.Column(db.String(100), nullable=True)
    especialidad = db.Column(db.String(100), nullable=False)
    turno = db.relationship('Turno', backref='profesional', lazy='dynamic')


    def __init__(self, nombre, apellido, dni, email, telefono, especialidad):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.email = email
        self.telefono = telefono
        self.especialidad = especialidad

    def nuevo(self):
        try:
            db.session.add(self)
            db.session.commit()
            return 'Profesional agregado'
        except SQLAlchemyError as e:
            print(f'ERROR:{e}')
            return 'No pudo completarse la operación'

    @staticmethod
    def listar_todos():
        """Lista todos los profesionales en la DB"""
        return Profesional.query.all()

    @staticmethod
    def listar_ultimos():
        """Lista los ultimos 3 profesionales en la DB"""
        return Profesional.query.order_by(Profesional.id_profesional.desc()).limit(3)

    @classmethod
    def listar(cls, id_profesional):
        """Lista datos de un profesional por su id_profesional"""
        return Profesional.query.get(id_profesional)

    @classmethod
    def listar_dni(cls, dni):
        """Lista datos de un profesional por dni"""
        return Profesional.query.filter(Profesional.dni == dni).all()

    @classmethod
    def listar_especialidad(cls, especialidad):
        """Lista datos de un profesional por dni"""
        return Profesional.query.filter(Profesional.especialidad == especialidad).all()

    def actualizar(self):
        """Realiza el commit del actualizado"""
        try:
            db.session.commit()
            return 'Actualización exitosa'
        except SQLAlchemyError as e:
            print(f'ERROR:{e}')
            return 'No pudo completarse la operación'

    @classmethod
    def eliminar(cls, profesional):
        try:
            db.session.delete(profesional)
            db.session.commit()
            return 'Eliminación exitosa'
        except SQLAlchemyError as e:
            print(f'ERROR:{e}')
            return 'No pudo completarse la operación'
