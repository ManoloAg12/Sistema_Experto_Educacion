# OrientaU · Sistema Experto Educativo

Portal web en Python que orienta a estudiantes universitarios sobre factores que pueden afectar su rendimiento académico. Analiza tiempo, hábitos de estudio, evaluación, entorno y apoyo académico para ofrecer recomendaciones trazables y accionables.

## Finalidad y alcance

OrientaU no etiqueta ni diagnostica condiciones clínicas. Apoya la reflexión académica mediante reglas de conocimiento y alertas preventivas; no sustituye atención psicológica, médica, docente o institucional. Las respuestas se procesan localmente y no se guardan automáticamente.

## Ejecución

Requiere Python 3.10+ y Flask.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python app.py
```

Abre `http://127.0.0.1:5000` en el navegador. Tailwind CSS se carga desde CDN, por lo que la primera carga requiere conexión a internet.

```bash
python3 main.py
```

La versión de consola original continúa disponible.

## Arquitectura

- `app.py`: servidor Flask y recepción/validación del cuestionario.
- `templates/`: portal web con Tailwind CSS y panel de resultados.
- `cuestionario.py`: preguntas y opciones.
- `motor.py`: motor de inferencia de reglas exactas.
- `evaluacion.py`: prioriza reglas y crea alertas preventivas con evidencia.
- `conocimiento/reglas.json`: base de conocimiento editable.
- `tests/test_reglas.py`: pruebas automatizadas.

## Comprobación manual

Inicia el servidor, completa el cuestionario y confirma que se muestran el índice orientativo, las señales, los hallazgos y las recomendaciones. El texto libre solo reconoce algunas menciones explícitas y las reporta como contexto; no cambia el puntaje ni las reglas.
