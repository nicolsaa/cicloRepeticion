import os

os.system("cls") #limpiar
# gatito para comentar
nombre = "nicol" # tipo string -> caracter
genero = 'm' # tipo char
edad = 35 # tipo int -> entero
estatura = 1.80 # tipo float o double -> real
condicion = True # bolean -> logico
descuento = 0.90
#operadorY = and # &
#operadorO = or # -> || o
nombre2 = input("ingrese nombre\n") #solicitar y almacenar dato en variable
apellido = input("ingrese apellido\n")
edad = int(input("ingrese su edad\n")) #solicitar dato de tipo int
nombreCompleto = nombre2 +""+ apellido # concatenacion 
print (nombreCompleto) # imprimir o mostrar info
#print ("el descuento es de : "+ descuento + "y tu nombre es "+ nombreCompleto) #muy pseint
#print (f"el descuento es de:{descuento} y tu nombre es: {nombreCompleto}") #muy python
#ciclo conficion - if else
if edad > 18:
  print("eres mayor de edad")
elif edad > 0 and edad <= 17: #SiNoSi
  print ("eres menor de edad")
else: 
  print ("no existe esa edad :s")

#elif (anidado)
#ctrl + S (guardado automatico)
#ctrl + k + c (al seleccionar todo el texto comenta todo)
#ctrl + k + U (al seleccionar todo el texto lo descomenta)


