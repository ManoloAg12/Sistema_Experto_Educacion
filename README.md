# OrientaU · Sistema Experto Educativo
# Presentado por: Manolo Herminio Vargas Aguilar
Portal web en Python que orienta a estudiantes universitarios sobre factores que pueden afectar su rendimiento académico. Analiza tiempo, hábitos de estudio, evaluación, entorno y apoyo académico para ofrecer recomendaciones trazables y accionables.

## Finalidad y alcance

OrientaU no etiqueta ni diagnostica condiciones clínicas. Apoya la reflexión académica mediante reglas de conocimiento y alertas preventivas; no sustituye atención psicológica, médica, docente o institucional. Las respuestas se procesan localmente y no se guardan automáticamente.

## Reglas nuevas
    {
      "id": "R09_A",
      "cluster": "Interés",
      "nombre": "Falta de interés por no saber para qué sirve lo que estudia",
      "certeza": 0.85,
      "si": {
        "nivel_interes": "bajo",
        "relevancia_percibida": "nula",
        "nivel_motivacion": "baja"
      },
      "entonces": {
        "conclusion": "El estudiante muestra una falta de interés profunda que deriva de no encontrarle aplicación práctica o utilidad a la materia, lo que reduce drásticamente su motivación general.",
        "recomendacion": "Investigar aplicaciones reales o del ámbito laboral donde se utilicen los conceptos de la materia. Consultar con el docente o profesionales sobre cómo esta asignatura impacta en el ejercicio de la carrera."
      }
    },
    {
      "id": "R09_B",
      "cluster": "Interés",
      "nombre": "Desinterés por monotonía en los métodos de aprendizaje",
      "certeza": 0.80,
      "si": {
        "nivel_interes": "bajo",
        "asistencia_clases": "irregular",
        "metodo_estudio": "lectura_memorizacion"
      },
      "entonces": {
        "conclusion": "La combinación de métodos de estudio pasivos y una asistencia irregular reflejan un desinterés que puede estar fuertemente ligado a la monotonía del proceso de aprendizaje.",
        "recomendacion": "Explorar formatos de aprendizaje más dinámicos, como videos, simuladores, o el desarrollo de proyectos personales que conecten la teoría de la clase con pasatiempos o temas que realmente apasionen al estudiante."
      }
    }

## Ejecución

Requiere Python 3.10+ y Flask.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python app.py
```

Abre `http://127.0.0.1:5000` en el navegador. Tailwind CSS se carga desde CDN, por lo que la primera carga requiere conexión a internet.

```bash
python3 app.py
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
