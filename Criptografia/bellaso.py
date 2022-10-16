"""
cfrado bellaso
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


def convert_text_to_list(text):
    """
    funcion encargada de eliminar los espacios 
    y de convertir el texto pasado por parametro
    en una lista
    """
    new_text = ""
    list_content = []
    for i in text:
        if(i != " "):
            new_text += i
    
    list_content = list(new_text)  
    return list_content


def create_new_list(key,length):
    """
    funcion encargada de crear una lista
    mediante la repeticion de la clave    
    con una longitud igual o mayor al texto
    en claro 
    """
    new_list = []
    
    while len(new_list) <= length:
        for c in key:
            new_list.append(c)

    return new_list[0:length]


def bellaso_encryption(key_list,text_list,encryption_table):
    """
    funcion encargada de reemplazar las letras del texto en claro
    mediante el uso de la clave y una tabla (diccionario)
    """
    final_text = ""
    
    letter_key = encryption_table.keys()

    # ciclo para verificar uno a uno los caracteres de la clave
    for i in range(0,len(key_list)):
        #recorremos la lista de claves del diccionario
        for k in letter_key:
            #verificamos que coincida la letra de la clave introducida
            #con una de las letras puestas como clave en el diccionario     
            if(key_list[i] in k):
                #verificamos si la letra del texto en claro esta en la primera
                # o segunda parte del alfabeto y capturamos el indice,
                #luego usamos ese indice para obtener la letra, pero, en el otro
                #alfabeto ya que este seria su valor equivalente
                
                if(text_list[i] in encryption_table[k][0]):
                    index_c = encryption_table[k][0].index(text_list[i])
                    final_text += encryption_table[k][1][index_c]
                else:
                    index_c = encryption_table[k][1].index(text_list[i])
                    final_text += encryption_table[k][0][index_c]
    
    print("clave letras: {0} \ntexto claro: {1} \ntexto final: {2}".format(key_list,text_list,list(final_text)))
    

def main():
    #variables
    alphabet_part1 = [chr(c) for c in range(97,110)]
    alphabet_part2 = [chr(c) for c in range(110,123)] #esta parte deberia ser aleatoria


    #diccionario
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

    #imprimimos el contenido del diccionario
    for k,v in dictionary.items():
        print("{0} : {1}\n".format(k,v))

    #capturamos la clave y el texto que se cifrará
    key = input("Clave de cifrado: ").upper()
    text = input("Texto en claro: \n")

    #llamamos a las funciones para convertir texto en lista y crear nueva lista
    list_key = create_new_list(key,len(convert_text_to_list(text)))
    list_txt = convert_text_to_list(text)

    #por ultimo llamamos a la funcion encargada de crear el cifrado bellaso
    bellaso_encryption(list_key,list_txt,dictionary)
    
    
    
if __name__ == '__main__':
    main()    