"""
Num = 34    
num1 = 1.25
valor = "Hola Mundo De Python"
v1 = True
print(type(num1))

"""
#Las comillas sirven para comentar en Python
#****El: // sirve para que te imprima un entero****  
#print(f"El resultado es {divicion}")  
"""

#operaciones basicas
dato1 = 4
dato2 = 2
division = dato1 / dato2
potenciacion = dato1**dato2
print("El resultado de la operacion es:",potenciacion)
print("El resultado es: {0}".format(division))
print("El resultado es %d" % (division))


#Para pedir que escriban algo por teclado y lo almacene en una variable:
dato3 = int(input("Ingrese Primer numero a Dividir:"))
dato4 = int(input("Ingrese Segundo numero a Dividir:"))
division1 = dato3 // dato4
print("El Resultado de la Division Es: %d" % (division1))

#metodos lower(), upper(), tittle()

texto = "Hola Python desde casa arrazando"
print(texto.upper())

texto1 = "HOLA PYTHON ARRAZADOR ARAGAN CONVIERTE MINUSCULA LETRA"
print(texto1.lower)

texto2 = "hola python convirtiendo la primera letra de cada palabra en mayuscula"
print(texto2.title())

#Ejercicio 1:

pregunta = int(input("Hay carros a ingresar 1:Si, 2:No"))
precioPorHora = 1000
while pregunta != 2:
    

    horaLLegada = int(input("Ingrese Hora entrada:"))
    horaSalida = int(input("Ingrese Hora Salida:"))
    cantidadHoras= horaSalida -horaLLegada  
    totalApagar = cantidadHoras * precioPorHora
    print(totalApagar)
    pregunta = int(input("Hay carros a ingresar 1:Si, 2:No")) 
    if pregunta == 2:
        print("un placer cobre la plata")
        break  

#Ejercicio 2:

numDividendo = int(input("Digite Dividendo A Dividir:"))  
numDivisor = int(input("Digite divisor:")) 
numCociente = numDividendo / numDivisor
numResiduo = numDividendo % numDivisor

print(f"El Dividendo Es: {numDividendo}")
print(f"El Divisor Es: {numDivisor}")
print(f"El Cociente Es: {numCociente}")
print(f"El Residuo Es: {numResiduo}")

""" 
#Condicional IF
"""

if condicion :
    el codigo que esta dentro 
    y cierra 
Aqui

"""
#Condicional ELSE

#Ingresar Edad Del Usuario, Enseñe Si Es Mayor de Edad.
"""
nombreUsu = input("ingrese su nombre: ".title())
edad = int(input("ingrese su edad: ".title()))
if edad >= 18:
    print("eres mayor de edad:".title(),nombreUsu)
else:
    print("eres menor de edad:".title(),nombreUsu)
"""
    
#Condicional ELIF
""" 
elif condicion
    instruciones a ejecutar


num1 = int(input("ingrese numero: ".title()))
num2 = int(input("ingrese segundo numero: ".title()))
if num1>num2:
    print(num1,"Es Mayor")
       
elif num1<num2: 
    print(num2,"Es Mayor")
       
else:
    print(f"{num1} y {num2} son iguales")
"""

#CONDICIONAL Y OPERADORES LOGICOS: and , or
#pedir al usuario la edad y a que grupo quiere pertenecer [Adultos/Infantes]. si el usuario tiene 18 años o mas y escoge 
#adultos muestre "Puede ingresar al grupo", de lo contrario "Excede la edad para pertenecer al grupo de infantes",de
#lo contrario  "no puede ingresar". si escoge una opcion diferente debe mostrar OPCION NO VALIDA




