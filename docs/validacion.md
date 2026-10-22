# Validación del sistema

Las pruebas automatizadas están en `tests/test_reglas.py` y se ejecutan con:

```bash
python3 -m unittest discover -s tests -v
```

Cubren activación de reglas, prevención de falsos positivos, priorización de resultados y alertas preventivas con evidencia. Cada nueva regla en `conocimiento/reglas.json` debe añadir su caso de prueba correspondiente.
