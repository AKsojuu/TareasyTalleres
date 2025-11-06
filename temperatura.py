# CONTROL DE TEMPERATURA

print(" Control de Temperatura ")
print(" La temperatura actual es de nivel 4: 5°C ")
print(" Niveles de ajuste: 1 a 8")
print(" -----------------------------------------")

# Pedimos el nivel que desea el usuario
temperatura = int(input(" Ingrese el nivel de temperatura (1-8): "))

# Diccionario de niveles y su temperatura
niveles = {
    1: -25,
    2: -15,
    3: -5,
    4: 5,
    5: 15,
    6: 25,
    7: 35,
    8: 45
}

# Verificación de la temperatura
if temperatura in niveles:
    valor = niveles[temperatura]
    print(f" Se ajustó la temperatura a {valor} °C")

    # Indicación de la temperatura
    if valor < 0:
        print(" Frío")

    elif valor <= 20:
        print(" Templado")

    else:
        print(" Caliente")
else:
    print("Opción invalida") 
    print("Por favor seleccione un nivel del 1 al 8.")
