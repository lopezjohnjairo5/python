"""
practica de web scrapping
"""


import requests
from bs4 import BeautifulSoup

def save(dict):
    with open("departamentos_y_capitales_colombia.txt",mode="a") as f:
        for c,v in dict.items():
            f.write("{0} : {1}\n".format(c,v))

def main():

    r = requests.get('https://libretilla.com/departamentos-colombia-capitales/')
    #r = requests.get("https://www.datos.gov.co/d/xdk5-pm3f/visualization")
    soup = BeautifulSoup(r.text,"lxml")
    #dictionary = soup.tbody.descendants #muestra todos los hijos de la etiqueta seleccionada (tbody)
    """
    dictionary_departments = soup.find_all('td', class_="column-1") #busqueda con mayor precision con etiqueta y clase aplicada
    dictionary_cities = soup.find_all('td', class_="column-2")

    for i in dictionary_departments:
        print(i.text)

    for j in dictionary_cities:
        print(j.text)
    """
    new_dict = {}
    dictionary = soup.find_all('td') #buscamos todos los elementos html que tengan "td" como etiqueta

    #recorremos el diccionario poniendo como clave el departamento y como valor la ciudad/capital 
    for i in range(0,len(dictionary),2):
        new_dict[dictionary[i].text] = dictionary[i+1].text #.text devuelve solo el string que corresponde al texto de la etiqueta html
        
    for c,v in new_dict.items():
        print("departamento: {0} ; ciudad: {1}".format(c,v))    

    return new_dict

if(__name__ == "__main__"):
    d = main()
    save(d)