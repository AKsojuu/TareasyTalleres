#for es el mientras
i=1

for i in range(1,5):
    print(" Hola ",i)

    
#formas de uso del for
#Barrido en recorrido de variables
#imprime el contenido de una arraid

Frutas = ["Manzana","Pera","Naranja"]

for fruta in Frutas :
    
    #print(frutas)
    print(fruta)
    
    
#Barrido de por bucle

for letras in "phyton":
    print(letras)

#Recorre e imprime las letras o enteros de las variables

nombre = "Martin"
for i in nombre:
    print(i)


#imprimir numeros del 1 al 10
for i in range (1,11):
    print(i)
    
#deletrea la palabra Abecedario

Abecedario ="Abecedario" #no necesario

for letras in Abecedario:
    print(letras) 


#imprime los primeros 5 numeros elevados al cuadrado
for n in range (1,6):
    print(n**2)

   
#imprima el contenido de una lista
Lista=["1","2","3",4,5,6]
 
for l in Lista:
     print(l)


# Mostrar solo los numeros pares del 1 al 20
# numero

for numero in range (1,21):
    if numero %2 ==0:
        print (numero)

       
# Contador que sume del 1 al 100
sumar= 0
for i in range (1,100):
    sumar += i    
    print(i,sumar)
print(" Total",sumar)

# Imprimir un triangulo
for i in range(1,10):
    print(" *"*i)