# Adquisición de Conocimiento: Entrevista con el Experto

**Proyecto:** Sistema Experto de Diagnóstico de Rendimiento Académico Universitario  
**Rol del Entrevistador:** Ingeniero del Conocimiento  
**Rol del Experto:** Asesor Académico / Psicólogo Educativo (Experiencia en Facultades de Ciencias e Informática)  
**Fecha de la Sesión:** Octubre 2026  
**Técnica Utilizada:** Entrevista Estructurada y Análisis de Casos  

---

## Objetivo de la Sesión
Extraer las reglas heurísticas que utiliza un asesor académico experimentado para diagnosticar por qué un estudiante universitario experimenta una caída abrupta en sus calificaciones, y qué recomendaciones personalizadas se le deben dar.

## Transcripción de la Entrevista

**Ingeniero de Conocimiento (IC):** Para empezar a diseñar el motor de inferencia, necesito entender cómo clasifica usted los problemas de los alumnos. Cuando un estudiante llega con notas bajas, ¿cuál es el primer factor que evalúa?

**Experto de Dominio (ED):** Lo primero que descarto es el factor físico y de entorno. Muchos alumnos, especialmente en carreras técnicas, trabajan y estudian al mismo tiempo. Si un estudiante me dice que tiene una jornada laboral de 20 horas o más a la semana, y su promedio de sueño cae por debajo de las 6 horas, mi diagnóstico inmediato es **Burnout por Sobrecarga**. En ese estado, el cerebro no retiene información compleja. La recomendación no es "estudiar más", sino reducir la carga académica.

**IC:** Entendido. ¿Qué sucede con los estudiantes que tienen el tiempo, no trabajan formalmente, e invierten hasta 15 horas extra a la semana estudiando, pero aún así reprueban parciales? 

**ED:** Ahí entramos a los factores metodológicos. Si el alumno reprueba materias lógicas o de ciencias exactas (como programación, bases de datos o matemáticas), le pregunto por su método de estudio. Si me responde que lee diapositivas, repasa apuntes o memoriza conceptos, estamos ante un caso claro de **Ineficiencia Metodológica**. 

**IC:** ¿Por qué la lectura no funciona en estos casos?

**ED:** Porque materias como arquitectura de software o algoritmia requieren memoria muscular y lógica abstracta. La lectura es pasiva. La regla heurística aquí es: *Altas horas de estudio + Método pasivo + Materia lógica = Falsa Productividad*. Mi recomendación es cambiar inmediatamente a resolución de problemas prácticos desde cero.

**IC:** He notado en proyectos universitarios de desarrollo de software que algunos estudiantes sacan la máxima nota, pero están completamente agotados. ¿Considera esto un problema diagnosticable?

**ED:** Absolutamente. Lo llamamos el **Síndrome del Llanero Solitario** o Sobrecarga Colaborativa. Ocurre cuando el estudiante asume toda la carga técnica de un proyecto grupal por desconfianza en su equipo. La regla se dispara cuando vemos: *Trabajo en equipo conflictivo o desigual + Entregas a tiempo + Menos de 5 horas de sueño*. A corto plazo salvan la materia, pero a medio plazo colapsan en las demás asignaturas. Les exijo aprender a usar control de versiones y delegar.

**IC:** ¿Y qué hay del estudiante que entiende todo perfectamente en clase, el catedrático le explica y lo capta rápido, pero reprueba los exámenes?

**ED:** Puede deberse a dos cosas. Si no estudia nada fuera de clase, es el **Efecto Dunning-Kruger** (exceso de confianza). Creen que entender es dominar. Pero si además estudian en casa y aún así fracasan en el momento de la evaluación presencial, es un problema psicológico: **Ansiedad de Evaluación**. El estrés bloquea el acceso a la memoria. A ellos les recomiendo simular parciales con cronómetro para desensibilizarse.

**IC:** Finalmente, ¿cómo diagnostica al alumno que simplemente deja de ir a la universidad o se presenta una vez al mes?

**ED:** Si la asistencia es nula y la inversión de horas en casa es menor a 5, es una **Desconexión Académica**. Generalmente viene acompañada de falta de motivación vocacional. La solución táctica es el "Time-blocking" estricto, pero la solución real suele requerir reevaluar si están en la carrera correcta.

---

## Conclusiones para la Base de Conocimiento (Mapeo a Reglas)
De esta entrevista, el Ingeniero del Conocimiento extrae las siguientes variables críticas para programar en `reglas.json`:
1. `horas_trabajo_semanal`
2. `horas_sueno`
3. `horas_estudio_extra`
4. `metodo_estudio`
5. `tipo_materia_reprobada`
6. `comprension_clase`
7. `trabajo_equipo`
8. `asistencia_clases`