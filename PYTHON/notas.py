def calcular_nota(puntaje):
    # Definimos los parámetros
    nota_minima = 1
    nota_media = 4
    nota_maxima = 7
    puntaje_maximo = 100
    puntaje_minimo = 60  # Exigencia del 60%

    if puntaje < 0 or puntaje > 100:
        return "El puntaje debe estar entre 0 y 100."

    # Calcular la nota de acuerdo al puntaje
    if puntaje < puntaje_minimo:
        # Escala proporcional entre 0 y 60 puntos (nota entre 1 y 4)
        nota = 1 + (puntaje * (nota_media - nota_minima) / puntaje_minimo)
    else:
        # Escala proporcional entre 60 y 100 puntos (nota entre 4 y 7)
        nota = nota_media + ((puntaje - puntaje_minimo) * (nota_maxima - nota_media) / (puntaje_maximo - puntaje_minimo))

    # Devolvemos la nota redondeada a dos decimales
    return round(nota, 2)

# Bucle para aceptar puntajes de forma continua
while True:
    try:
        puntaje = float(input("Ingresa el puntaje (0-100) o escribe 'salir' para terminar: "))
        calificacion = calcular_nota(puntaje)
        print(f"La calificación es: {calificacion}")
    except ValueError:
        # Si el usuario escribe 'salir' o cualquier cosa no numérica, termina el bucle
        decision = input("¿Deseas salir? Escribe 'sí' para terminar o 'no' para continuar: ").lower()
        if decision == 'sí' or decision == 'si':
            print("Programa finalizado.")
            break
        else:
            continue
