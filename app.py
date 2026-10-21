"""Portal web OrientaU. Ejecutar con: python3 app.py"""
from flask import Flask, render_template, request
from cuestionario import SECCIONES
from evaluacion import evaluar_perfil

app = Flask(__name__)
app.config["SECRET_KEY"] = "orientau-local-session"

NUMERICAS = {clave: datos for _, preguntas in SECCIONES for clave, _, tipo, datos, _ in preguntas if tipo == "numero"}
OPCIONES = {clave: dict(datos) for _, preguntas in SECCIONES for clave, _, tipo, datos, _ in preguntas if tipo == "opcion"}


def analizar_comentario(texto):
    """Busca menciones claras para incorporar contexto, sin inferir estados clínicos."""
    texto = (texto or "").lower()
    patrones = {
        "tiempo y carga": ("no tengo tiempo", "falta de tiempo", "mucho trabajo", "sobrecarga", "trabajo demasiado"),
        "descanso": ("no duermo", "duermo poco", "insomnio", "cansancio", "agotado"),
        "comprensión": ("no entiendo", "no comprendo", "me cuesta entender", "no entiendo nada"),
        "evaluaciones": ("me bloqueo", "nervios en el examen", "ansiedad por examen", "miedo al examen"),
        "apoyo": ("no tengo apoyo", "nadie me ayuda", "no puedo consultar", "no hay tutor"),
        "economía": ("problemas económicos", "falta de dinero", "no puedo pagar", "situación económica"),
        "entorno": ("mucho ruido", "me distraigo", "no tengo un lugar", "ambiente ruidoso"),
    }
    return [area for area, frases in patrones.items() if any(frase in texto for frase in frases)]


def puntuacion_riesgo(hechos):
    """Índice heurístico académico de 0-100; es orientativo, no una probabilidad."""
    puntos = 0
    reglas = [
        (hechos.get("horas_sueno", 8) < 6, 12),
        (hechos.get("horas_trabajo_semanal", 0) >= 30, 10),
        (hechos.get("horas_estudio_extra", 10) < 5, 10),
        (hechos.get("asistencia_clases") in ("irregular", "baja"), 12),
        (hechos.get("comprension_clase") == "baja", 12),
        (hechos.get("dominio_prerrequisitos") == "bajo", 10),
        (hechos.get("entrega_trabajos") in ("tardios", "incompletos_por_tiempo"), 10),
        (hechos.get("nivel_motivacion") == "nula", 8),
        (hechos.get("bloqueo_examenes") == "si", 6),
        (hechos.get("revision_errores") == "nunca", 5),
        (hechos.get("estabilidad_financiera") == "precaria", 5),
    ]
    return min(100, sum(valor for cumple, valor in reglas if cumple))


@app.route("/", methods=["GET", "POST"])
def inicio():
    if request.method == "GET":
        return render_template("inicio.html", secciones=SECCIONES)
    hechos, errores = {}, []
    for clave, (minimo, maximo) in NUMERICAS.items():
        valor = request.form.get(clave, "").strip().replace(",", ".")
        try:
            numero = float(valor)
            if not minimo <= numero <= maximo:
                raise ValueError
            hechos[clave] = int(numero) if numero.is_integer() else numero
        except ValueError:
            errores.append(f"Revisa el valor de «{clave.replace('_', ' ')}» (de {minimo} a {maximo}).")
    for clave, opciones in OPCIONES.items():
        valor = request.form.get(clave, "")
        if valor not in opciones.values():
            errores.append(f"Selecciona una respuesta válida para «{clave.replace('_', ' ')}».")
        else:
            hechos[clave] = valor
    comentario = request.form.get("comentario", "").strip()[:2000]
    if errores:
        return render_template("inicio.html", secciones=SECCIONES, errores=errores, valores=request.form), 400
    resultados = evaluar_perfil(hechos)
    contexto = analizar_comentario(comentario)
    indice = puntuacion_riesgo(hechos)
    nivel = "Atención prioritaria" if indice >= 55 else "Conviene atender algunos factores" if indice >= 30 else "Señales favorables"
    return render_template("resultado.html", resultados=resultados, hechos=hechos,
                           comentario=comentario, contexto=contexto, indice=indice, nivel=nivel)


if __name__ == "__main__":
    app.run(debug=False)
