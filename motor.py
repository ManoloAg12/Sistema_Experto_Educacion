# motor.py
import json
import os

class MotorInferencia:
    def __init__(self, ruta_reglas="conocimiento/reglas.json"):
        self.ruta_reglas = ruta_reglas
        self.base_conocimiento = self._cargar_reglas()

    def _cargar_reglas(self):
        """
        Carga la base de conocimiento desde el sistema de archivos.
        Maneja errores básicos si el archivo no existe o está mal formateado.
        """
        if not os.path.exists(self.ruta_reglas):
            raise FileNotFoundError(f"[Error CRÍTICO] No se encontró el archivo de reglas en: {self.ruta_reglas}")
        
        try:
            with open(self.ruta_reglas, 'r', encoding='utf-8') as archivo:
                return json.load(archivo)
        except json.JSONDecodeError as e:
            raise ValueError(f"[Error CRÍTICO] El archivo JSON tiene un error de sintaxis: {e}")

    def evaluar(self, hechos):
        """
        Algoritmo de Encadenamiento Hacia Adelante.
        Compara el diccionario de hechos contra las condiciones de cada regla.
        Retorna una lista con todas las reglas que hicieron 'match' al 100%.
        """
        diagnosticos = []
        reglas = self.base_conocimiento.get("reglas", [])

        for regla in reglas:
            condiciones = regla.get("condiciones", {})
            regla_cumplida = True

            # Iteramos sobre las condiciones específicas que exige esta regla
            for variable, valor_esperado in condiciones.items():
                
                # Si el hecho no existe en las respuestas o el valor no coincide, 
                # la regla se descarta y rompemos el bucle (Optimización)
                if hechos.get(variable) != valor_esperado:
                    regla_cumplida = False
                    break 

            # Si el bucle termina y regla_cumplida sigue siendo True, 
            # significa que todas las condiciones hicieron match perfecto.
            if regla_cumplida:
                diagnosticos.append({
                    "id_regla": regla["id"],
                    "nombre": regla.get("nombre", "Diagnóstico General"),
                    "conclusion": regla["conclusion"],
                    "recomendacion": regla["recomendacion"],
                    "condiciones_evaluadas": condiciones # Útil para el módulo de explicación
                })

        return diagnosticos

if __name__ == "__main__":
    # Prueba unitaria rápida aislando el motor
    motor = MotorInferencia()
    
    # Simulamos un estudiante que trabaja mucho, duerme poco y falta a clases
    hechos_simulados = {
        "horas_trabajo_semanal": ">=20",
        "horas_sueno": "<6",
        "asistencia_clases": "irregular"
    }
    
    resultados = motor.evaluar(hechos_simulados)
    
    print(f"Reglas disparadas: {len(resultados)}")
    for res in resultados:
        print(f"[{res['id_regla']}] {res['nombre']}")