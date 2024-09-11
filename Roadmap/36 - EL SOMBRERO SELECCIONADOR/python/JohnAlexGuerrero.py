# -*- coding: utf-8 -*-
"""#36-el-sombrero-seleccionador.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FeZc3xRWVqqOFn7EfMpHUBIU0IFGdOFh

* EJERCICIO:
 * Cada 1 de septiembre, el Hogwarts Express parte hacia la escuela
 * de programación de Hogwarts para magos y brujas del código.
 * En ella, su famoso sombrero seleccionador ayuda a los programadores
 * a encontrar su camino...
 * Desarrolla un programa que simule el comportamiento del sombrero.
 * Requisitos:
 * 1. El sombrero realizará 10 preguntas para determinar la casa del alumno.
 * 2. Deben existir 4 casas. Por ejemplo: Frontend, Backend, Mobile y Data.
 *    (Puedes elegir las que quieras)
 * Acciones:
 * 1. Crea un programa que solicite el nombre del alumno y realice 10
 *    preguntas, con cuatro posibles respuestas cada una.
 * 2. Cada respuesta asigna puntos a cada una de las casas (a tu elección).
 * 3. Una vez finalizado, el sombrero indica el nombre del alumno
 *    y a qué casa pertenecerá (resuelve el posible empate de manera aleatoria,
 *    pero indicándole al alumno que la decisión ha sido complicada).
"""

preguntas_respuestas = [

    # Frontend
        {
        "id":1,
        "pregunta": "¿Cuál de los siguientes lenguajes se utiliza comúnmente para diseñar el aspecto visual de una página web?",
        "respuestas": {
            "a": "HTML",
            "b": "Java",
            "c": "CSS",  # Correcta
            "d": "Python"
        } ,
        "correcta": "c",
        "casa":"fronted"
    },
    {
        "id":2,
        "pregunta": "¿Cuál es el propósito principal de JavaScript en el desarrollo web frontend?",
        "respuestas": {
            "a": "Crear gráficos 3D",
            "b": "Añadir interactividad a las páginas web",  # Correcta
            "c": "Definir la estructura de una página",
            "d": "Estilizar la página web"
        },
        "correcta": "b",
        "casa":"fronted"
    },
    {
        "id":3,
        "pregunta": "¿Cuál de los siguientes frameworks es utilizado principalmente para el desarrollo frontend?",
        "respuestas": {
            "a": "Django",
            "b": "Flask",
            "c": "React",  # Correcta
            "d": "PostgreSQL"
        },
        "correcta": "c"
    },
    {
        "id":4,
        "pregunta": "¿Qué propiedad CSS se usa para cambiar el tamaño de un elemento?",
        "respuestas": {
            "a": "color",
            "b": "margin",
            "c": "width",  # Correcta
            "d": "display"
        },
        "correcta": "c",
        "casa":"fronted"
    },

    # Backend
    {
        "id":5,
        "pregunta": "¿Cuál de los siguientes lenguajes es más comúnmente usado para el desarrollo backend?",
        "respuestas": {
            "a": "CSS",
            "b": "JavaScript",
            "c": "Python",  # Correcta
            "d": "HTML"
        },
        "correcta": "c",
        "casa":"backend"
    },
    {
        "id":6,
        "pregunta": "¿Qué es una API en el contexto de desarrollo backend?",
        "respuestas": {
            "a": "Una biblioteca para crear gráficos",
            "b": "Un método de autenticación",
            "c": "Una interfaz para que las aplicaciones se comuniquen",  # Correcta
            "d": "Una base de datos"
        },
        "correcta": "c",
        "casa":"backend"
    },
    {
        "id":7,
        "pregunta": "¿Cuál es un ejemplo de un servidor de aplicaciones backend?",
        "respuestas": {
            "a": "Apache",  # Correcta
            "b": "Bootstrap",
            "c": "React",
            "d": "MySQL"
        },
        "correcta": "a",
        "casa":"backend"
    },
    {
        "id":8,
        "pregunta": "¿Qué tipo de base de datos utiliza SQL?",
        "respuestas": {
            "a": "NoSQL",
            "b": "Relacional",  # Correcta
            "c": "Archivo plano",
            "d": "Jerárquica"
        },
        "correcta": "b",
        "casa":"backend"
    },

    # Data
    {
        "id":9,
        "pregunta": "¿Qué lenguaje es más popular para el análisis de datos?",
        "respuestas": {
            "a": "Java",
            "b": "R",  # Correcta
            "c": "C++",
            "d": "PHP"
        },
        "correcta": "b",
        "casa":"data"
    },
    {
        "id":10,
        "pregunta": "¿Qué biblioteca de Python es ampliamente utilizada para el análisis de datos?",
        "respuestas": {
            "a": "TensorFlow",
            "b": "Django",
            "c": "pandas",  # Correcta
            "d": "Flask"
        },
        "correcta": "c",
        "casa":"data"
    },
    {
        "id":11,
        "pregunta": "¿Qué significa el término 'Big Data'?",
        "respuestas": {
            "a": "Pequeñas cantidades de datos",
            "b": "Un proceso de minería de datos",
            "c": "Conjuntos de datos extremadamente grandes",  # Correcta
            "d": "Una estructura de base de datos"
        },
        "correcta": "c",
        "casa":"data"
    },
    {
        "id":12,
        "pregunta": "¿Cuál es la principal ventaja de una base de datos NoSQL sobre una base de datos relacional?",
        "respuestas": {
            "a": "Soporte para transacciones ACID",
            "b": "Mejor rendimiento en grandes cantidades de datos no estructurados",  # Correcta
            "c": "Mayor seguridad",
            "d": "Compatibilidad con SQL"
        },
        "correcta": "b",
        "casa":"data"
    },

    # Mobile
    {
        "id":13,
        "pregunta": "¿Qué lenguaje es usado principalmente para el desarrollo nativo de aplicaciones Android?",
        "respuestas": {
            "a": "Swift",
            "b": "Kotlin",  # Correcta
            "c": "JavaScript",
            "d": "C#"
        },
        "correcta": "b",
        "casa":"mobile"
    },
    {
        "id":14,
        "pregunta": "¿Qué lenguaje se utiliza para desarrollar aplicaciones nativas de iOS?",
        "respuestas": {
            "a": "Java",
            "b": "Python",
            "c": "Swift",  # Correcta
            "d": "Ruby"
        },
        "correcta": "c",
        "casa":"mobile"
    },
    {
        "id":15,
        "pregunta": "¿Cuál de las siguientes plataformas permite el desarrollo de aplicaciones móviles multiplataforma?",
        "respuestas": {
            "a": "Xcode",
            "b": "Android Studio",
            "c": "Flutter",  # Correcta
            "d": "Jupyter Notebook"
        },
        "correcta": "c",
        "casa":"mobile"
    }
]

