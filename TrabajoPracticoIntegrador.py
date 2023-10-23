from abc import ABC, abstractmethod
from generador_contra import generar

#Clases

class Usuario(ABC):
    def __init__(self, nombre, apellido, email, contrasenia):
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._contrasenia = contrasenia

    def __str__(self):
        return f"- Nombre: {self._nombre}\n- Apellido: {self._apellido}\n- Email: {self._email}"

    @abstractmethod
    def validar_credenciales(self, email, contrasenia):
        pass #no se

class Estudiante(Usuario): 
    def __init__(self, nombre, apellido, email, contrasenia, legajo, anio_inscripcion_carrera):
        super().__init__(nombre, apellido, email, contrasenia)
        self._legajo = legajo 
        self._anio_inscripcion_carrera = anio_inscripcion_carrera
        
    def __str__(self):
        return super().__str__() + f"\n- Legajo: {self._legajo}\n- Año de inscripción a la carrera: {self._anio_inscripcion_carrera}"
    
    def matricular_en_curso (self):
        pass #no se 

    def validar_credenciales(self, email, contrasenia):
        super().validar_credenciales(email, contrasenia)
        if email == self._email:
            if contrasenia == self._contrasenia:  
                return True
            else:
                return False
        else:
            return False

class Profesor(Usuario): 
    def __init__(self, nombre, apellido, email, contrasenia, titulo, anio_egreso):
        super().__init__(nombre, apellido, email, contrasenia)
        self._titulo = titulo 
        self._anio_egreso = anio_egreso
    
    def dictar_curso (self):
        pass #no se 

    def __str__(self):
        return super().__str__() + f"\n- Titulo: {self._titulo}\n- Año de egreso: {self._anio_egreso}"

    def validar_credenciales(self, email, contrasenia):
        super().validar_credenciales(email, contrasenia)
        if email == self._email:
            if contrasenia == self._contrasenia:  
                return True
            else:
                return False
        else:
            return False

class Curso: 
    def __init__(self, nombre):
        self._nombre = nombre
        self._contrasenia_matriculacion = generar()

    def __str__(self):
        return f"- Curso: {self._nombre}"