
import requests
from bs4 import BeautifulSoup

def save(dict):
    """
    funcion encargado de guardar en un txt los departamentos 
    y sus ciudades
    """
    with open("departamentos_ciudades.txt",mode="a") as f:
        for c in dict.keys():
            for i in dict[c]:
                f.write("{0}:{1}\n".format(c,i))

def main():
    """
    funcion encargada de obtener la informacion correspondiente
    de departamentos y ciudades, mediante web scraping
    """
    
    list_numbers = [n for n in range(0,10)]

    url = requests.get("https://es.wikipedia.org/wiki/Anexo:Municipios_de_Colombia_por_%C3%A1rea")
    url_content = BeautifulSoup(url.text,"lxml")
    dictionary = url_content.find_all('td')#buscando etiquetas td en la web

    new_dict = {}
    list_cities = []
    
    #añadiendo claves al diccionario
    for i in range(0,len(dictionary),3):
        #añadiendo las claves al diccionario
        key_string = ((dictionary[i+1].text).lstrip()).strip("\n")
        new_dict[key_string] = []
    
    #añadiendo los municipios en la clave correspondiente
    for i in range(0,len(dictionary),3):
        key_string = ((dictionary[i+1].text).lstrip()).strip("\n")
        new_dict[key_string].append((dictionary[i].text).strip("\n"))

            
    #print(new_dict)
    return new_dict
    
   
if(__name__ == "__main__"):
    d = main()
    save(d)