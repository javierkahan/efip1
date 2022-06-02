from models.profesional import Profesional
from utils.db import db
from models.paciente import Paciente
from sqlalchemy.exc import SQLAlchemyError


class Turno(db.Model):
    id_turno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_paciente = db.Column(db.Integer, db.ForeignKey('paciente.id_paciente'))
    id_profesional = db.Column(db.Integer, db.ForeignKey('profesional.id_profesional'))
    fecha_turno = db.Column(db.String(100))
    estado_turno = db.Column(db.String(100))

    def __init__(self, id_paciente, id_profesional, fecha_turno, estado_turno):
        self.id_paciente = id_paciente
        self.id_profesional = id_profesional
        self.fecha_turno = fecha_turno
        self.estado_turno = estado_turno

    def nuevo(self):
        try:
            db.session.add(self)
            db.session.commit()
            return 'Turno agregado'
        except SQLAlchemyError as e:
            print(f'ERROR:{e}')
            db.session.rollback()
            return 'No pudo completarse la operación'

    @classmethod
    def listar(cls, id_turno):
        """Lista datos de un turno por su id"""
        return Turno.query.get(id_turno)

    @staticmethod
    def listar_turnos_paciente(dni):
        """Lista todos los turnos por DNI de paciente"""

        resultado = db.session.query(Paciente, Profesional, Turno)\
            .select_from(Turno)\
            .outerjoin(Profesional, Profesional.id_profesional == Turno.id_profesional)\
            .outerjoin(Paciente, Paciente.id_paciente == Turno.id_paciente)\
            .filter(Paciente.dni == dni)\
            .order_by(Turno.fecha_turno.asc())\
            .all()

        return resultado

    @staticmethod
    def listar_turnos():
        """Lista todos los turnos """

        resultado = db.session.query(Paciente, Profesional, Turno)\
            .select_from(Turno)\
            .outerjoin(Profesional, Profesional.id_profesional == Turno.id_profesional)\
            .outerjoin(Paciente, Paciente.id_paciente == Turno.id_paciente)\
            .order_by(Turno.fecha_turno.asc())\
            .all()

        return resultado

    @classmethod
    def eliminar(cls, turno):
        try:
            db.session.delete(turno)
            db.session.commit()
            return 'Eliminación exitosa'
        except SQLAlchemyError as e:
            print(f'ERROR:{e}')
            db.session.rollback()
            return 'No pudo completarse la operación'
