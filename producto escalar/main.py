import numpy as np

def get_values_vector(v,count):
	"""
	funcion encargada de obtener, llenar y retornar
	un vector.
	"""
	v1 = []
	num = 0
	
	#creamos un ciclo que va capturando valores por teclado
	#y los almacena en el vector 1
	while num < count:
		value = float(input("Introduzca un valor para el vector {0}: ".format(v))) 
		v1.append(value)
		num +=1
		
	#retornamos el vector	
	return v1
	
	
def calculate_product(v1,v2):
	"""
	funcion encargada de calcular el producto escalar 
	dados 2 vectores
	"""
	#usamos numpy para calcular el producto escalar
	result = np.dot(v1,v2)
	
	#retornamos el calculo
	return result

if(__name__ == "__main__"):
	_continue = false
	 
	while 
	dim = int(input("Introduzca la dimension/tamaño del vector: "))

	print("\nvector 1\n")
	v1 = get_values_vector("1",dim)
	print("\nvector 2\n")
	v2 = get_values_vector("2",dim)	
	
	r = calculate_product(v1,v2)
	print(f"Vector1: {v1}\nVector2: {v2}\n\nResultado: {r}\n")
