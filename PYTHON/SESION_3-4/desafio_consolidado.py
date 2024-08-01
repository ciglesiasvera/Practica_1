# Título: Sistema de Puntuación Interactivo para un Juego de Niveles

# Descripción:
# Desarrolla un sistema de puntuación interactivo para un juego de niveles utilizando Python.
# El sistema debe cumplir con los siguientes requisitos:

# 1. Utiliza un diccionario para almacenar los jugadores y sus puntuaciones.

# 2. Implementa una lista de niveles (Fácil, Medio, Difícil, Experto)
# y sus correspondientes puntuaciones.

# 3. Recibe información de la consola para simular una ronda de juego:
#    - Pide al usuario que ingrese el nombre del jugador actual.
#    - Solicita el nivel completado por el jugador.
#    - Pregunta por el tiempo que tardó en completar el nivel.

# 4. Valida la entrada del usuario:
#    - Verifica que el jugador exista en el diccionario de jugadores.
#    - Asegúrate de que el nivel ingresado sea válido.
#    - Comprueba que el tiempo ingresado sea un número positivo.

# 5. Actualiza la puntuación del jugador basándote en el nivel completado.

# 6. Incluye un sistema de bonificación: 
# si un jugador completa un nivel Difícil o Experto en 30 segundos o menos, 
# recibe puntos extra.

# 7. Determina el líder actual del juego.
# En caso de empate, muestra todos los jugadores empatados.

# 8. Muestra las puntuaciones actuales de todos los jugadores.

# Restricciones:
# - Utiliza estructuras if-else para la lógica condicional.
# - Emplea operadores lógicos cuando sea necesario.
# - Usa listas y diccionarios para almacenar y manipular datos.
# - Utiliza input() para recibir información del usuario.

# # Lista de niveles con sus respectivos puntos
# niveles = ["Fácil", "Medio", "Difícil", "Experto"]
# puntos_por_nivel = [10, 20, 30, 50]
######

# Lista de niveles con sus respectivos puntos
levels = ["Fácil", "Medio", "Difícil", "Experto"]
level_points = {"Fácil": 10, "Medio": 20, "Difícil": 30, "Experto": 50}
# Diccionario para almacenar los jugadores y sus puntuaciones
players = {}
while True:
    # Ingresar datos del jugador
    name = input("Ingresa el nombre del jugador: ")
    
    # Validar si el jugador ya existe en el diccionario, si no, agregarlo
    if name not in players:
        players[name] = 0

    # Ingresar nivel completado
    levels = input("Ingrese el nivel completado (Fácil/Medio/Difícil/Experto): ")
    if levels not in levels:
        print("Nivel inválido. Intente nuevamente.")
        continue

    # Ingresar tiempo en segundos
    try:
        time = float(input("Ingrese el tiempo en segundos: "))
        if time <= 0:
            print("El tiempo debe ser un número positivo. Intente nuevamente.")
            continue
    except ValueError:
        print("El tiempo debe ser un número. Intente nuevamente.")
        continue

    # Actualizar la puntuación del jugador
    if levels == "Fácil":
        points = level_points["Fácil"]
    elif levels == "Medio":
        points = level_points["Medio"]
    elif levels == "Difícil":
        points = level_points["Difícil"]
        if time <= 30:
            points += 10  # Bonificación por completar en 30 segundos o menos
    elif levels == "Experto":
        points = level_points["Experto"]
        if time <= 30:
            points += 10  # Bonificación por completar en 30 segundos o menos

    players[name] += points

    # Determinar el líder actual del juego
    max_puntuacion = max(players.values())
    leaders = [player for player, points in players.items() if points == max_puntuacion]
    if len(leaders) == 1:
        print(f"El líder actual es {leaders[0]} con {max_puntuacion} puntos.")
    else:
        print(f"Hay un empate entre los líderes: {', '.join(leaders)} con {max_puntuacion} puntos cada uno.")

    # Mostrar las puntuaciones actuales de todos los jugadores
    print("\nPuntuaciones actuales de todos los jugadores:")
    for player, points in players.items():
        print(f"{player}: {points} puntos")
    print("\n")

print("Juego terminado. Gracias por participar!")