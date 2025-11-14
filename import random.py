#PROGRAMA PARA ADIVINAR UN NUMERO GENERADO POR IA
# REALIZADO POR BRANDON OYOLA CALDERON Y SANTIAGO CAICEDO SERRATO
import random

def adivina_el_numero():
    # 1. Definir el rango de números
    limite_inferior = 1
    limite_superior = 100
    
    # 2. Generar el número secreto
    # `random.randint` incluye ambos límites.
    numero_secreto = random.randint(limite_inferior, limite_superior)
    
    # Inicializar el contador de intentos y la suposición del usuario
    intentos = 0
    suposicion = None
    
    print("🤖 ¡Bienvenido al juego de Adivina el Número!")
    print(f"Estoy pensando en un número entre **{limite_inferior}** y **{limite_superior}**.")
    print("¡Intenta adivinarlo!")
    print("-" * 30)

    # El bucle continúa mientras la suposición no sea igual al número secreto
    while suposicion != numero_secreto:
        try:
            # 3. Pedir la entrada del usuario
            entrada = input("Introduce tu suposición: ")
            suposicion = int(entrada)
            intentos += 1
            
            # 4. Dar pistas
            if suposicion < limite_inferior or suposicion > limite_superior:
                print(f"⚠️ Por favor, introduce un número *dentro* del rango ({limite_inferior} a {limite_superior}).")
                # No incrementamos los intentos si el número está fuera de rango
                intentos -= 1 
            elif suposicion < numero_secreto:
                print("⬆️ ¡Demasiado bajo! Intenta con un número mayor.")
            elif suposicion > numero_secreto:
                print("⬇️ ¡Demasiado alto! Intenta con un número menor.")
                
        except ValueError:
            # Manejar el error si el usuario no ingresa un número
            print("❌ Entrada no válida. Por favor, introduce solo números enteros.")

    # 5. Mensaje de éxito (solo se ejecuta cuando `suposicion == numero_secreto`)
    print("-" * 30)
    print(f"🎉 **¡Felicidades!** ¡Adivinaste el número!")
    print(f"El número secreto era el **{numero_secreto}**.")
    print(f"Te tomó **{intentos}** intentos.")

# Llamar a la función para iniciar el juego

adivina_el_numero()
