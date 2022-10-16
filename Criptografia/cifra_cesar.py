"""
#cifra cesar
def cesar(texto, cant):
    alph_1 = [chr(i) for i in range(97,123)]
    #alph_2 = [chr(i) for i in range(122,96,-1)]
    cantidad = cant
    texto_cesar = ""

    for i in texto:
        if(i in alph_1):
            pos = alph_1.index(i)+int(cantidad)
            if( pos < len(alph_1)):
                texto_cesar += alph_1[pos]
            else:
                #print(pos - len(alph_1))
                texto_cesar += alph_1[ pos -(len(alph_1))]
    
    return texto_cesar

cantidad = input("\nDesplazamiento para el cifrado cesar: ")
texto_claro = input("Introduzca una palabra o frase a encriptar: ")
print("El texto en claro en cifra cesar es: {0}".format(cesar(texto_claro, cantidad)))
"""

#creando lista con el alfabeto en orden ascendente
alph_1 = [chr(i) for i in range(97,123)]

#capturando el valor de desplazamiento
displacement_number =""
while not displacement_number.isdigit():
    displacement_number = input("Introduzca valor de desplazamiento: ")

#capturando el texto a encriptar
text = input("Introduzca el texto a encriptar: ")
text_cesar = ""

# recorriendo el texto y creando el texto cifrado
for i in text:
    if(i in alph_1):
        #obtenemos la posicion de la letra y le sumamos el valor de desplazamiento
        pos = alph_1.index(i)+int(displacement_number)
        if( pos < len(alph_1)):
            #si el nuevo indice es menor a la longitud concatenamos el nuevo valor
            text_cesar += alph_1[pos]
        else:
            #si el nuevo indice es mayor a la longitud, lo recalculamos y concatenamos el nuevo valor
            text_cesar += alph_1[ pos -(len(alph_1))]


print("Lista: {0}".format(alph_1))
print("Texto claro: {0}".format(text))
print("Texto cifrado: {0}".format(text_cesar))