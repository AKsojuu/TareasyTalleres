#La empresa XYZ necesita automatizar los siguientes procesos

#-1 Control de temperatura
#-2 Valor e sueldos(diario, mensual, anual)
#-3 Calculo de areasy perimeto de 4 figuras basicas

#-1 Control de temperatura
print("la temperatura actual es de nivel 4: 5°C")

temperatura =int(input("ingrese su nivel de temperatura, (1,2,3,4,5,6,7,8)"))

if temperatura ==1:
    print("Se ajusto a -25°C")
elif temperatura==2:
    print("Se ajusto a -15°C")
elif temperatura==3:
    print("Se ajusto a -5°C")
elif temperatura==4:
    print("Se ajusto a 5°C")
elif temperatura==5:
    print("Se ajusto a 15°C")
elif temperatura==6:
    print("Se ajusto a 25°C")
elif temperatura==7:
    print("Se ajusto a 35°C")
elif temperatura==8:
    print("Se ajusto a 45°C")
else:
    print("Seleccione una opción correcta")

#-2 Valor de sueldos    
# Diario

sueldo=float(input("Ingrese el sueldo"))



#-3 Cálculo de áreas y perímetro de 4 figuras básicas

# CUADRADO
#- Cálculo del área del cuadrado
print(" - Área del Cuadrado -")

# Ingreso de de los valores
lado1C =float(input("Ingrese el primer lado: "))

áreaC= lado1C*lado1C
print(" El área es: ",áreaC) 


#- Cálculo del perímetro del cuadrado
print("- Perímetro del Cuadrado -")

# Ingreso de los valores
long1C =float(input("Ingrese el valor del primer lado: "))
long2C =float(input("Ingrese el valor del segundo lado: "))
long3C =float(input("Ingrese el valor del tercer lado: "))
long4C =float(input("Ingrese el valor del cuarto lado: "))

perímetroC= long1C+long2C+long3C+long4C
print(" El perímetro del cuadrado es: ",perímetroC)



#TRIANGULO
#- Cálculo del área de un Triángulo

print(" - Área de un Triángulo - ")

# Ingreso de los valores
baseT =float(input(" Ingrese la base: "))
alturaT =float(input("Infrese la altura: "))

áreaT= baseT*alturaT/2
print("El área es: ",áreaT)


#- Cálculo del perímetro de un Triángulo
print(" - Perímetro de un Triángulo -")

#Ingreso de los valores
Lado1T =float(input(" Ingrese el lado 1: "))
lado2T =float(input(" Ingrese el lado 2: "))
lado3T =float(input(" Ingrese el lado 3: "))

perímetroT= Lado1T+lado2T+lado3T
print(" El perímetro del Triángulo es: ",perímetroT)



# CIRCULO
#- Cálculo del área de un Circulo
print(" - Área de un Circulo - ")

#Ingreso de los valores
diametro =float(input("Ingrese el diametro: "))
radio= diametro/2

áreaCir= 3.14159*(radio*radio)
print(" El área del Circulo es: ",áreaCir)


#- Cálculo del perímetro de un Circulo
print(" - Perímetro de un Circulo -")

diametro =float(input(" Ingrese el diametro: "))

perímetrocir= 3.14159*diametro
print(" El perímetro del Circulo es: ", perímetrocir)



# RECTÁNGULO
#- Cálculo del área de un Rectángulo
print(" - Área de un Rectángulo - ")

# Ingreso de los valores
baseR =float(input(" Ingrese la Base: "))
alturaR =float(input(" Ingrese la Altura: "))

áreaR= baseR*alturaR
print(" El área del Rectángulo es de: ", áreaR)


#- Cálculo del perímetro de un Rectángulo
print(" - Perímetro de un Rectángulo - ")

# Ingreso de valores
lado1R=float(input(" Ingrese el primer lado: "))
lado2R=float(input(" Ingrese el segundo lado: "))

perímetroR= 2*lado1R + 2*lado2R
print(" El perímetro del Rectángulo es de: ",perímetroR)
