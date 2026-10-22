import unittest
import os
import sys

# Asegura que Python encuentre el motor desde la carpeta tests
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from motor import MotorInferencia

class TestSistemaExperto(unittest.TestCase):

    def setUp(self):
        # Se ejecuta antes de cada prueba. Carga el JSON real.
        self.motor = MotorInferencia()

    def test_regla_sobrecarga(self):
        # Probamos que la regla R01_A se active correctamente
        hechos = {
            "horas_trabajo_semanal": 40,
            "horas_sueno": 4,
            "tiempo_transporte": 3
        }
        resultados = self.motor.evaluar(hechos)
        diagnosticos = [r["id_regla"] for r in resultados]
        
        # Verifica que la regla se activó
        self.assertIn("R01_A", diagnosticos)

    def test_no_falsos_positivos(self):
        # Si duerme bien y no trabaja mucho, la regla R01_A NO debe saltar
        hechos = {
            "horas_trabajo_semanal": 0,
            "horas_sueno": 8,
            "tiempo_transporte": 1
        }
        resultados = self.motor.evaluar(hechos)
        diagnosticos = [r["id_regla"] for r in resultados]
        
        # Verifica que la regla NO se activó
        self.assertNotIn("R01_A", diagnosticos)
        
    def test_regla_conectividad(self):
        # Probamos la regla que agregamos de tu captura
        hechos = {
            "sin_internet": True,
            "otros_con_internet": False
        }
        resultados = self.motor.evaluar(hechos)
        diagnosticos = [r["id_regla"] for r in resultados]
        
        self.assertIn("R08_B", diagnosticos)

if __name__ == "__main__":
    unittest.main()