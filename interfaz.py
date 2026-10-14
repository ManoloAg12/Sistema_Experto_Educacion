# interfaz.py
import os

def limpiar_pantalla():
    """Limpia la terminal para mantener una interfaz pulcra."""
    os.system('cls' if os.name == 'nt' else 'clear')

def hacer_pregunta(pregunta, opciones):
    """
    Despliega una pregunta, enumera las opciones y fuerza al usuario 
    a elegir una opción válida.
    """
    while True:
        print(f"\n{pregunta}")
        for key, value in opciones.items():
            print(f"  {key}. {value['texto']}")
        
        respuesta = input("\nSelecciona el número de tu respuesta: ").strip()
        
        if respuesta in opciones:
            return opciones[respuesta]['valor']
        else:
            print("\n[!] Entrada inválida. Por favor, ingresa un número de la lista.")

def iniciar_entrevista():
    """
    Orquesta la recolección de datos simulando la entrevista con el experto.
    Retorna un diccionario con los hechos listos para el motor de inferencia.
    """
    limpiar_pantalla()
    print("="*60)
    print(" SISTEMA EXPERTO: DIAGNÓSTICO DE RENDIMIENTO ACADÉMICO")
    print("="*60)
    print("Responde las siguientes preguntas con la mayor sinceridad posible.")
    print("Esto nos ayudará a identificar la raíz del problema.\n")

    hechos = {}

    # 1. Factor de Carga Laboral y Tiempo
    hechos["horas_trabajo_semanal"] = hacer_pregunta(
        "¿Cuántas horas a la semana dedicas a un empleo formal o informal?",
        {
            "1": {"texto": "No trabajo", "valor": "0"},
            "2": {"texto": "Medio tiempo (menos de 20 horas)", "valor": "<20"},
            "3": {"texto": "Tiempo parcial alto (20 a 39 horas)", "valor": ">=20"},
            "4": {"texto": "Tiempo completo (40 horas o más)", "valor": ">=40"}
        }
    )

    hechos["horas_sueno"] = hacer_pregunta(
        "En una semana típica de clases, ¿cuántas horas duermes por noche en promedio?",
        {
            "1": {"texto": "Menos de 5 horas", "valor": "<5"},
            "2": {"texto": "Entre 5 y 6 horas", "valor": "5-6"},
            "3": {"texto": "7 horas o más", "valor": ">=7"}
        }
    )

    # 2. Factor Académico y de Entorno
    hechos["horas_estudio_extra"] = hacer_pregunta(
        "¿Cuántas horas a la semana estudias por tu cuenta (fuera de clases)?",
        {
            "1": {"texto": "Menos de 5 horas", "valor": "<5"},
            "2": {"texto": "Entre 5 y 14 horas", "valor": "5-14"},
            "3": {"texto": "15 horas o más", "valor": ">=15"}
        }
    )

    hechos["asistencia_clases"] = hacer_pregunta(
        "¿Cómo describirías tu asistencia a las clases de las materias problemáticas?",
        {
            "1": {"texto": "Alta (Casi nunca falto)", "valor": "alta"},
            "2": {"texto": "Irregular (Falto a veces por cansancio/trabajo)", "valor": "irregular"},
            "3": {"texto": "Baja (Falto frecuentemente)", "valor": "baja"}
        }
    )

    # 3. Factor Metodológico (Enfocado en Informática/Ciencias)
    hechos["tipo_materia_reprobada"] = hacer_pregunta(
        "¿En qué tipo de materia has notado la mayor caída de rendimiento?",
        {
            "1": {"texto": "Teórica (Leyes, Administración, Historia)", "valor": "teorica"},
            "2": {"texto": "Práctica/Lógica (Matemáticas, Algoritmos, Redes)", "valor": "practica_logica"},
            "3": {"texto": "Proyectos de Desarrollo (Backend, Full-stack, Arquitectura)", "valor": "proyectos_desarrollo"}
        }
    )

    hechos["metodo_estudio"] = hacer_pregunta(
        "¿Cuál es tu técnica principal para estudiar para un examen o proyecto?",
        {
            "1": {"texto": "Leer apuntes, diapositivas y memorizar teoría", "valor": "lectura_memorizacion"},
            "2": {"texto": "Práctica activa (escribir código, resolver ejercicios sin ver la respuesta)", "valor": "practica_distribuida"},
            "3": {"texto": "Estudiar intensivamente uno o dos días antes de la entrega/examen", "valor": "estudio_ultima_hora"}
        }
    )

    hechos["comprension_clase"] = hacer_pregunta(
        "Durante la clase, cuando el catedrático explica un tema nuevo, ¿cómo es tu nivel de comprensión?",
        {
            "1": {"texto": "Alta (Entiendo la lógica al momento)", "valor": "alta"},
            "2": {"texto": "Media (Entiendo a medias, me pierdo en detalles)", "valor": "media"},
            "3": {"texto": "Baja (Me siento perdido desde el inicio)", "valor": "baja"}
        }
    )

    print("\n" + "="*60)
    print(" Entrevista finalizada. Procesando diagnóstico...")
    print("="*60 + "\n")
    
    return hechos

if __name__ == "__main__":
    # Prueba unitaria rápida del módulo
    datos_recolectados = iniciar_entrevista()
    print("Hechos generados para motor.py:")
    print(datos_recolectados)