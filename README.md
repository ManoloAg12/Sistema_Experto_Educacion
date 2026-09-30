# Sistema Experto Educativo

## 📖 ¿Qué es este proyecto?
<!-- Describe aquí tu proyecto en un par de líneas. -->
Este es un sistema experto basado en reglas, desarrollado en Python y enfocado en el área de educación. Su objetivo principal es [EJEMPLO: orientar a los estudiantes sobre su estilo de aprendizaje / ayudar a los docentes a detectar dificultades de aprendizaje / recomendar planes de estudio]. 

## 🧠 ¿Quién es el experto?
<!-- Detalla de dónde se extrajo la información para la base de conocimiento. -->
El conocimiento codificado en este sistema proviene de [EJEMPLO: entrevistas realizadas a docentes especialistas en psicopedagogía / un experto en currículo educativo]. Los detalles del proceso de extracción de conocimiento se encuentran en `docs/entrevista.md`.

## 📂 Estructura del Proyecto
El repositorio sigue la siguiente estructura modular:
* `main.py`: Punto de entrada de la aplicación.
* `motor.py`: Motor de inferencia encargado de evaluar las reglas.
* `interfaz.py`: Gestiona las preguntas y respuestas en la terminal.
* `explicacion.py`: Módulo que responde al usuario la pregunta "¿por qué?" justificando las decisiones.
* `conocimiento/reglas.json`: Archivo que almacena la base de conocimiento.
* `docs/`: Carpeta con toda la documentación, validaciones y diseño del árbol de decisión.

## ⚙️ Cómo se ejecuta

### Requisitos previos
* Python 3 instalado en el sistema.

### Instalación y ejecución
1. Clona este repositorio en tu máquina local:
   ```bash
   git clone <AQUI_TU_ENLACE_DE_GITHUB>
   cd sistema_experto_educacion
   ```

2. Crea y activa un entorno virtual (recomendado):
   ```bash
   python3 -m venv env
   source env/bin/activate  # Para macOS/Linux
   # En Windows usa: env\Scripts\activate
   ```

3. Ejecuta el sistema:
   ```bash
   python3 main.py
   ```

## 🤖 Bitácora de Inteligencia Artificial
El proceso de desarrollo de este software fue asistido por Inteligencia Artificial. Todos los prompts y usos registrados se encuentran documentados en `docs/bitacora_ia.md`.