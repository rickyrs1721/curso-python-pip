import random

# Juego de piedra papel o tijera

point_user = 0
point_computer = 0
options = ("piedra", "papel", "tijera")

while True:

    option_user = input("Piedra, papel o tijera? => ")

    if not option_user in options:
        print("Esa opción no es valida, vuelve a jugar..")
        option_user = input("Piedra, papel o tijera? => ")

    option_user = option_user.lower()

    option_machine = random.choice(options)
    print(f"Select user: {option_user}")
    print(f"Select machine: {option_machine}")

    if not(option_user in options):
        print("digite un valor válido.!")
        continue

    if option_user == "piedra" and option_machine == "tijera":
        print("Ganaste..!")
        point_user += 1
    elif option_user == "piedra" and option_machine == "papel":
        print("Perdiste..!")
        point_computer += 1
    elif option_user == "piedra" and option_machine == "piedra":
        print("Empate..!")
        point_user = point_user
        point_computer = point_computer
    elif option_user == "papel" and option_machine == "tijera":
        print("Perdiste..!")
        point_computer += 1
    elif option_user == "papel" and option_machine == "papel":
        print("Empate..!")
        point_user = point_user
        point_computer = point_computer
    elif option_user == "papel" and option_machine == "piedra":
        print("Ganaste..!")
        point_user += 1
    elif option_user == "tijera" and option_machine == "tijera":
        print("Empate..!")
        point_user = point_user
        point_computer = point_computer
    elif option_user == "tijera" and option_machine == "papel":
        print("Ganaste..!")
        point_user += 1
    elif option_user == "tijera" and option_machine == "piedra":
        print("Perdiste..!")
        point_computer += 1
    

    if point_user == 2:
        print("punto user: ", point_user)
        print("punto computer: ", point_computer)
        print("Ganador del juego es el Usuario..!")
        break

    if point_computer == 2:
        print("punto user: ", point_user)
        print("punto computer: ", point_computer)
        print("Ganador del juego es la computadora.!")
        break