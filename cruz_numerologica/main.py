"""
programa encargado de
calcular los numeros de la loteria
segun la fecha actual
mediante el metodo de la cruz
numerologica

metodo antiguo -- el metodo moderno cambia la manera de reducir numeros
mediante la sumatoria

"""
import time
import tkinter as tk
from tkinter import messagebox

def window():
	"""
	crear ventana tkinter
	"""
	wind = tk.Tk()
	wind.title("Cruz numerológica")
	wind.geometry("300x150+10+10")
	return wind


def elements_to_window():
	"""
	poner elementos en la ventana
	"""
	w = window()
	var_el = tk.StringVar()
	input_el = tk.Entry(w,width=20, textvariable=var_el).place(x=10,y=14)

	var_label_el = tk.StringVar()
	var_label_el.set("Introduce la fecha a calcular \ndia mes y año, sin caracteres especiales \ny sin espacios. Ej: 12052022 => \ndia:12,mes:05,año:2022")
	label_el = tk.Label(w,textvariable=var_label_el,width=33,anchor="center").place(x=20,y=50)
	button_el = tk.Button(w,text="calculate",width=7,height=1,command= lambda : validate_click_btn(var_el.get(),var_label_el)).place(x=190,y=10)	
	w.mainloop()
		
def validate_click_btn(v1,v2):
	"""
	funcion encargada de validar que la casilla tenga un valor valido antes de 
	proceder a realizar los calculos correspondientes
	"""
	if(v1 != "" and v1.isnumeric()):
		main_calculate(v1,v2)
	else:
		msn = "el contenido de la casilla de texto debe ser de tipo númerico, sin espacios, sin caracteres especiales y no puede estar vacio, ej: 12092022 => dia:12, mes:septiembre, año:2022"
		messagebox.showerror(message=msn, title="Contenido no valido")	
		
def create_x(list_val):
	"""
	funcion encargada de crear los numeros
	finales a mostrar | 2 numeros de 4 digitos
	cada uno
	"""
	final_list = []
	#calculamos los numeros de la cruz
	v1 = calculate_num(list_val[0] + list_val[2])
	v2 = list_val[2]
	v3 = calculate_num(list_val[1] + list_val[2])
	v4 = calculate_num(v1+v3)

	#calculamos los numeros finales
	num1 = str(v1)+str(v2)+str(v3)+str(v4)
	num2 = str(calculate_num(v1+v2))+str(calculate_num(v2+v3))+str(calculate_num(v3+v4))+str(calculate_num(v4+v1))
	
	final_list.append(num1)
	final_list.append(num2)

	return final_list
	
def calculate_num(num):
	"""
	funcion encargada de convertir/reducir el numero
	a un numero de una sola cifra para seguir
	el proceso de sumatoria
	"""
	if (num > 9):
		v = num - 10 #metodo antiguo
		#v = (num - 10) + 1 #metodo moderno
	else:
		v = num

	return v		

def summation(l):
	"""
	funcion encargada de sumar los valores de una lista pasada
	por parametro y de generar una nueva lista
	con los valores nuevos. 
	return
		retorna una lista con 3 elementos
	"""
	l2 = []
	
	#recorriendo la lista pasada por parametro
	for i in range(0,len(l)-1):
		val1 = calculate_num(int(l[i]) + int(l[i+1]))
		l2.append(val1)
	
	return l2

def main_calculate(date,label_element):
	#fecha
	string_date = list(str(date))
	print("\n\t-Metodo antiguo-\n")
	print(f"fecha {string_date}")

	list_values = summation(string_date)

	#realizamos la operacion de sumatoria varias veces
	while len(list_values) > 2:
		list_values = summation(list_values)

	#incluimos al array final la ultima suma, para tener los valores minimos
	# para crear la cruz numerologica
	list_values.append(calculate_num(list_values[0] + list_values[1]))
	print(f"Reduccion {list_values}")

	#creamos la cruz con los valores finales resultantes
	final = create_x(list_values)
	print(f"numeros finales: {final}")
	
	#mostrando el contenido en tkinter
	final_content = "fecha: {0}\nReducción: {1}\nNúmeros finales: {2}".format(str(string_date), str(list_values), str(final))	
	label_element.set(final_content)
	
	
if __name__ == '__main__':
	elements_to_window()
	
