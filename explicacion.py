# explicacion.py

def justificar_diagnosticos(diagnosticos, hechos):
    """
    Explica el razonamiento detrás de cada diagnóstico disparado por el motor.
    Desglosa las condiciones lógicas evaluadas.
    """
    print("\n" + "="*60)
    print(" JUSTIFICACIÓN DEL SISTEMA (TRAZABILIDAD DE REGLAS)")
    print("="*60)
    
    # Diccionario auxiliar para formatear las variables internas a texto legible en consola
    nombres_variables = {
        "horas_trabajo_semanal": "Horas de trabajo a la semana",
        "horas_sueno": "Horas de sueño promedio",
        "horas_estudio_extra": "Horas de estudio independiente",
        "asistencia_clases": "Nivel de asistencia a clases",
        "tipo_materia_reprobada": "Tipo de materia afectada",
        "metodo_estudio": "Técnica de estudio empleada",
        "comprension_clase": "Nivel de comprensión durante la cátedra"
    }

    for diag in diagnosticos:
        print(f"\n-> Para la conclusión: '{diag['nombre']}' (Regla disparada: {diag['id_regla']})")
        print("El motor de inferencia determinó esto basándose en los siguientes hechos registrados:\n")
        
        condiciones = diag['condiciones_evaluadas']
        
        for variable, valor_requerido in condiciones.items():
            nombre_legible = nombres_variables.get(variable, variable)
            
            # Obtenemos el valor que el usuario realmente ingresó
            valor_ingresado = hechos.get(variable, "No especificado")
            
            # En un encadenamiento hacia adelante perfecto, valor_ingresado == valor_requerido
            print(f"   * {nombre_legible}: indicaste '{valor_ingresado}'")
            
        print("\n   [Lógica Aplicada]: El experto determina que la combinación exacta de estos factores")
        print("   conduce directamente a este bloqueo académico.")
        print("-" * 60)