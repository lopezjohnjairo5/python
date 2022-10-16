"""
cifrado vigenere original
"""

def shuffle(min_value, array):
    """
    funcion encargada de pasar el primer 
    valor al final del array
    """
    new_array = []
    
    for i in range(min_value,len(array)):
        new_array.append(array[i])
    
    for e in range(0,min_value):
        new_array.append(array[e])
    
    return new_array


def delete_espace(text):
    """
    funcion encargada de eliminar los 
    espacios presentes en el texto en claro
    """
    final_text = ""
    
    for c in text:
        if(c != " "):
             final_text += c       

    return final_text


def create_list_par(key,text):
    """
    funcion encargada de crear una matriz 
    con los valores de la clave y el texto en claro
    """
    matriz = [list(key+text[:len(text)-1].upper()),list(text)]
    
    return matriz


def create_vigenere(text,dictionary):
    """
    funcion encargada de crear el cifrado vigenere
    """
    new_text = ""
    final_text = text
    keys_dict = list(dictionary.keys())
    #print(text)
    #print(keys_dict)
    
    #recorremos la clave
    for c in range(0,len(text[0])):
        #buscamos cada letra de la clave en las claves del diccionario
        for k in keys_dict:
            #si la letra de la clave coincide con algun valor de la clave del diccionario entonces...
            if(text[0][c] in k):
                #concatenamos a la variable "new_text" el valor del texto claro 
                #que se encuentre en la otra lista pero, en la misma posicion anterior
                try:
                    new_text += dictionary[k][1][dictionary[k][0].index(text[1][c])]
                except:
                    new_text += dictionary[k][0][dictionary[k][1].index(text[1][c])]

    final_text.append(list(new_text))
    return final_text


def main():
    #variables
    alphabet_part1 = [chr(c) for c in range(97,110)]
    alphabet_part2 = [chr(c) for c in range(110,123)] #esta parte deberia ser aleatoria

    dictionary = {
        'AB':(alphabet_part1,alphabet_part2),
        'CD':(alphabet_part1,shuffle(1, alphabet_part2)),
        'EF':(alphabet_part1,shuffle(2, alphabet_part2)),
        'GH':(alphabet_part1,shuffle(3, alphabet_part2)),
        'IJ':(alphabet_part1,shuffle(4, alphabet_part2)),
        'KL':(alphabet_part1,shuffle(5, alphabet_part2)),
        'MN':(alphabet_part1,shuffle(6, alphabet_part2)),
        'OP':(alphabet_part1,shuffle(7, alphabet_part2)),
        'QR':(alphabet_part1,shuffle(8, alphabet_part2)),
        'ST':(alphabet_part1,shuffle(9, alphabet_part2)),
        'UV':(alphabet_part1,shuffle(10, alphabet_part2)),
        'WX':(alphabet_part1,shuffle(11, alphabet_part2)),
        'YZ':(alphabet_part1,shuffle(12, alphabet_part2))
    }

    #imprimimos mensaje
    print("\n"*2+"*"*10+" CIFRADO VIGENERE ORIGINAL "+"*"*10+"\n"*2)

    #imprimimos el contenido del diccionario
    for k,v in dictionary.items():
        print("\t{0} : {1}\n".format(k,v))


    #capturamos la clave y el texto que se cifrará
    letter = input("letra para iniciar clave: ").upper()[0]
    text = input("Texto en claro: ")
    
    #llamamos a funcion para quitar espacios
    text_not_spaces = delete_espace(text)
    
    #llamamos a funcion para convertir el texto y el cifrado en listas
    list_text = create_list_par(letter,text_not_spaces)
    
    #llamamos a funcion encargada de crear el texto cifrado
    encript_text = create_vigenere(list_text,dictionary)
    
    #imprimimos la clave, el texto en claro y el texto cifrado
    for i in encript_text:
        print("\t {0}".format(i))
    
    print("\nClave creada: \t{0}".format("".join(encript_text[0])))
    print("Texto claro: \t{0}".format("".join(encript_text[1])))
    print("Texto cifrado: \t{0}".format("".join(encript_text[2])))
    
    
if __name__ == '__main__':
    main()    