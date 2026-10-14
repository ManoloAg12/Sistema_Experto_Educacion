# Base de Conocimiento: Diagnóstico de Rendimiento Académico Universitario

## 1. Objetivo del Sistema Experto
Identificar las causas subyacentes de la disminución del rendimiento académico en estudiantes universitarios, enfocándose específicamente en perfiles de alta exigencia analítica (ej. Ciencias de la Computación, Ingeniería).

## 2. Variables de Entrada (Hechos)
El sistema recolecta el estado de las siguientes variables a través de la interfaz:
* **Horas de trabajo semanal:** `0`, `<20`, `>=20`, `>=40`
* **Horas de sueño promedio:** `<5`, `5-6`, `>=7`
* **Método de estudio principal:** `lectura_memorizacion`, `practica_distribuida`, `estudio_ultima_hora`
* **Tipo de materia reprobada:** `teorica`, `practica_logica` (ej. algoritmos, bases de datos), `proyectos_desarrollo` (ej. backend, full-stack)
* **Trabajo en equipo:** `equitativo`, `asume_toda_carga`, `conflictivo`

## 3. Matriz de Reglas (Clusters)

### Cluster A: Entorno y Gestión del Tiempo
* **Regla R01_A - Burnout por Sobrecarga:** 
  * *Si* trabaja >=20 horas *Y* duerme <6 horas *Y* su asistencia es irregular.
  * *Diagnóstico:* Agotamiento crónico (Burnout).
* **Regla R01_C - Ley de Parkinson (Procrastinación):**
  * *Si* trabaja 0 horas *Y* estudia extra <5 horas *Y* entrega trabajos tarde.
  * *Diagnóstico:* Expansión del tiempo libre sin estructura.

### Cluster B: Metodología Técnica
* **Regla R02_B - Falsa Productividad Lógica:**
  * *Si* horas de estudio >=15 *Y* método es "memorización" *Y* materia es "práctica_lógica".
  * *Diagnóstico:* Uso de técnicas de estudio incompatibles con materias de ciencias exactas.
* **Regla R04_A - Síndrome del Llanero Solitario:**
  * *Si* trabajo en equipo es "asume_toda_carga" *Y* horas de sueño <5.
  * *Diagnóstico:* Liderazgo tóxico o falta de delegación en proyectos de desarrollo, causando cuello de botella personal.