"""Capa de priorización: conserva reglas exactas y añade alertas preventivas."""
from motor import MotorInferencia


FACTORES = [
    ("Gestion del tiempo", "Carga de tiempo elevada", "alto",
     {"horas_trabajo_semanal": lambda v: v >= 30, "horas_sueno": lambda v: v < 6},
     "Protege el descanso y revisa si la carga académica y laboral es sostenible.",
     ["Define bloques fijos de estudio de 45 minutos.", "Evita sacrificar el sueño para completar tareas.", "Consulta opciones de horario, beca o carga académica."]),
    ("Metodos de estudio", "Método poco activo para una materia práctica", "medio",
     {"metodo_estudio": lambda v: v in ("lectura_memorizacion", "estudio_ultima_hora"),
      "tipo_materia_reprobada": lambda v: v in ("matematicas", "programacion", "practica_logica")},
     "En materias prácticas, comprender no basta: hay que recuperar y aplicar sin apoyo.",
     ["Practica ejercicios o código desde cero.", "Registra y corrige tus errores.", "Haz una autoevaluación corta al final de cada sesión."]),
    ("Evaluacion y habitos", "Riesgo en evaluaciones", "medio",
     {"bloqueo_examenes": lambda v: v == "si", "horas_estudio_extra": lambda v: v >= 5},
     "Hay señales de que el desempeño en examen no refleja completamente tu preparación.",
     ["Realiza simulacros con cronómetro.", "Practica recuperación activa sin apuntes.", "Consulta al docente por ejemplos de evaluación."]),
    ("Entorno y apoyo", "Barreras de entorno o apoyo", "medio",
     {"entorno_estudio": lambda v: v != "tranquilo", "consulta_dudas": lambda v: v in ("ocasional", "nunca")},
     "El ambiente y la falta de consulta pueden estar reduciendo la calidad del estudio.",
     ["Reserva un lugar y horario con menos interrupciones.", "Formula una duda concreta por cada tema difícil.", "Busca tutoría, docente o compañero de estudio."]),
]


def _nivel(coincidencias, total, nivel_base):
    if coincidencias == total and nivel_base == "alto":
        return "Alto"
    if coincidencias == total:
        return "Medio"
    return "Preventivo"


def evaluar_perfil(hechos):
    """Devuelve resultados trazables, ordenados por severidad y sin diagnosticar clínicamente."""
    exactos = MotorInferencia().evaluar(hechos)
    resultados = []
    for regla in exactos:
        resultados.append({
            "titulo": regla["nombre"], "area": regla.get("cluster", "General"), "nivel": "Alto",
            "tipo": "Regla experta", "conclusion": regla["conclusion"],
            "recomendacion": regla["recomendacion"], "acciones": [],
            "evidencia": list(regla["condiciones_evaluadas"].keys()), "id": regla["id_regla"],
        })

    areas_exactas = {resultado["area"] for resultado in resultados}
    for area, titulo, nivel_base, condiciones, conclusion, acciones in FACTORES:
        cumplidas = [campo for campo, criterio in condiciones.items() if campo in hechos and criterio(hechos[campo])]
        if len(cumplidas) >= 2 and area not in areas_exactas:
            resultados.append({
                "titulo": titulo, "area": area, "nivel": _nivel(len(cumplidas), len(condiciones), nivel_base),
                "tipo": "Alerta preventiva", "conclusion": conclusion,
                "recomendacion": "Prioriza las acciones sugeridas y vuelve a evaluar tu progreso en dos semanas.",
                "acciones": acciones, "evidencia": cumplidas, "id": None,
            })
    orden = {"Alto": 0, "Medio": 1, "Preventivo": 2}
    return sorted(resultados, key=lambda r: orden[r["nivel"]])
