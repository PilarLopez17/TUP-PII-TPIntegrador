from abc import ABC, abstractmethod
from generador_contra import generar
from datetime import date

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
            contrasenia_ingresada = input(f"Ingrese la contraseña de matriculación del curso {curso._nombre}: ")
            if contrasenia_ingresada == curso._contrasenia_matriculacion:
                self._cursos.append(curso)
                print(f"Matriculado con éxito en el curso {curso._nombre}.")
            else:
                print("Error! Contraseña de matriculación incorrecta.")
        else:
            print(f"Error! Ya está matriculado en el curso '{curso._nombre}'.")
    
    def desmatricular_del_curso(self, curso):
        if curso in self._cursos:
            self._cursos.remove(curso)
            print(f"Desmatriculado con éxito del curso {curso._nombre}.")
        else:
            print(f"No estás matriculado en el curso {curso._nombre}. No se puede desmatricular.")


class Profesor(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia, titulo, anio_egreso):
        super().__init__(nombre, apellido, email, contrasenia)
        self._titulo = titulo
        self._anio_egreso = anio_egreso
        self._cursos = []

    def dictar_curso(self, curso):
        if curso not in self._cursos:
            self._cursos.append(curso)
            print(f"\nAhora dictas el curso: {curso._nombre}\n")
        else:
            print("Error! Ya estás dictando ese curso.")

    def __str__(self):
        return super().__str__() + f"\n- Titulo: {self._titulo}\n- Año de egreso: {self._anio_egreso}"


class Curso:
    prox_cod = 0
    
    def __init__(self, nombre):
        self._nombre = nombre
        self._contrasenia_matriculacion = generar(self)  #funcion extraida del tp anterior
        Curso.prox_cod += 1
        self.archivos = []
    
    def __str__(self):
        return f"- Curso: {self._nombre}\n- Contraseña: {self._contrasenia_matriculacion}"

    def nuevo_archivo(self, archivo):
        self.archivos.append(archivo)
    

class Carrera():
    def __init__(self, nombre, cant_anios):
        self._nombre = nombre
        self._cant_anios = cant_anios
    
    def __str__(self) -> str:
        return f"- Nombre: {self._nombre} \n- Cantidad de años: {self._cant_anios}"
    
    def get_cantidad_materias(self):
        pass

class Archivo():

    def __init__(self, nombre, formato):
        self._nombre = nombre
        self._fecha_hoy = date.today()
        self._formato = formato

    def __str__(self) -> str:
        return f"- Nombre: {self._nombre} \n- Fecha: {self._fecha_hoy} \n- Formato: {self._formato}"
    

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

# Funciones submenú


def op1_alumno(alumno):
    if not mis_cursos:
        print("\nNo hay ningun curso\n")
    else:
        print("\nTodos los cursos:")
       
        for i, curso in enumerate(mis_cursos.values(), 1):
            print(f"{i}. {curso._nombre}")

        op_curso = int(input("\nIngrese número de curso al que desea matricularse:\n"))

        while op_curso < 1 or op_curso > len(mis_cursos):
            op_curso = int(input("Error! Ingrese un número de curso válido:\n"))
        
        curso_seleccionado = list(mis_cursos.values())[op_curso - 1]#se resta 1 porque la lista empieza en 0

        alumno.matricular_en_curso(curso_seleccionado)

def op2_alumno(alumno):
    if not alumno._cursos:
        print("\nNo se encuentra matriculado en ningun curso.\n")
    else:
        print("\nTe encuentras matriculado en los siguientes cursos:")
        for i, curso in enumerate(alumno_existe._cursos, 1):
            print(f"{i}. {curso._nombre}")

        opcion_desmatricular = int(input("Ingrese número de curso del que desea desmatricularse: "))

        while opcion_desmatricular < 1 or opcion_desmatricular > len(alumno_existe._cursos):
            opcion_desmatricular = int(input("\nError! Ingrese un número de curso válido:\n"))

        seleccionado_desmatricular = alumno_existe._cursos[opcion_desmatricular - 1]
        alumno_existe.desmatricular_del_curso(seleccionado_desmatricular)       
            
def op3_alumno(alumno):
    if not alumno._cursos:
        print("\nNo se encuentra matriculado en ningun curso.\n")
    else:
        print("\nTe encontras matriculado en los siguientes cursos:")
        for i, curso in enumerate(alumno._cursos, 1):
            print(f"{i}. {curso._nombre}")

        opcion_ver_alum = int(input("Ingrese numero de curso que desea ver los archivos: "))

        while opcion_ver_alum < 1 or opcion_ver_alum > len(alumno._cursos):
            opcion_ver_alum = int(input("\nError! Ingrese un número de curso válido:\n"))
        
        seleccionado_ver_alum = alumno._cursos[opcion_ver_alum - 1]
        print(f"\nNombre: {seleccionado_ver_alum._nombre.title()}")
        
        if len(seleccionado_ver_alum.archivos) == 0:
            print("No hay archivos en este curso.")
        else:
            print("Archivos disponibles:\n")
            for archivo in seleccionado_ver_alum.archivos:
                 print(f"Archivo: {archivo._nombre}.{archivo._formato}, Fecha: {archivo._fecha_hoy}")