import math
import random

#alumno candidato para ingresar a la escuela de programacion de Hogwarts
class Alumno:

  def __init__(self, nombre):
    self.nombre = nombre

#sombrero que realiza un test para asignar a un alumno a una casa de programacion en Hogwarts
class Sombrero:

  def __init__(self, alumno, preguntas):
    self.alumno = alumno
    self.preguntas = preguntas
    self.puntuacion = {
        "fronted": 0,
        "backend": 0,
        "mobile": 0,
        "data": 0
    }
    self.escuelas = [
          {
            "casa":"fronted",
            "alumnos":[],
          },
          {
          "casa":"backend",
          "alumnos":[],
          },
          {
          "casa":"mobile",
          "alumnos":[]
          },
          {
          "casa":"data",
          "alumnos":[]
          }
        ]

  def test(self):
    pass

  def seleccionar_pregunta(self):
    index_pregunta = random.randint(1, len(self.preguntas))
    res = self.preguntas[index_pregunta - 1]
    return res

  def adicionar_punto_casa(self, nombre_casa):
    self.puntuacion[nombre_casa] += 1

  def restar_punto_casa(self, nombre_casa):
    if self.puntuacion[nombre_casa] == 0:
      return
    self.puntuacion[nombre_casa] -= 1

  def mostrar_puntuacion(self):
    return self.puntuacion

  def asignar_casa_ganadora(self):
    casa = [(k, v) for k, v in self.puntuacion.items() if v > 2]
    print(casa)
    #return casa

candidatos = ['Juan Gabriel','Peter Ortiz','John Guerrero']

for name in candidatos:
  total_preguntas = 0
  print('Bienvenido a la Escuela de Programación de Hagwarts\n')
  print('cual es tu nombre?: ')
  print(f'hola, {name}')

  al = Alumno(name)
  s = Sombrero(al, preguntas_respuestas)

  while total_preguntas <= 10:
    total_preguntas += 1
    pregunta = s.seleccionar_pregunta()

    print(f'N. pregunta: {total_preguntas}')
    nombre_casa = pregunta["casa"]
    print(pregunta["pregunta"])
    print('='*len(pregunta['pregunta']))

    print('RESPUESTAS: \n')
    for key, value in pregunta['respuestas'].items():
      print(f'{key}: {value}')

    respuesta = str(input('Cual es la respuesta? '))
    if respuesta == pregunta['correcta']:
      print("Respuesta correcta")
      s.adicionar_punto_casa(nombre_casa)
    elif respuesta != pregunta['correcta']:
      print("Respuesta incorrecta")
      s.restar_punto_casa(nombre_casa)

    print(s.mostrar_puntuacion())
    print(s.asignar_casa_ganadora())
    print('='*50)