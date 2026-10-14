# interfaz.py
import os
from motor import MotorInferencia


def limpiar_pantalla():
    """Limpia la terminal."""
    os.system("cls" if os.name == "nt" else "clear")


def hacer_pregunta(pregunta, opciones):
    """Valida la selección y devuelve el valor correspondiente."""
    while True:
        print(f"\n{pregunta}")

        for numero, opcion in opciones.items():
            print(f"  {numero}. {opcion['texto']}")

        respuesta = input("\nSelecciona una opción: ").strip()

        if respuesta in opciones:
            return opciones[respuesta]["valor"]

        print("[!] Selecciona un número válido.")


def iniciar_entrevista():
    """Recopila los hechos utilizados por el motor de inferencia."""
    limpiar_pantalla()

    print("=" * 60)
    print(" SISTEMA EXPERTO: DIAGNÓSTICO ACADÉMICO")
    print("=" * 60)
    print("Responde según tu situación actual.\n")

    hechos = {}

    # Tiempo y responsabilidades
    hechos["horas_trabajo_semanal"] = hacer_pregunta(
        "¿Cuántas horas trabajas por semana?",
        {
            "1": {"texto": "No trabajo", "valor": 0},
            "2": {"texto": "Menos de 20 horas", "valor": 15},
            "3": {"texto": "Entre 20 y 39 horas", "valor": 30},
            "4": {"texto": "40 horas o más", "valor": 40}
        }
    )

    hechos["horas_sueno"] = hacer_pregunta(
        "¿Cuántas horas duermes por noche en promedio?",
        {
            "1": {"texto": "Menos de 5 horas", "valor": 4},
            "2": {"texto": "Entre 5 y 6 horas", "valor": 5.5},
            "3": {"texto": "7 horas o más", "valor": 7}
        }
    )

    hechos["tiempo_transporte"] = hacer_pregunta(
        "¿Cuánto tiempo total dedicas al transporte en un día de clases?",
        {
            "1": {"texto": "Hasta 1 hora", "valor": 1},
            "2": {"texto": "Más de 1 y hasta 2 horas", "valor": 2},
            "3": {"texto": "Más de 2 y hasta 3 horas", "valor": 2.5},
            "4": {"texto": "Más de 3 horas", "valor": 4}
        }
    )

    hechos["horas_estudio_extra"] = hacer_pregunta(
        "¿Cuántas horas estudias por tu cuenta a la semana?",
        {
            "1": {"texto": "Menos de 5 horas", "valor": 3},
            "2": {"texto": "Entre 5 y 14 horas", "valor": 10},
            "3": {"texto": "15 horas o más", "valor": 16}
        }
    )

    hechos["asistencia_clases"] = hacer_pregunta(
        "¿Cómo es tu asistencia a las clases problemáticas?",
        {
            "1": {"texto": "Alta", "valor": "alta"},
            "2": {"texto": "Irregular", "valor": "irregular"},
            "3": {"texto": "Baja", "valor": "baja"}
        }
    )

    # Dificultades académicas
    hechos["tipo_materia_reprobada"] = hacer_pregunta(
        "¿En qué tipo de materia tienes mayores dificultades?",
        {
            "1": {"texto": "Matemáticas", "valor": "matematicas"},
            "2": {"texto": "Programación", "valor": "programacion"},
            "3": {"texto": "Proyectos de desarrollo", "valor": "proyectos_desarrollo"},
            "4": {"texto": "Materias teóricas", "valor": "teorica"},
            "5": {"texto": "Otra materia práctica o lógica", "valor": "practica_logica"}
        }
    )

    hechos["metodo_estudio"] = hacer_pregunta(
        "¿Cuál es tu método principal de estudio?",
        {
            "1": {"texto": "Leer y memorizar", "valor": "lectura_memorizacion"},
            "2": {"texto": "Practicar ejercicios o código", "valor": "practica_distribuida"},
            "3": {"texto": "Estudiar a última hora", "valor": "estudio_ultima_hora"}
        }
    )

    hechos["comprension_clase"] = hacer_pregunta(
        "¿Cómo comprendes los temas explicados en clase?",
        {
            "1": {"texto": "Alta", "valor": "alta"},
            "2": {"texto": "Media", "valor": "media"},
            "3": {"texto": "Baja", "valor": "baja"}
        }
    )

    hechos["dominio_prerrequisitos"] = hacer_pregunta(
        "¿Dominas los conocimientos previos necesarios?",
        {
            "1": {"texto": "Sí, los domino", "valor": "alto"},
            "2": {"texto": "Parcialmente", "valor": "medio"},
            "3": {"texto": "Tengo dificultades", "valor": "bajo"}
        }
    )

    hechos["revision_errores"] = hacer_pregunta(
        "¿Con qué frecuencia revisas los errores de exámenes y tareas?",
        {
            "1": {"texto": "Siempre", "valor": "siempre"},
            "2": {"texto": "A veces", "valor": "a_veces"},
            "3": {"texto": "Nunca", "valor": "nunca"}
        }
    )

    hechos["bloqueo_examenes"] = hacer_pregunta(
        "¿Te bloqueas durante los exámenes aunque hayas estudiado?",
        {
            "1": {"texto": "Sí", "valor": "si"},
            "2": {"texto": "No", "valor": "no"}
        }
    )

    hechos["entrega_trabajos"] = hacer_pregunta(
        "¿Cómo sueles entregar tus trabajos?",
        {
            "1": {"texto": "A tiempo", "valor": "a_tiempo"},
            "2": {"texto": "Tarde", "valor": "tardios"},
            "3": {"texto": "Incompletos por falta de tiempo", "valor": "incompletos_por_tiempo"}
        }
    )

    hechos["uso_herramientas_ia"] = hacer_pregunta(
        "¿Cuánto dependes de herramientas de IA para resolver tareas?",
        {
            "1": {"texto": "Poco", "valor": "bajo"},
            "2": {"texto": "Moderadamente", "valor": "medio"},
            "3": {"texto": "Mucho; frecuentemente resuelven por mí", "valor": "alto"}
        }
    )

    # Hábitos y entorno
    hechos["entorno_estudio"] = hacer_pregunta(
        "¿Dónde estudias habitualmente?",
        {
            "1": {"texto": "Lugar tranquilo y organizado", "valor": "tranquilo"},
            "2": {"texto": "Lugar ruidoso o compartido", "valor": "ruidoso_o_compartido"},
            "3": {"texto": "Cama o habitación donde me distraigo", "valor": "cama_o_habitacion"}
        }
    )

    hechos["consulta_dudas"] = hacer_pregunta(
        "¿Qué haces cuando no comprendes un tema?",
        {
            "1": {"texto": "Consulto al docente o compañeros", "valor": "frecuente"},
            "2": {"texto": "Busco ayuda algunas veces", "valor": "ocasional"},
            "3": {"texto": "Nunca consulto", "valor": "nunca"}
        }
    )

    hechos["trabajo_equipo"] = hacer_pregunta(
        "¿Cómo describirías tu experiencia en trabajos grupales?",
        {
            "1": {"texto": "Distribuimos las tareas", "valor": "equilibrado"},
            "2": {"texto": "Asumo casi toda la carga", "valor": "asume_toda_carga"},
            "3": {"texto": "Tenemos conflictos frecuentes", "valor": "conflictivo"}
        }
    )

    hechos["nivel_motivacion"] = hacer_pregunta(
        "¿Cómo describirías tu motivación académica?",
        {
            "1": {"texto": "Alta", "valor": "alta"},
            "2": {"texto": "Media", "valor": "media"},
            "3": {"texto": "Muy baja o nula", "valor": "nula"}
        }
    )

    hechos["estabilidad_financiera"] = hacer_pregunta(
        "¿Cómo describirías tu situación económica para continuar estudiando?",
        {
            "1": {"texto": "Estable", "valor": "estable"},
            "2": {"texto": "Ajustada", "valor": "ajustada"},
            "3": {"texto": "Precaria; dificulta cubrir gastos", "valor": "precaria"}
        }
    )

    print("\n" + "=" * 60)
    print(" ENTREVISTA FINALIZADA")
    print("=" * 60)

    return hechos


