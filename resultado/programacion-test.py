class Alumnos:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def estudiante(self):
        return "Nombre del estudiante es: " +self.nombre
        
class Curso(Alumnos):
    def __init__(self,nombre, curso):
        self.curso = curso
        super().__init__(nombre)
    
    def asignatura(self):
      return "El curso de "+self.nombre+" es: "+self.curso

class Profesor(Curso):
    def __init__(self,nombre,curso,maestro) :
        self.maestro = maestro
        super().__init__(nombre,curso)
                
    def instructor(self):
      return "El nombre del profesor es: " +self.maestro

if __name__== '__main__':
    alumno = Alumnos("Pedro")
    print(alumno.estudiante())
    print("\nLista de Estudiantes: ")
    for i in ["Laura","Frank","Raul"]:
      alumno = Alumnos(i)
      print(alumno.estudiante())
    print("\n")
    curso = Curso("Pedro","Math")
    print(curso.estudiante())
    print(curso.asignatura())
    print("\nLista de Estudiantes y cursos")
    dictionary  =	{
    "Laura": "Math",
    "Frank": "Historia",
    "Raul": "Geografia",
    "Carlos":"Quimica",
    }
    for key,value in dictionary.items():
      alumno = Alumnos(key)
      print(alumno.estudiante())
      curso_dual = Curso(key,value)
      print(curso_dual.asignatura())

    print("\nDatos Profesor: ")   
    profe = Profesor("Pedro","Math","Tadeo")
    
    print(profe.instructor())
    print("\nDatos de la Clase: ") 
    datos_clase = Profesor("Julian","Castellano","Pietro")
    print(datos_clase.instructor())
    print(datos_clase.estudiante())
    print(datos_clase.asignatura())

    
