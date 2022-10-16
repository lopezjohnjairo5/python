"""
programa generador de contrasennas
"""

import random as rd

def include_special_chars(word):
	"""
	funcion 'include_special_chars' 
	
	Encargada de agregar a la palabra pasada por parametro
	un numero aleatorio de caracteres especiales.
	
	params:
	- word (str): palabra con uno o mas caracteres.
	
	return
	- new_txt (str): palabra encriptada, mediante equivalencias
	"""
	new_txt = word
	special_chars = [chr(c) for c in range(35,39)]
	special_chars.append("*")
	special_chars.append("_")
	
	for i in range(0,3):
		pos_num = rd.randint(1,len(word)-1)
		num_sp_char = rd.randint(0,len(special_chars)-1)
		sp_char = special_chars[num_sp_char]
		new_txt = new_txt[:pos_num] + sp_char + new_txt[pos_num:]
	
	return new_txt
	
	
def change_letters(word):
	"""
	funcion 'change_letters' 
	
	Encargada de modificar la palabra pasada por parametro
	mediante un diccionario con equivalencias
	
	params:
	- word (str): palabra con uno o mas caracteres.
	
	return
	- new_txt (str): palabra encriptada, mediante equivalencias
	"""
	new_txt = ""
	dictionary_eq = {
	"a":"u",
	"b":"o",
	"c":"t",
	"d":"v",
	"e":"p",
	"f":"i",
	"g":"z",
	"h":"q",
	"j":"y",
	"k":"r",
	"l":"s",
	"m":"x",
	"n":"w"
	}
	for l in word:
		if(l in dictionary_eq.keys()):
			new_txt += dictionary_eq[l] #localizamos el valor segun la clave
		elif(l in dictionary_eq.values()):
			new_txt += list(dictionary_eq.keys())[list(dictionary_eq.values()).index(l)] #localizamos la clave segun el valor	
		else:
			new_txt += l #concatenamos el valor sino esta en el diccionario 
	return new_txt		
	
	
def min_len(word,length):
	"""
	funcion 'min_len' 
	
	Encargada de modificar la palabra pasada por parametro
	agregando o eliminando valores a fin de cumplir
	con la longitud minima requerida
	
	params:
	- word (str): palabra con uno o mas caracteres.
	- length (int): numero entero que representa la longitud final de la palabra
	
	return
	- new_txt (str): palabra encriptada, con la longitud solicitada
	"""
	new_txt = word	
	
	while (len(new_txt) < length):
		val_num_alphabet = list_alphabet[rd.randint(0,len(list_alphabet)-1)]
		al_num = rd.randint(0,9)
		num_pos = rd.randint(1,len(new_txt)-1)
		new_txt = new_txt[:num_pos] + val_num_alphabet + str(al_num) + new_txt[num_pos:]

	return new_txt[:length]
	
	
def change_minus_may(word):
	"""
	funcion 'change_minus_may' 
	
	Encargada de modificar/cambiar letras de la palabra pasada por
	parametro, de mayusculas a minusculas y viceversa.
	
	params:
	- word (str): palabra con uno o mas caracteres.
	
	return
	- new_txt (str): palabra encriptada, con algunos valores mayusculas y minusculas
	"""
	new_txt = word
	
	for l in range(0,len(word)):
		num_al = rd.randint(0,1)
		
		if not (num_al == 0):
			new_txt = new_txt[:l] + new_txt[l].upper() + new_txt[l+1:]
		else: 
			new_txt = new_txt[:l] + new_txt[l].lower() + new_txt[l+1:] 
	
	return new_txt

def capture_len(msn = "Introduzca la longitud deseada para la contrasenna: "):
	"""
	funcion 'capture_len' 
	
	Encargada de capturar por teclado un numero entero 
	que representa una longitud o cantidad
	a generar 
	
	return
	- valor numerico (int)
	- False
	"""
	try:
		user_len_word = int(input(msn))
	except:
		return False
	else:
		return user_len_word	


def main():
	len_word = capture_len()
	while(not len_word):
		len_word = capture_len()
	
	word_base = list_words[rd.randint(0,len(list_words)-1)]
	n_word = change_letters(word_base)
	n_word = include_special_chars(n_word)
	n_word = min_len(n_word,len_word)
	n_word = change_minus_may(n_word)
	
	print("Palabra base: {0}\nLongitud: {1}\nContraseña: {2}".format(word_base, len_word,n_word))


if(__name__ == "__main__"):
	list_alphabet = [chr(i) for i in range(97,123)]
	list_words = [
	"perro",
	"gato",
	"conejo",
	"arroz",
	"hola",
	"mundo",
	"nuevo",
	"armpit",
	"heel",
	"finger",
	"navel",
	"ohayou",
	"gomen"]
	count_p = 0
	
	count_pass = capture_len("\nCuantas contraseñas desea generar? ")
	while(not count_pass):
		print("\nCantidad no valida. Por favor introduzca un numero entero. ")
		count_pass = capture_len("Cuantas contraseñas desea generar? ")
	
	for i in range(0,count_pass):
		print("\n"+"-"*10+str(i+1)+"-"*10)
		main()

