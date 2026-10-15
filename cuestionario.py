"""Definición única de las preguntas empleadas por consola y escritorio."""

SECCIONES = [
    ("Contexto y tiempo", [
        ("horas_trabajo_semanal", "Horas de trabajo a la semana", "numero", (0, 100),
         "Escribe 0 si no trabajas."),
        ("horas_sueno", "Horas que duermes por noche", "numero", (0, 24),
         "Usa un promedio, por ejemplo: 6.5."),
        ("tiempo_transporte", "Horas de transporte en un día de clases", "numero", (0, 12),
         "Considera ida y vuelta."),
        ("horas_estudio_extra", "Horas de estudio independiente por semana", "numero", (0, 100),
         "No incluyas las horas de clase."),
        ("estabilidad_financiera", "Situación económica para continuar estudiando", "opcion",
         [("Estable", "estable"), ("Ajustada", "ajustada"), ("Precaria; dificulta cubrir gastos", "precaria")], ""),
    ]),
    ("Aprendizaje", [
        ("tipo_materia_reprobada", "Área en la que tienes mayor dificultad", "opcion",
         [("Matemáticas", "matematicas"), ("Programación", "programacion"),
          ("Proyectos de desarrollo", "proyectos_desarrollo"), ("Materias teóricas", "teorica"),
          ("Otra materia práctica o lógica", "practica_logica")], ""),
        ("metodo_estudio", "Método principal de estudio", "opcion",
         [("Leer y memorizar", "lectura_memorizacion"), ("Practicar ejercicios o código", "practica_distribuida"),
          ("Estudiar a última hora", "estudio_ultima_hora")], ""),
        ("comprension_clase", "Comprensión de los temas explicados en clase", "opcion",
         [("Alta", "alta"), ("Media", "media"), ("Baja", "baja")], ""),
        ("dominio_prerrequisitos", "Dominio de los conocimientos previos", "opcion",
         [("Los domino", "alto"), ("Parcialmente", "medio"), ("Tengo dificultades", "bajo")], ""),
        ("revision_errores", "Frecuencia con que revisas errores de tareas o exámenes", "opcion",
         [("Siempre", "siempre"), ("A veces", "a_veces"), ("Nunca", "nunca")], ""),
    ]),
    ("Evaluación y hábitos", [
        ("asistencia_clases", "Asistencia a las clases problemáticas", "opcion",
         [("Alta", "alta"), ("Irregular", "irregular"), ("Baja", "baja")], ""),
        ("bloqueo_examenes", "¿Te bloqueas durante los exámenes aunque hayas estudiado?", "opcion",
         [("Sí", "si"), ("No", "no")], ""),
        ("entrega_trabajos", "Cómo sueles entregar tus trabajos", "opcion",
         [("A tiempo", "a_tiempo"), ("Tarde", "tardios"),
          ("Incompletos por falta de tiempo", "incompletos_por_tiempo")], ""),
        ("uso_herramientas_ia", "Dependencia de IA para resolver tareas", "opcion",
         [("Poca", "bajo"), ("Moderada", "medio"), ("Mucha; suele resolver por mí", "alto")], ""),
        ("nivel_motivacion", "Motivación académica actual", "opcion",
         [("Alta", "alta"), ("Media", "media"), ("Muy baja o nula", "nula")], ""),
    ]),
    ("Entorno y apoyo", [
        ("entorno_estudio", "Lugar donde estudias habitualmente", "opcion",
         [("Lugar tranquilo y organizado", "tranquilo"), ("Lugar ruidoso o compartido", "ruidoso_o_compartido"),
          ("Cama o habitación donde me distraigo", "cama_o_habitacion")], ""),
        ("consulta_dudas", "Qué haces cuando no comprendes un tema", "opcion",
         [("Consulto a docente o compañeros", "frecuente"), ("Busco ayuda algunas veces", "ocasional"),
          ("Nunca consulto", "nunca")], ""),
        ("trabajo_equipo", "Experiencia en trabajos grupales", "opcion",
         [("Distribuimos las tareas", "equilibrado"), ("Asumo casi toda la carga", "asume_toda_carga"),
          ("Tenemos conflictos frecuentes", "conflictivo")], ""),
    ]),
]


def todas_las_preguntas():
    return [pregunta for _, preguntas in SECCIONES for pregunta in preguntas]
