#!/usr/bin/env python3
import subprocess
import time

def main():
	lista_act = ["1-actualizar software","2-potenciar rendimiento","3-limpiar sistema","4-eliminar paquetes antiguos","5-eliminar archivos en otros idiomas","6-desfragmentar raiz","s/S- salir","*-todas"]
	print("\nQue actividad desea desarrollar:\n")
	for i in range(0,len(lista_act)):
		print(lista_act[i])
	
	actividad = str(input("\nintroduzca el numero de actividad a desarrollar o * para desarrollar todas las actividades mencionadas:"))
	if(actividad.lower() != "s"):
		actividades(actividad)
	else:
		print("\nGracias por preferirnos, que tenga un buen día.")

		
def actividades(tarea):
	"""
	comandos probados en linux 100% funcionales
	"""
	print("\n\n"+"-"*10+"NOTA: La ejecución de algunas actividades puede requerir confirmación"+"-"*10+"\n\n")

	if(tarea == "1" or tarea == "*"):	
		print("\n"+"-"*20+"Actualizando software"+"-"*20+"\n")
		time.sleep(3)
		subprocess.call("sudo apt-get update",shell =True)
		
	if(tarea == "2" or tarea == "*"):
		print("\n"+"-"*20+"Potenciando rendimiento"+"-"*20+"\n")
		time.sleep(3)
		subprocess.call("sudo apt-get upgrade",shell =True)
	
	if(tarea == "3" or tarea == "*"):
		print("\n"+"-"*20+"Limpiando sistema"+"-"*20+"\n")
		time.sleep(3)
		subprocess.call("sudo apt-get autoclean",shell =True)
	
	if(tarea == "4" or tarea == "*"):
		print("\n"+"-"*20+"Eliminando paquetes antiguos"+"-"*20+"\n")
		time.sleep(3)	
		subprocess.call("sudo apt-get autoremove",shell =True)
	
	if(tarea == "5" or tarea == "*"):
		continuar = input("Confirma la eliminacion de archivos en otros idiomas?(s/n)")
		
		if (continuar.lower()=="s"):	
			print("\n"+"-"*20+"Eliminando archivos en otros idiomas"+"-"*20+"\n")
			time.sleep(3)	
			subprocess.call("sudo localepurge",shell =True)
		else:
			print("\n"+"-"*20+"Saltando eliminacion de archivos en otros idiomas"+"-"*20+"\n")
		
	if(tarea == "6" or tarea == "*"):
		print("\nAtención: esta acción hace uso de la herramienta e4defrag (instalar: sudo apt install e2fsprogs)\n")
		print("\n"+"-"*20+"Desfragmentando raiz '/'"+"-"*20+"\n")
		time.sleep(3)	
		subprocess.call("sudo e4defrag /",shell =True)
	
	
	
	print("\n"+"."*20+"Procesos Finalizados"+"."*20+"\n")		

if (__name__ =="__main__"):
	main()	
	
