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
            raise FileNotFoundError(
                f"No se encontró el archivo de reglas: {self.ruta_reglas}"
            )

        try:
            with open(self.ruta_reglas, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        except json.JSONDecodeError as error:
            raise ValueError(
                f"El JSON de reglas no es válido: {error}"
            ) from error

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
                    raise ValueError(
                        f"La regla {indice} no contiene el campo '{campo}'."
                    )

            if not isinstance(regla["condiciones"], dict) or not regla["condiciones"]:
                raise ValueError(
                    f"La regla {indice} debe tener condiciones no vacías."
                )

            if regla["id"] in ids:
                raise ValueError(f"ID de regla duplicado: {regla['id']}")

            ids.add(regla["id"])

        return datos

    @staticmethod
    def _comparar(valor_real, condicion):
        """Evalúa igualdad, desigualdad y operadores numéricos."""
        if not isinstance(condicion, str):
            return valor_real == condicion

        coincidencia = re.fullmatch(
            r"\s*(>=|<=|!=|==|>|<)\s*(-?\d+(?:\.\d+)?)\s*",
            condicion
        )

        # Si no hay operador, se compara como categoría o valor literal.
        if not coincidencia:
            return valor_real == condicion

        operador_texto, numero_texto = coincidencia.groups()

        # Evita comparar números con respuestas ausentes o inválidas.
        if isinstance(valor_real, bool) or valor_real is None:
            return False

        try:
            numero_real = float(valor_real)
            numero_esperado = float(numero_texto)
        except (TypeError, ValueError):
            return False

        operaciones = {
            ">": operator.gt,
            "<": operator.lt,
            ">=": operator.ge,
            "<=": operator.le,
            "==": operator.eq,
            "!=": operator.ne,
        }

        return operaciones[operador_texto](
            numero_real, numero_esperado
        )

    def evaluar(self, hechos):
        """Evalúa todas las reglas y devuelve los diagnósticos coincidentes."""
        if not isinstance(hechos, dict):
            raise TypeError("Los hechos deben proporcionarse como un diccionario.")

        diagnosticos = []

        for regla in self.base_conocimiento["reglas"]:
            condiciones = regla["condiciones"]

            # Una regla se activa solo si todas sus condiciones se cumplen.
            cumplida = all(
                variable in hechos
                and self._comparar(hechos[variable], condicion)
                for variable, condicion in condiciones.items()
            )

            if cumplida:
                diagnosticos.append({
                    "id_regla": regla["id"],
                    "nombre": regla.get("nombre", "Diagnóstico general"),
                    "conclusion": regla["conclusion"],
                    "recomendacion": regla["recomendacion"],
                    "condiciones_evaluadas": condiciones.copy(),
                })

        return diagnosticos


if __name__ == "__main__":
    motor = MotorInferencia()

    hechos_simulados = {
        "horas_trabajo_semanal": 22,
        "horas_sueno": 5,
        "asistencia_clases": "irregular",
    }

    resultados = motor.evaluar(hechos_simulados)

    print(f"\nReglas activadas: {len(resultados)}")

    for resultado in resultados:
        print(f"\n[{resultado['id_regla']}] {resultado['nombre']}")
        print(f"Diagnóstico: {resultado['conclusion']}")
        print(f"Recomendación: {resultado['recomendacion']}")