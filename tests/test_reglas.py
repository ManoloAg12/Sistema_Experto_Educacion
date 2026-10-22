import unittest

from evaluacion import evaluar_perfil
from motor import MotorInferencia
from cuestionario import todas_las_preguntas


class MotorInferenciaTests(unittest.TestCase):
    def setUp(self):
        self.motor = MotorInferencia()

    def test_detecta_sobrecarga_por_trabajo_y_descanso(self):
        hechos = {"horas_trabajo_semanal": 40, "horas_sueno": 4, "tiempo_transporte": 3}
        ids = [resultado["id_regla"] for resultado in self.motor.evaluar(hechos)]
        self.assertIn("R01_A", ids)

    def test_no_activa_regla_si_falta_una_condicion(self):
        hechos = {"horas_trabajo_semanal": 40, "horas_sueno": 4, "tiempo_transporte": 1}
        self.assertEqual(self.motor.evaluar(hechos), [])

    def test_detecta_practica_insuficiente_en_programacion(self):
        hechos = {"tipo_materia_reprobada": "programacion", "metodo_estudio": "lectura_memorizacion", "comprension_clase": "media"}
        ids = [resultado["id_regla"] for resultado in self.motor.evaluar(hechos)]
        self.assertIn("R02_B", ids)

    def test_cada_pregunta_tiene_la_estructura_esperada(self):
        for pregunta in todas_las_preguntas():
            self.assertEqual(len(pregunta), 5)


class EvaluacionPerfilTests(unittest.TestCase):
    def test_prioriza_regla_experta(self):
        resultado = evaluar_perfil({"horas_trabajo_semanal": 40, "horas_sueno": 4, "tiempo_transporte": 3})
        self.assertEqual(resultado[0]["id"], "R01_A")
        self.assertEqual(resultado[0]["nivel"], "Alto")

    def test_crea_alerta_preventiva_con_evidencia(self):
        resultado = evaluar_perfil({"metodo_estudio": "estudio_ultima_hora", "tipo_materia_reprobada": "matematicas"})
        self.assertEqual(resultado[0]["tipo"], "Alerta preventiva")
        self.assertIn("metodo_estudio", resultado[0]["evidencia"])
