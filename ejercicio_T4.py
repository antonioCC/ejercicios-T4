import re
#patron = re.compile('a[3-5]+')# coincide con una letra, seguida de al menos 1 dígito entre 3 y 5
#print( input("Introduce un texto") );
archivo=open('datos.txt','r')
#print("el texto es: "+archivo.read())
mensaje=archivo.read()


print("ingresa un una opcion")
print("1: variables validas")
print("2: enteros y decimales")
print("3: operadores aritmeticos")
print("4: operadores relacionales")
print("5: palabras reservadas")
numero = int(input())

if numero==1:
	#variables validad
	patron = re.compile('\s[A-Za-z]+\;')
	print (patron.findall(mensaje))
	archivo.close()


if numero==2:
	#enteros y decimales
	patron = re.compile('\s([0-9]+(\d+)?\;|\d+\.+\d+\;)')
	print (patron.findall(mensaje))
	archivo.close()

if numero==3:
	#operadores aritmeticos
	patron = re.compile('[+*/-]')
	print (patron.findall(mensaje))
	archivo.close()

if numero==4:
	#operadores relacionales
	patron = re.compile('[<>=\!]')
	print (patron.findall(mensaje))
	archivo.close()

if numero==5:
	#palabras reservadas
	patron = re.compile('if|else|double|print')
	print (patron.findall(mensaje))
	archivo.close()