def op1_profe(profe, mis_cursos):
    nombre_curso = input("\nIngrese el nombre del curso: ")
    if nombre_curso not in mis_cursos:
        curso = Curso(nombre_curso)
        profe.dictar_curso(curso)
        mis_cursos[nombre_curso] = curso
        print(f"Nombre: {nombre_curso}\nContraseña: {curso._contrasenia_matriculacion}")
    else:
        print("Error! Ya existe un curso con ese nombre.")
    
def op2_profe(profe):
    if not profe._cursos:
        print("\nNo tenes cursos registrados.\n")
    else:
        print("\nTus cursos son:")
        for i, curso in enumerate(profe._cursos, 1):
            print(f"{i}. {curso._nombre}")

        opcion_ver_profe = int(input("Ingrese numero de curso que desea ver: "))

        while opcion_ver_profe < 1 or opcion_ver_profe > len(profe._cursos):
            opcion_ver_profe = int(input("\nError! Ingrese un número de curso válido:\n"))
        
        seleccionado_ver_profe = profe._cursos[opcion_ver_profe - 1]
        print(f"\nNombre: {seleccionado_ver_profe._nombre.title()}")
        print(f"Código: {seleccionado_ver_profe.prox_cod}") 
        print(f"Contraseña: {seleccionado_ver_profe._contrasenia_matriculacion}")
        print(f"Cantidad de archivos: {len(seleccionado_ver_profe.archivos)}")

        if seleccionado_ver_profe.archivos:
            print("Archivos adjuntos:")
            for i, archivo in enumerate(seleccionado_ver_profe.archivos, 1):
                print(f"{i}. {archivo._nombre}.{archivo._formato} (fecha: {archivo._fecha_hoy})")
        else:
            print("No hay archivos en este curso.")

        agregar_archivos = input("¿Desea agregar un archivo adjunto? (Si/No): ").lower()
        if agregar_archivos == "si":
            while True:
                nombre_archivo = input("Ingrese el nombre del archivo: ")
                formato_archivo = input("Ingrese el formato del archivo: ")
                archivo = Archivo(nombre_archivo, formato_archivo)
                seleccionado_ver_profe.nuevo_archivo(archivo)
                print("Archivo adjunto agregado con éxito.")

                continuar = input("¿Desea agregar otro archivo adjunto? (Si/No): ").lower()
                if continuar != "si":
                    break


# Menu principal
while True:
    print("\n-- Menú Principal --\n")
    print("1. Ingresar cómo alumno")
    print("2. Ingresar cómo profesor")
    print("3. Ver cursos")
    print("4. Salir")

    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        email = input("Ingrese su email: ")
        
        alumno_existe = None

        for alumno in alumnos:
            if email == alumno._email:
                alumno_existe = alumno
                break

        if alumno_existe:
            contrasenia = input("Ingrese su contraseña: ")
            if alumno.validar_credenciales(email, contrasenia):
                print(f"\nBienvenid@, {alumno_existe._nombre} {alumno_existe._apellido}!\n")
                while True:
                    print("\n-- Submenú Alumno --\n")
                    print("1. Matricularse a un curso")
                    print("2. Desmatricularse a un curso")                    
                    print("3. Ver cursos")
                    print("4. Volver al menú principal")
                    subopcion_alum = int(input("Seleccione una opción: "))
                    if subopcion_alum == 1:
                        op1_alumno(alumno)
                    elif subopcion_alum == 2:
                        op2_alumno(alumno)
                    elif subopcion_alum == 3:
                        op3_alumno(alumno)
                    elif subopcion_alum == 4:
                        break
                    else:
                        print("Opcion incorrecta. Ingrese una opción válida (1-3)\n")
            else:
                print("Error! Datos incorrectos")
        else:
            print("No se encuentra registrado. Debe darse de alta en alumnado")

    elif opcion == 2:
        email = input("Ingrese su email: ")
        
        profe_existe = None

        for profe in profesores:
            if email == profe._email:
                profe_existe = profe
                break

        if profe_existe:
            contrasenia = input("Ingrese su contraseña: ")
            if profe.validar_credenciales(email, contrasenia):
                print(f"\nBienvenid@, {profe_existe._nombre} {profe_existe._apellido}!\n")
                while True:
                    print("\n-- Submenú Profesor --\n")
                    print("1. Dictar un curso")
                    print("2. Ver cursos")
                    print("3. Volver al menú principal")
                    subopcion_profe = int(input("Seleccione una opción: "))
                    if subopcion_profe == 1:
                        op1_profe(profe, mis_cursos)
                    elif subopcion_profe == 2:
                        op2_profe(profe)
                    elif subopcion_profe == 3:
                        break
                    else:
                        print("\nOpcion incorrecta. Ingrese una opción válida (1-3)")
            else:
                print("Error! Datos incorrectos.")
        else:
            print("No se encuentra registrado. Debe darse de alta en alumnado")        
            
    elif opcion == 3:
        if not mis_cursos:
            print("\nNo hay cursos\n")
        else:
            print("\nCursos disponibles (ordenados alfabéticamente):")
            sorted_cursos = sorted(mis_cursos.values(), key=lambda curso: curso._nombre)
            for curso in sorted_cursos:
                print(f"Materia: {curso._nombre} - Carrera: Tecnicatura Universitaria en Programación")
                    
    elif opcion == 4:
        print("Adios!")
        break

    else:
        print("Opción incorrecta. Ingrese una opción válida (1-4)\n")