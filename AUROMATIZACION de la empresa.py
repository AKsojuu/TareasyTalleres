#La empresa XYZ necesita automatizar los siguientes procesos
#-1 Control de temperatura
#-2 Valor de sueldos(diario, mensual, anual)
#-3 Cálculo de área y perímeto de 4 figuras básicas

# Login para el usuario de la empresa
print("                      - Bienvenido a la Empresa XYZ - ")
print("INGRESE AL SISTEMA")

for i in range (3):
# Definimos usuario y contraseña
    ussercorrecto = "administrador"
    contraseñacorrecta ="54321"
    
# Pedimos al usuario que ingrese sus datos
    nombre = input("\nIngresa tu nombre: ")
    usuario = input("Ingrese su usuario: ")
    contraseña= input("Ingrese su contraseña: ")

    if usuario == ussercorrecto and contraseña==contraseñacorrecta:
        print("                  ")
        print("                        -Acceso Concedido-")
        print("Bienvenido",nombre)
        
        #-1 CONTROL DE TEMPERATURA
        
        print("\nCONTROL DE TEMPERATURA")
        pregunta1=input("\n¿Desea Ejecutar el Control de Temperatura?  (si/no): ")

        if pregunta1 == "si":
            print("\n-La temperatura actual es de nivel 4: 5°C")
            
            temperatura =int(input(" Ingrese su nivel de temperatura: 1,2,3,4,5,6,7,8: "))
            
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
                print("\n Ingresó nivel",temperatura)
                print(f" Se ajustó la temperatura a: {valor} °C")

            # Indicación de la temperatura
                if valor < 0:
                    print(" Sensación térmica: Frío")
                elif valor <= 20:
                    print(" Sensación térmica: Templado")
                else:
                    print(" Sensación Térmica: Caliente")
            else:
                print(" \n*Opción inválida* ")
                print(" Por favor seleccione un nivel del 1 al 8.")
        else:
            print("\nNo se Ejecutará el Control de de temperatura ")
   
        # 2- CÁLCULO DE VALOR DE SUELDOS
        print("\nCÁLCULO DE VALOR DE SUELDOS ")
        pregunta2=input("\n¿Desea ejecutar el Cálculo?  (si/no):")
        
        if pregunta2=="si":
            # Ingreso de datos
            nombre = input("\n Nombre del trabajador: ")
            pagohora = float(input(" Ingrese el pago por hora : $"))
            horasdia = float(input(" Ingrese cuántas horas trabaja al día: "))
            diastrabajados = int(input(" Ingrese cuántos días trabajó este mes: "))
            # Cálculo de sueldo
            sueldo_diario = pagohora * horasdia
            sueldo_mensual = sueldo_diario * diastrabajados
            sueldo_anual = sueldo_mensual * 12

            # Mostramos los resultados
            print("\n-Datos")
            print(" Trabajador:", nombre)
            print(" Sueldo diario: $", round(sueldo_diario, 2))
            print(" Sueldo mensual: $", round(sueldo_mensual, 2))
            print(" Sueldo anual (estimado): $", round(sueldo_anual, 2))
            # Clasificamos el sueldo mensual
            if sueldo_mensual < 500:
                print(" Sueldo: Bajo ")
            elif sueldo_mensual <= 1500:
                print(" Sueldo: Medio ")
            else:
                print(" Sueldo: Alto ")
        else:
            print("\nNo se Ejecutará el Cálculo de Sueldos ")
            
            
        #-3 CÁLCULO DE ÁREAS Y PERÍMETROS DE 4 FIGURAS BÁSICAS
        print("\nCÁLCULO DE ÁREAS Y PERÍMETROS DE 4 FIGURAS BÁSICAS")
        
        # CUADRADO
        print("\n1-CUADRADO")

        #- Cálculo del área del cuadrado
        print("\n- Área del Cuadrado -")
        # Ingreso de de los valores
        lado1C =float(input(" Ingrese el primer lado: "))
        áreaC= lado1C*lado1C
        print("\n El área es: ",áreaC)   

        #- Cálculo del perímetro del cuadrado
        print("\n- Perímetro del Cuadrado -")
        # Ingreso de los valores
        long1C =float(input(" Ingrese el valor del primer lado: "))
        long2C =float(input(" Ingrese el valor del segundo lado: "))
        long3C =float(input(" Ingrese el valor del tercer lado: "))
        long4C =float(input(" Ingrese el valor del cuarto lado: "))
        perímetroC= long1C+long2C+long3C+long4C
        print("\n El perímetro del cuadrado es: ",perímetroC)

        #TRIÁNGULO
        print("\n2-TRIÁNGULO")

        #- Cálculo del área de un Triángulo
        print("\n- Área de un Triángulo - ")
        # Ingreso de los valores
        baseT =float(input(" Ingrese la base: "))
        alturaT =float(input(" Ingrese la altura: "))
        áreaT= baseT*alturaT/2
        print("\n El área es: ",áreaT)
        
        #- Cálculo del perímetro de un Triángulo
        print("\n- Perímetro de un Triángulo -")
        #Ingreso de los valores
        Lado1T =float(input(" Ingrese el lado 1: "))
        lado2T =float(input(" Ingrese el lado 2: "))
        lado3T =float(input(" Ingrese el lado 3: "))
        perímetroT= Lado1T+lado2T+lado3T
        print("\n El perímetro del Triángulo es: ",perímetroT)

        # CIRCULO
        print("\n3-CÍRCULO")

        #- Cálculo del área de un Círculo
        print("\n- Área de un Círculo - ")
        #Ingreso de los valores
        diametro =float(input(" Ingrese el diametro: "))
        radio= diametro/2
        áreaCir= 3.14159*(radio*radio)
        print("\n El área del Círculo es: ",áreaCir)

        #- Cálculo del perímetro de un Circulo
        print("\n- Perímetro de un Círculo -")
        diametro =float(input(" Ingrese el diametro: "))
        perímetrocir= 3.14159*diametro
        print("\n El perímetro del Círculo es: ", perímetrocir)

        # RECTÁNGULO
        print("\n4-RECTÁNGULO")

        #- Cálculo del área de un Rectángulo
        print("\n- Área de un Rectángulo - ")
        # Ingreso de los valores
        baseR =float(input(" Ingrese la Base: "))
        alturaR =float(input(" Ingrese la Altura: "))
        áreaR= baseR*alturaR
        print("\n El área del Rectángulo es de: ", áreaR)
        
        #- Cálculo del perímetro de un Rectángulo
        print("\n- Perímetro de un Rectángulo - ")
        # Ingreso de valores
        lado1R=float(input(" Ingrese el primer lado: "))
        lado2R=float(input(" Ingrese el segundo lado: "))
        perímetroR= 2*lado1R + 2*lado2R
        print("\n El perímetro del Rectángulo es de: ",perímetroR)
        break
    
    else:
        print(" \nUsuario incorrecto ")
        print(" ACCESO DENEGADO")