def mostrar_resultados(hechos, resultados):
    """Muestra las respuestas y los resultados de la inferencia."""
    print("\n" + "=" * 60)
    print(" RESULTADOS DEL DIAGNÓSTICO ACADÉMICO")
    print("=" * 60)

    print(f"\nReglas activadas: {len(resultados)}")

    if resultados:
        for resultado in resultados:
            print("\n" + "-" * 60)
            print(f"Regla: {resultado['id_regla']}")
            print(f"Área identificada: {resultado['nombre']}")
            print(f"Resultado: {resultado['conclusion']}")
            print(f"Recomendación: {resultado['recomendacion']}")
    else:
        print("\nNo se activaron reglas con las respuestas proporcionadas.")
        print("Esto no significa que no existan dificultades académicas.")
        print("Revisa si es necesario ampliar o ajustar las reglas.")

    print("\n" + "=" * 60)
    print("Evaluación finalizada.")
    print("=" * 60)


if __name__ == "__main__":
    try:
        datos = iniciar_entrevista()

        # Envía las respuestas al motor de inferencia.
        motor = MotorInferencia()
        resultados = motor.evaluar(datos)

        mostrar_resultados(datos, resultados)

    except (FileNotFoundError, ValueError, TypeError) as error:
        print(f"\n[ERROR] {error}")
        print("Verifica el archivo motor.py y la base conocimiento/reglas.json.")
    except KeyboardInterrupt:
        print("\n\nEntrevista cancelada por el usuario.")