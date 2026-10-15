# OrientaU · Sistema Experto Educativo

Aplicación de escritorio en Python que orienta a estudiantes universitarios sobre factores que pueden afectar su rendimiento académico. Analiza tiempo, hábitos de estudio, evaluación, entorno y apoyo académico para ofrecer recomendaciones trazables y accionables.

## Finalidad y alcance

OrientaU no etiqueta ni diagnostica condiciones clínicas. Apoya la reflexión académica mediante reglas de conocimiento y alertas preventivas; no sustituye atención psicológica, médica, docente o institucional. Las respuestas se procesan localmente y no se guardan automáticamente.

## Ejecución

Requiere Python 3.10+ con soporte para Tk/Tcl (en Linux suele ser el paquete `python3-tk`).

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python app.py
```

En macOS, si el Python actual indica que falta `_tkinter`, instala una distribución de Python que incluya Tcl/Tk o el paquete de Tk correspondiente antes de ejecutar la aplicación.

```bash
python3 main.py
```

La versión de consola original continúa disponible y no requiere CustomTkinter.

## Arquitectura

- `app.py`: interfaz de escritorio en CustomTkinter.
- `cuestionario.py`: preguntas y opciones.
- `motor.py`: motor de inferencia de reglas exactas.
- `evaluacion.py`: prioriza reglas y crea alertas preventivas con evidencia.
- `conocimiento/reglas.json`: base de conocimiento editable.
- `tests/test_reglas.py`: pruebas automatizadas.

## Pruebas

```bash
python3 -m unittest discover -s tests -v
```
