# main.py
import sys
from interfaz import iniciar_entrevista
from motor import MotorInferencia
import explicacion

def main():
    # 1. Recolectar datos (Hechos) a través de la Interfaz
    try:
        hechos = iniciar_entrevista()
    except KeyboardInterrupt:
        print("\n\n[!] Entrevista cancelada por el usuario. Saliendo de la terminal...")
        sys.exit(0)

    # 2. Inicializar el Motor y evaluar las reglas
    print("Analizando respuestas con la base de conocimiento...")
    motor = MotorInferencia() # Por defecto carga 'conocimiento/reglas.json'
    
    try:
        diagnosticos = motor.evaluar(hechos)
    except Exception as e:
        print(f"\n[Error del Sistema] No se pudo procesar la inferencia: {e}")
        sys.exit(1)

    # 3. Mostrar Resultados (El Diagnóstico)
    print("\n" + "="*60)
    print(" RESULTADOS DEL DIAGNÓSTICO ACADÉMICO")
    print("="*60)
    
    if not diagnosticos:
        print("\n[!] No se encontraron problemas metodológicos o de entorno críticos.")
        print("Tus métricas actuales no dispararon ninguna regla de alerta.")
    else:
        for i, diag in enumerate(diagnosticos, 1):
            print(f"\n[{i}] ALERTA: {diag['nombre']}")
            print(f"    Diagnóstico: {diag['conclusion']}")
            print(f"    Recomendación: {diag['recomendacion']}")

    # 4. Invocación del Módulo de Explicación (Transparencia del Sistema)
    if diagnosticos:
        print("\n" + "-"*60)
        respuesta = input("¿Deseas saber POR QUÉ el sistema llegó a estas conclusiones? (s/n): ").strip().lower()
        if respuesta == 's':
            explicacion.justificar_diagnosticos(diagnosticos, hechos)
        
    print("\nGracias por utilizar el Sistema Experto de Diagnóstico.")

if __name__ == "__main__":
    main()