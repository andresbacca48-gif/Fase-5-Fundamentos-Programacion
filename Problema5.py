# ==========================================
# CURSO: Fundamentos de Programación (213022)
# FASE 5: Evaluación Final POA
# ESTUDIANTE: Andrés Bacca
# GRUPO: 213022_16
# PROBLEMA SELECCIONADO: Problema 5
# ==========================================

def calcular_y_clasificar_jornada(horas_semanales):
    """
    Función que calcula la suma total de horas y clasifica la jornada.
    Retorna el total de horas y la clasificación correspondiente.
    """
    # Lógica de negocio: Calcular la suma de las horas del arreglo/lista
    total_horas = sum(horas_semanales)
    
    # Lógica de negocio: Clasificación según el umbral de 40 horas
    if total_horas > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"
        
    return total_horas, clasificacion


def procesar_control_horas():
    # Matriz con 4 recursos (personas de tu familia) y sus horas de Lunes a Viernes
    # Estructura de cada fila: [Nombre, Lunes, Martes, Miércoles, Jueves, Viernes]
    matriz_empleados = [
        ["Robinson", 9, 9, 8, 9, 9],    # Total: 44 horas (Sobretiempo)
        ["Ana", 8, 8, 8, 8, 8],         # Total: 40 horas (Horario Estándar)
        ["Marlon", 6, 8, 7, 8, 6],      # Total: 35 horas (Horario Estándar)
        ["Andres", 9, 10, 8, 9, 8]      # Total: 44 horas (Sobretiempo)
    ]
    
    print("==================================================")
    print("      REPORTE DE JORNADAS LABORALES SEMANALES     ")
    print("==================================================")
    print(f"{'Nombre':<15} | {'Horas Totales':<13} | {'Clasificación':<16}")
    print("-" * 50)
    
    # Recorrer la matriz usando estructuras de control (ciclo for)
    for empleado in matriz_empleados:
        nombre = empleado[0]
        # Extraemos las horas trabajadas (desde la columna 1 hasta la 5)
        horas_diarias = empleado[1:]
        
        # Llamamos a la función modular para calcular y clasificar
        total_horas, clasificacion = calcular_y_clasificar_jornada(horas_diarias)
        
        # Mostrar los resultados formateados en consola
        print(f"{nombre:<15} | {total_horas:<13} | {clasificacion:<16}")
        
    print("==================================================")


# Punto de entrada para ejecutar el programa
if __name__ == "__main__":
    procesar_control_horas()
