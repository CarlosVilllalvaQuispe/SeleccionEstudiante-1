from src.seleccionestudiante.modelo.Asignatura import Asignatura
from src.seleccionestudiante.modelo.declarative_base import engine, Base, session
#import
from src.seleccionestudiante.modelo.Actividad import Actividad
from src.seleccionestudiante.modelo.Equipo import Equipo
from src.seleccionestudiante.modelo.Estudiante import Estudiante

class Sorteo():

    def __init__(self):
        Base.metadata.create_all(engine)
    #asignatura
    def agregar_asignatura(self, nombreAsignatura):
        busqueda = session.query(Asignatura).filter(Asignatura.nombreAsignatura == nombreAsignatura).all()
        if len(busqueda) == 0:
            asignatura = Asignatura(nombreAsignatura=nombreAsignatura)
            session.add(asignatura)
            session.commit()
            return True
        else:
            return False

#actividad nuestra
    #Actividad
    def agregar_actividad(self, denominacionActividad):
        busqueda1 = session.query(Actividad).filter(Actividad.denominacionActividad == denominacionActividad).all()
        if len(busqueda1) == 0:
            actividad = Actividad(denominacionActividad=denominacionActividad)
            session.add(actividad)
            session.commit()
            return True
        else:
            return False
    #equipo
    def agregar_equipo(self, denominacionEquipo):
        busqueda2 = session.query(Equipo).filter(Equipo.denominacionEquipo == denominacionEquipo).all()
        if len(busqueda2) == 0:
            equipo = Equipo(denominacionEquipo=denominacionEquipo)
            session.add(equipo)
            session.commit()
            return True
        else:
            return False
    #Estudiante Luchito
    def agregar_estudiante(self, apellidoPaterno, apellidoMaterno, nombres, elegible):
        busqueda = session.query(Estudiante).filter(
            Estudiante.apellidoPaterno + Estudiante.apellidoMaterno + Estudiante.nombres == apellidoPaterno + apellidoMaterno + nombres).all()
        if len(busqueda) == 0:
            estudiante = Estudiante(apellidoPaterno=apellidoPaterno, apellidoMaterno=apellidoMaterno, nombres=nombres,
                                    elegible=elegible)
            session.add(estudiante)
            session.commit()
            return True
        else:
            return False