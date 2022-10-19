#encoding: utf-8

"""
author: John Jairo - JJLE
metodo de ordenamiento
burbuja
"""

import random as rd 


def switch_values(nl,order):
	"""
	funcion encargada de cambiar los valores
	de una lista segun sea uno mayor o menor
	"""
	if (order == "desc"):
		for i in range(0,len(nl)-1):
			if (nl[i+1] > nl[i]):
				n_pass = nl[i]
				nl[i] = nl[i+1]
				nl[i+1] = n_pass 
	else:
		for i in range(0,len(nl)-1):
			if (nl[i] > nl[i+1]):
				n_pass = nl[i+1]
				nl[i+1] = nl[i]
				nl[i] = n_pass 			

	return nl
				

def burble(l,order="asc"):
	"""
	funcion encargada del ordenamiento
	de una lista pasada por parametro
	"""
	nl = l

	# invocamos la operacion de ordenamiento
	# tantas veces como elementos tenga la lista
	for x in range(0,int(len(nl)-1)):
		nl = switch_values(nl,order)

	return nl


if(__name__ == '__main__'):
	#conjunto de numeros aleatorios . ejemplo con minima intervencion del  user
	"""
	numbers = [ rd.randint(0,60) for n in range(0,60) ]
	print(numbers)
	result = burble(numbers,"desc")
	print(result)
	"""
	numbers = []
	continue_add = True 	

	#capturamos el tipo de ordenamiento a realizar
	t_order = input("Ordenar de manera ascendente(a) ó descendente(d)? ").lower()

	if (t_order.startswith("a")):
		order = "asc"
	else:	
		order = "desc"

	#pedimos los valores a ordenar	
	#menu 1 - finito
	continue_add = int(input("Cuantos valores desea agregar (Número entero): "))
	for x in range(0,continue_add):
		try:
			numbers.append(int(input("#{0}-Introduzca un numero entero: ".format(x+1))))
		except:
			print("ERROR. Se requiere un numero entero.")
	
	#menu 2 - infinito
	"""
	while continue_add:
		try:
			numbers.append(int(input("Introduzca un numero entero: ")))
		except:
			print("ERROR. Se requiere un numero entero.")

		continue_add = (True if(input("Desea agregar otro valor(s|n): ").lower().startswith("s")) else False)
	"""
	print("Original: {0}".format(numbers))	
	result = burble(numbers,order)
	print("Ordenamiento: {0}\nResultado: {1}".format(order,result))