# Bitácora de Uso de Inteligencia Artificial (IA) en el Desarrollo

**Proyecto:** Sistema Experto de Diagnóstico de Rendimiento Académico Universitario  
**Autor:** Manolo Herminio Vargas Aguilar  
**Herramienta de IA Utilizada:** Gemini (Google)  
**Técnica de Prompting Principal:** Asignación de Roles (Role-prompting) y Generación Iterativa  

## 1. Propósito de la Bitácora
Este documento detalla el uso de asistencia de Inteligencia Artificial durante las fases de diseño, codificación y documentación del Sistema Experto, garantizando la transparencia académica y explicando el proceso de validación humana aplicado a las respuestas generadas.

## 2. Fases de Asistencia de IA

### Fase 1: Estructuración de la Base de Conocimiento (JSON)
* **Objetivo:** Traducir las reglas heurísticas de un Asesor Académico a un formato estructurado y escalable.
* **Uso de la IA:** Se le asignó a la IA el rol de "Asesor Académico / Psicólogo Educativo con experiencia en carreras de informática". Se solicitó la generación de diagnósticos basados en la combinación de variables como horas de sueño, carga laboral y métodos de estudio.
* **Validación Humana:** Se descartaron diagnósticos genéricos y se refinaron las variables para que encajaran específicamente en el contexto de estudiantes de educación superior (ej. inclusión de variables como `tipo_materia_reprobada` orientada a programación y bases de datos).
* **Ejemplo de Prompt Utilizado:** *"Actúa como un asesor académico universitario. Proporciona reglas lógicas para diagnosticar por qué un alumno reprueba materias, estructuradas en formato JSON con 'condiciones', 'conclusion' y 'recomendacion'."*

### Fase 2: Desarrollo del Motor de Inferencia (Python)
* **Objetivo:** Construir un motor de encadenamiento hacia adelante (Forward Chaining) eficiente y una interfaz de terminal interactiva.
* **Uso de la IA:** La IA generó la estructura base de las clases en `motor.py` para iterar sobre el archivo JSON, así como los diccionarios de validación de entrada en `interfaz.py` y la lógica de trazabilidad en `explicacion.py`.
* **Validación Humana:** Se revisó el código para asegurar el desacoplamiento. Se verificó que `motor.py` no contuviera lógica de interfaz y que las comparaciones de strings (ej. `">=20"`) coincidieran exactamente con las llaves del JSON. Se implementó manejo de excepciones (`try-except`) para evitar caídas del sistema.

### Fase 3: Modelado Visual (Árbol de Decisión)
* **Objetivo:** Representar gráficamente el flujo de toma de decisiones del motor de inferencia.
* **Uso de la IA:** Dado que la IA no puede generar archivos `.png` directamente, se utilizó para traducir la lógica condicional del archivo JSON a sintaxis **Mermaid.js**.
* **Validación Humana:** El código Mermaid generado fue renderizado en el editor en vivo (Mermaid Live Editor) y exportado manualmente a `docs/arbol_decision.png` para asegurar su correcta legibilidad.

### Fase 4: Documentación y Casos de Prueba
* **Objetivo:** Crear la documentación técnica que respalda la arquitectura del proyecto.
* **Uso de la IA:** Generación de formatos estándar de la industria, como la transcripción de la Adquisición del Conocimiento (`entrevista.md`) y la matriz de validación (`validacion.md`).
* **Ejemplo de Prompt Utilizado:** *"Genera una matriz de casos de prueba simulando perfiles de estudiantes (ej. el estudiante sobreexplotado laboralmente) para validar que el motor dispara la regla correcta."*

## 3. Conclusión sobre la Integración
El uso de la IA aceleró drásticamente la fase de "codificación" (escribir el boilerplate de Python y la sintaxis repetitiva del JSON). Sin embargo, la fase de "ingeniería" (definir qué variables importan, diseñar la arquitectura modular en carpetas y validar que el algoritmo de inferencia tenga sentido clínico/académico) fue dirigida íntegramente por el desarrollador humano.