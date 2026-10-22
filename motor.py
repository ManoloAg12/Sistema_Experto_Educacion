# motor.py
import json
import os
import operator
import re

class MotorInferencia:
    def __init__(self, ruta_reglas="conocimiento/reglas.json"):
        self.ruta_reglas = ruta_reglas
        self.base_conocimiento = self._cargar_reglas()

    def _cargar_reglas(self):
        """Carga y valida la base de conocimiento."""
        if not os.path.isfile(self.ruta_reglas):
            raise FileNotFoundError(f"No se encontró el archivo de reglas: {self.ruta_reglas}")

        try:
            with open(self.ruta_reglas, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        except json.JSONDecodeError as error:
            raise ValueError(f"El JSON de reglas no es válido: {error}") from error

        if not isinstance(datos, dict):
            raise ValueError("La base de conocimiento debe ser un objeto JSON.")

        reglas = datos.get("reglas")
        if not isinstance(reglas, list):
            raise ValueError("La base de conocimiento debe contener una lista 'reglas'.")

        ids = set()
        for indice, regla in enumerate(reglas, start=1):
            if not isinstance(regla, dict):
                raise ValueError(f"La regla {indice} debe ser un objeto.")

            for campo in ("id", "condiciones", "conclusion", "recomendacion"):
                if campo not in regla:
                    raise ValueError(f"La regla {indice} no contiene el campo '{campo}'.")

            if not isinstance(regla["condiciones"], dict) or not regla["condiciones"]:
                raise ValueError(f"La regla {indice} debe tener condiciones no vacías.")

            if regla["id"] in ids:
                raise ValueError(f"ID de regla duplicado: {regla['id']}")

            ids.add(regla["id"])

        return datos

    @staticmethod
    def _comparar(valor_real, condicion):
        """Evalúa igualdad, desigualdad y operadores numéricos."""
        if not isinstance(condicion, str):
            return valor_real == condicion

        if isinstance(valor_real, bool):
            if condicion.lower() == "true": return valor_real is True
            if condicion.lower() == "false": return valor_real is False

        coincidencia = re.fullmatch(r"\s*(>=|<=|!=|==|>|<)\s*(-?\d+(?:\.\d+)?)\s*", condicion)
        if not coincidencia:
            return valor_real == condicion

        operador_texto, numero_texto = coincidencia.groups()
        if isinstance(valor_real, bool) or valor_real is None:
            return False

        try:
            numero_real = float(valor_real)
            numero_esperado = float(numero_texto)
        except (TypeError, ValueError):
            return False

        operaciones = {
            ">": operator.gt, "<": operator.lt,
            ">=": operator.ge, "<=": operator.le,
            "==": operator.eq, "!=": operator.ne,
        }
        return operaciones[operador_texto](numero_real, numero_esperado)

    def evaluar(self, hechos):
        """Evalúa todas las reglas y devuelve los diagnósticos coincidentes con su factor de certeza."""
        if not isinstance(hechos, dict):
            raise TypeError("Los hechos deben proporcionarse como un diccionario.")

        # Usaremos un diccionario para agrupar conclusiones idénticas y combinar sus certezas
        conclusiones_agrupadas = {}

        for regla in self.base_conocimiento["reglas"]:
            condiciones = regla["condiciones"]

            cumplida = all(
                variable in hechos and self._comparar(hechos[variable], condicion)
                for variable, condicion in condiciones.items()
            )

            if cumplida:
                # Obtenemos la certeza de la regla (por defecto 0.90 si no está en el JSON)
                fc_regla = float(regla.get("certeza", 0.90))
                conclusion = regla["conclusion"]

                if conclusion in conclusiones_agrupadas:
                    # Fórmula de Combinación de MYCIN para dos evidencias positivas
                    fc_actual = conclusiones_agrupadas[conclusion]["certeza"]
                    fc_nuevo = fc_actual + fc_regla * (1 - fc_actual)
                    
                    conclusiones_agrupadas[conclusion]["certeza"] = round(fc_nuevo, 2)
                    conclusiones_agrupadas[conclusion]["reglas"].append(regla["id"])
                else:
                    # Primera vez que vemos esta conclusión
                    conclusiones_agrupadas[conclusion] = {
                        "id_regla": regla["id"], # Guardamos la principal
                        "reglas": [regla["id"]],
                        "cluster": regla.get("cluster", "General"),
                        "nombre": regla.get("nombre", "Diagnóstico general"),
                        "conclusion": conclusion,
                        "recomendacion": regla["recomendacion"],
                        "certeza": fc_regla,
                        "condiciones_evaluadas": condiciones.copy(),
                    }

        # Convertimos el diccionario a una lista y lo ordenamos por certeza de mayor a menor
        resultados = list(conclusiones_agrupadas.values())
        resultados.sort(key=lambda x: x["certeza"], reverse=True)

        return resultados