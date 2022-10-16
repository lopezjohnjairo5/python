#! /usr/bin/env python3

import numpy

print("-"*10+"EJERCICIOS - Formas de calcular PI. A\n"+"-"*10)


lista_v1 = [(4/1),(4/3),(4/5),(4/7),(4/9),(4/11)]
lista_v2 = [(8/(1*3)),(8/(5*7)),(8/(9*11)),(8/(13*15)),(8/(17*19)),(8/(21*23))]

def Function_PI(args,op = "minus" ):
	"""
	valor PI : (4/1) - (4/3) + (4/5) - (4/7) + (4/9) ...
	"""
	new_op = op
	while (len(args) > 1):
		if(op == "minus"):
			args[0] = args[0] - args[1]
			new_op = "plus"
		else:
			args[0] = args[0] + args[1]
			new_op = "minus"
		args.pop(1)
		Function_PI(args, new_op)
	pi_value = args[0]
	return	pi_value


def Function_PI2(args):
	"""
	valor PI : (8/(1*3)) + (8/(5*7)) + (8/(9*11))...
	"""
	while (len(args) > 1):
		args[0] = args[0] + args[1]
		args.pop(1)
		Function_PI2(args)
	pi_value2 = args[0]
	return pi_value2


def Function_difference(piv):
	"""
	1. resta el valor pasado por parametro del valor de PI 
		de numpy para saber la diferencia
	2. obtiene un valor en porcentaje que equivale a la diferencia 
		entre el valor pasado por parametro y el valor de PI de numpy
	"""
	error_difference = numpy.pi - piv
	
	#calculando mediante regla de 3
	"""
	si 3.1415... equivale al 100%
	cuanto equivale piv
	"""
	percentage = (100 * piv)/ numpy.pi
	percentage_difference = 100 - percentage
	print("\nValor calculado: {0}".format(piv))
	print("Valor de PI: {0}".format(numpy.pi))
	print("La diferencia entre numpy.pi y el valor calculado es: {0}".format(error_difference))
	print("El valor de pi calculado equivale a: {0}% de PI".format(round(percentage,3)))
	print("La diferencia entre el valor calculado y PI es de: {0}%".format(round(percentage_difference,3)))


pi1 = Function_PI(lista_v1)
pi2 = Function_PI2(lista_v2)
print(pi1)
print(pi2)
Function_difference(pi1)
Function_difference(pi2)
