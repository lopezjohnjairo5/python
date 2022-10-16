"""
cifra de sustitucion con alfabeto confeccionado
"""

alphabet = [chr(l) for l in range(97,123)]
alphabet_2 = [] #usamos un conjunto para almacenar el nuevo alfabeto

keyword = input("\nPalabra clave: ")
message = input("\nMensaje a encriptar: ")
encrypted_message = ""

#ubicamos la ultima letra de la palabra clave
end_word = keyword[len(keyword)-1]


#agregamos la palabra clave a la segunda lista
for l in keyword:
    #evitamos que se agreguen espacios en blanco
    if(l != "" and l != " " and l not in alphabet_2):
        alphabet_2.append(l)

#obtenemos el indice de la ultima letra de la clave en el alfabeto
first = alphabet.index(end_word)+1

#agregamos las letras al nuevo alfabeto, desde la ultima letra de la palabra clave
for i in range(first,len(alphabet)):
    #nos aseguramos de que la letra a agregar no esta en ya agregada
    if(alphabet[i] not in alphabet_2):
        alphabet_2.append(alphabet[i])

#completamos las 26 letras del nuevo alfabeto con las letras iniciales.
for i in range(0,first):
    #nos aseguramos de que la letra a agregar no esta en ya agregada
    if(len(alphabet_2) < 26 and (alphabet[i] not in alphabet_2)):
        alphabet_2.append(alphabet[i])

# recorremos cada letra del mensaje a encriptar y
# las ubicamos en el abecedario inicial,
# luego creamos el mensaje codificado
# haciendo uso de los indices anteriormente obtenidos

for l in message:
    if(l in alphabet):
        encrypted_message += alphabet_2[alphabet.index(l)]

print("\nMensaje encriptado : {0}".format(encrypted_message))    