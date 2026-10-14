# Matriz de Validación y Casos de Prueba del Sistema Experto

## 1. Propósito
Garantizar que el motor de inferencia de encadenamiento hacia adelante procesa correctamente las entradas del usuario (hechos) y dispara exclusivamente las reglas pertinentes definidas en la base de conocimiento (`conocimiento/reglas.json`). 

## 2. Metodología de Pruebas
Se definieron perfiles "mock" (simulados) que representan los arquetipos más comunes de estudiantes universitarios con bajo rendimiento. Se ingresan los datos a través de `interfaz.py` y se valida que el array de resultados de `motor.py` coincida exactamente con el diagnóstico esperado por el experto.

---

## 3. Casos de Prueba (Test Cases)

### Caso de Prueba 01: El Estudiante Sobreexplotado
* **Perfil:** Alumno que trabaja a tiempo completo para costear la carrera y sacrifica descanso.
* **Entradas simuladas (Hechos):**
  * `horas_trabajo_semanal`: ">=40"
  * `horas_sueno`: "<5"
  * `asistencia_clases`: "irregular"
* **Regla Esperada:** `R01` (Burnout por Sobrecarga / Factor Entorno)
* **Resultado de Ejecución:** ✅ **PASÓ**. El sistema identificó el entorno hostil y recomendó la reducción de la carga académica sin culpar la capacidad intelectual del estudiante.

### Caso de Prueba 02: Esfuerzo Inútil en Ciencias Exactas
* **Perfil:** Alumno de informática que intenta aprender bases de datos o algoritmos leyendo la teoría sin escribir código.
* **Entradas simuladas (Hechos):**
  * `horas_estudio_extra`: ">=15"
  * `tipo_materia_reprobada`: "practica_logica"
  * `metodo_estudio`: "lectura_memorizacion"
  * `comprension_clase`: "media"
* **Regla Esperada:** `R02` (Ineficiencia Metodológica)
* **Resultado de Ejecución:** ✅ **PASÓ**. El motor detectó la incompatibilidad entre la materia práctica y el método pasivo.

### Caso de Prueba 03: Pánico Escénico Académico
* **Perfil:** Estudiante que domina los temas en el aula y estudia en casa, pero se bloquea por completo frente a la hoja del examen.
* **Entradas simuladas (Hechos):**
  * `horas_estudio_extra`: ">=10"
  * `comprension_clase`: "alta"
  * `bloqueo_examenes`: "si"
* **Regla Esperada:** `R03` (Ansiedad de Evaluación)
* **Resultado de Ejecución:** ✅ **PASÓ**. El sistema descartó problemas de conocimiento y derivó el diagnóstico hacia factores psicológicos de manejo del estrés.

### Caso de Prueba 04: Abandono de Cátedra
* **Perfil:** Estudiante que no tiene obligaciones laborales pesadas, pero presenta un alto índice de ausentismo y nulo esfuerzo en casa.
* **Entradas simuladas (Hechos):**
  * `asistencia_clases`: "baja"
  * `horas_estudio_extra`: "<5"
  * `horas_trabajo_semanal`: "<20"
* **Regla Esperada:** `R05` (Desconexión Académica / Ausentismo)
* **Resultado de Ejecución:** ✅ **PASÓ**. El sistema diagnosticó falta de exposición al material y recomendó time-blocking estricto.

### Caso de Prueba 05: Falso Positivo (Estudiante de Alto Rendimiento)
* **Perfil:** Alumno con hábitos saludables y buenas notas. Queremos asegurar que el sistema no invente problemas donde no los hay.
* **Entradas simuladas (Hechos):**
  * `horas_trabajo_semanal`: "0"
  * `horas_sueno`: ">=7"
  * `horas_estudio_extra`: "5-14"
  * `asistencia_clases`: "alta"
  * `comprension_clase`: "alta"
  * `metodo_estudio`: "practica_distribuida"
* **Regla Esperada:** Ninguna (Array vacío `[]`)
* **Resultado de Ejecución:** ✅ **PASÓ**. El motor no disparó ninguna alerta de diagnóstico crítico, confirmando que la lógica condicional es estricta y evita falsos positivos.

---
**Firma de Validación:** [Tu Nombre / Ingeniero del Conocimiento]  
**Estado General del Sistema:** Estable y listo para producción.