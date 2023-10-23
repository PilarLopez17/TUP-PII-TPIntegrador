from abc import ABC, abstractmethod
from generador_contra import generar

mis_cursos = {}
alumnos = []
profesores = []

# Clases
class Usuario(ABC):
    def __init__(self, nombre, apellido, email, contrasenia):
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._contrasenia = contrasenia

    def __str__(self):
        return f"- Nombre: {self._nombre}\n- Apellido: {self._apellido}\n- Email: {self._email}"

    def validar_credenciales(self, email, contrasenia):
        if self._email == email and self._contrasenia == contrasenia: 
            return True
        else:
            return False


class Estudiante(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia, legajo, anio_inscripcion_carrera):
        super().__init__(nombre, apellido, email, contrasenia)
        self._legajo = legajo
        self._anio_inscripcion_carrera = anio_inscripcion_carrera
        self._cursos = []

    def __str__(self):
        return super().__str__() + f"\n- Legajo: {self._legajo}\n- Año de inscripción a la carrera: {self._anio_inscripcion_carrera}"

    def matricular_en_curso(self, curso):
        if curso not in self._cursos:
            self._cursos.append(curso)
            print(f"Te matriculaste con éxito en el curso: {curso.nombre}")
        else:
            print("Error! Ya estás matriculado en este curso.")


class Profesor(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia, titulo, anio_egreso):
        super().__init__(nombre, apellido, email, contrasenia)
        self._titulo = titulo
        self._anio_egreso = anio_egreso
        self._cursos = []

    def dictar_curso(self, curso):
        self._cursos.append(curso)
        print(f"Ahora dictas el curso: {curso.nombre}")

    def __str__(self):
        return super().__str__() + f"\n- Titulo: {self._titulo}\n- Año de egreso: {self._anio_egreso}"


class Curso:
    def __init__(self, nombre):
        self._nombre = nombre
        self._contrasenia_matriculacion = generar()  # funcion extraida del tp anterior

    def __str__(self):
        return f"- Curso: {self._nombre}\n - Contraseña: {self._contrasenia_matriculacion}"

# Estudiantes y Profesores ya cargados


alum1 = Estudiante("Lucia", "Miranda", "lucia@gmail.com", "utn", 12345, 2023)
alumnos.append(alum1)

alum2 = Estudiante("Victoria", "Menna",
                   "victoria@gmail.com", "12345", 56789, 2019)
alumnos.append(alum2)

profe1 = Profesor("Pilar", "Lopez", "pilar@gmail.com",
                  "utn123", "Tecnica en Programación", 2022)
profesores.append(profe1)

profe2 = Profesor("Juan", "Perez", "juan@gmail.com",
                  "123utn", "Ingeniero en Sistemas", 2013)
profesores.append(profe2)

# Menu principal
while True:
    print("-- Menú Principal --")
    print("1. Ingresar cómo alumno")
    print("2. Ingresar cómo profesor")
    print("3. Ver cursos")
    print("4. Salir")

    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        email = input("Ingrese su email: ")
        
        for alumno in alumnos:
            if email == alumno._email:
                alumno_existe = alumno
                break

        if alumno_existe:
            contrasenia = input("Ingrese su contraseña: ")
            if alumno.validar_credenciales(email, contrasenia):
                print(f"Bienvenid@, {alumno_existe._nombre} {alumno_existe._apellido}!")
                while True:
                    print("-- Submenú Alumno --")
                    print("1. Matricularse a un curso")
                    print("2. Ver cursos")
                    print("3. Volver al menú principal")
                    subopcion_alum = int(input("Seleccione una opción: "))
                    if subopcion_alum == 1:
                        print("Aca va funcion de matricular curso") #funcion
                    elif subopcion_alum == 2:
                        print("Aca va funcion de ver curso") #funcion
                    elif subopcion_alum == 3:
                        break
                    else:
                        print("Opcion incorrecta. Ingrese una opción válida (1-3)\n")
            else:
                print("Error! Datos incorrectos")
        else:
            print("No se encuentra registrado. Debe darse de alta en alumnado")

    elif opcion == 2:
        email = input("Ingrese su email: ")
        
        for profe in profesores:
            if email == profe._email:
                profe_existe = profe
                break
            
        if profe_existe:
            contrasenia = input("Ingrese su contraseña: ")
            if profe.validar_credenciales(email, contrasenia):
                print(f"Bienvenid@, {profe_existe._nombre} {profe_existe._apellido}!")
                while True:
                    print("-- Submenú Profesor --")
                    print("1. Dictar un curso")
                    print("2. Ver cursos")
                    print("3. Volver al menú principal")
                    subopcion_profe = int(input("Seleccione una opción: "))
                    if subopcion_profe == 1:
                        print("Aca va funcion de dictar curso") #funcion
                    elif subopcion_profe == 2:
                        print("Aca va funcion de ver curso") #funcion
                    elif subopcion_profe == 3:
                        break
                    else:
                        print("Opcion incorrecta. Ingrese una opción válida (1-3)\n")
            else:
                print("Error! Datos incorrectos.")
        else:
            print("No se encuentra registrado. Debe darse de alta en alumnado")        
            
    elif opcion == 3:
        print("Aca se muestran cursos")

    elif opcion == 4:
        print("Adios!")
        break

    else:
        print("Opción incorrecta. Ingrese una opción válida (1-4)\n")