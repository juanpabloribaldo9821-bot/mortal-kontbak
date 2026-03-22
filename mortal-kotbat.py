import random

potions = 3
cure = 30
health_enemy = 120
health_hero = 100

def generar_daño(minimo, maximo):
    return random.randint(minimo, maximo)

def barra_vida(vida):
    corazones = vida // 10
    if corazones < 0:
        corazones = 0
    return "❤️" * corazones

def quit_health_enemy(health_enemy):
    probability = random.randint(1, 100)

    if probability <= 10:
        damage = generar_daño(25, 50)
        print("Critical hit")
    else:
        damage = generar_daño(10, 25)

    health_enemy -= damage
    print("Damage to enemy:", damage)

    return health_enemy

# 🔹 IA DEL ENEMIGO
def turno_enemigo(health_enemy, health_hero):
    # 20% de 120 = 24
    if health_enemy <= 24:
        heal = generar_daño(15, 25)
        health_enemy += heal
        if health_enemy > 120:
            health_enemy = 120
        print("Enemy heals:", heal)
    else:
        attack = generar_daño(15, 25)
        health_hero -= attack
        print("Enemy attacks. Damage:", attack)

    return health_enemy, health_hero

def show_status(health_hero, health_enemy):
    print("\nHero")
    print("Name: Kratos")
    print("Health:", health_hero, barra_vida(health_hero))

    print("\nEnemy")
    print("Name: Zephyro")
    print("Health:", health_enemy, barra_vida(health_enemy))

def pedir_opcion():
    while True:
        try:
            opcion = int(input("\nChoose action:\n1. Attack\n2. Cure\n3. Special ability\n-> "))
            if opcion in [1, 2, 3]:
                return opcion
            else:
                print("Invalid option")
        except:
            print("Enter a valid number")
print("___________")
print("|---------------------------|")
print("|WELCOME TO MORTAL KOMBAT 10|")
print("|---------------------------|")
while health_hero > 0 and health_enemy > 0:
    show_status(health_hero, health_enemy)

    turno_valido = False

    while not turno_valido:
        option = pedir_opcion()

        if option == 1:
            health_enemy = quit_health_enemy(health_enemy)
            turno_valido = True

        elif option == 2:
            if potions > 0:
                health_hero += cure
                if health_hero > 100:
                    health_hero = 100
                potions -= 1
                print("You healed 30 HP")
                turno_valido = True
            else:
                print("No potions left. Choose another option.")

        elif option == 3:
            probability2 = random.randint(1, 100)
            if probability2 <= 50:
                damage = generar_daño(30, 50)
                health_enemy -= damage
                print("Special ability successful")
                print("Damage:", damage)
            else:
                print("Special ability failed")
            turno_valido = True

    # 🔹 Turno con IA
    if health_enemy > 0:
        health_enemy, health_hero = turno_enemigo(health_enemy, health_hero)

if health_hero > 0:
    print("YOU WIN")
else:
    print("YOU LOST")
