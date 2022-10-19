#encoding: utf-8

"""
author: John Jairo - JJLE
metodo de ordenamiento
quicksort

basado en recursividad
"""
import random as rd

def quicksort(l):
	"""
	funcion encargada de ordenar los 
	elementos de la lista pasada por 
	parametro
	"""
	left = []
	right = []
	pivot = 0

	if len(l) < 2:
		return l

	else:
		for i in range(1,len(l)):
			pivot = l[0]
			if l[i] < pivot:
				left.append(l[i])
			else:	
				right.append(l[i])

		left.append(pivot)
		
		return quicksort(left) + quicksort(right)


if __name__ == '__main__':
	l1 = [rd.randint(0,100) for i in range(0,10)]
	result = quicksort(l1)
	print("Original:\n{0}\nResultado asc:\n{1}\nResultado desc:\n{2}".format(l1,result,result[::-1]))
