import time
import os
import random
import sys

#Tarea de Heurística IA 2019-02
#Matías Robles, Cristobal Sanchez y Tamara Salgado

# Declaración de variables globales
numeros_in = [] # Lista que almacena el conjunto ingresado
recorridos = [] # Lista que almacena los números recorridos

cont = 0
sum_acum = 0
heur = 0
head = 0
# Adornos
porcentaje = '%'
pnt = '..........'


# Método que inicializa el programa (main)
def init():
	heur = 0
	head = 0
	numeros_in = llamada()
	resolve(numeros_in,heur,head)

# Método que lee el conjunto de entrada
def llamada():
	num = -1
	cont = 0
	while num != 0: # Mientras el numero ingresado sea distinto de 0 leo
		num = int(input())
		if num != 0:
			numeros_in.append(num)
	# barrita de carga inutil		
	while cont<=100:
		os.system ("clear")
		print('%sPROCESANDO%s'%(pnt,pnt))
		print("%s%s"%(cont, porcentaje))
		wt=int(random.randrange(3))
		time.sleep(0.2)
		nm=int(random.randrange(20))
		cont = cont+nm
		if cont>100:
			os.system ("clear")
			print('%sPROCESANDO%s'%(pnt,pnt))
			print('100%')
			break
	print('%s.COMPLETED.%s'%(pnt,pnt))
	return numeros_in


def resolve(numeros_in,heur,head):
	head = random.randrange(len(numeros_in))
	print("head afsdjasdf %d"%head)
	heur = 99999999999999999
	sum_acum = numeros_in[head]
	recorridos.append(numeros_in[head])
	print('Se agrego el %d como primer valor'%numeros_in[head])
	print('head: %d,heur: %d,sum_acum: %d'%(head,heur,sum_acum))
	head,heur=heuristic(heur,head,sum_acum)
	print('head: %d,heur: %d,sum_acum: %d'%(head,heur,sum_acum))
	if heur != 0:
		next_num(head,heur,sum_acum)
	print('RESULTADO')
	print(numeros_in)
	print(recorridos)

def heuristic(heur,head,sum_acum):
	print('entre a heuristic')
	heur_aux = 0
	num = numeros_in[0]
	print(numeros_in)
	for num in numeros_in:
		print("esto es un numero o es un indice? %d"%num)
		if (num in recorridos):
			print('este no %d'%num)
		else:
			heur_aux = sum_acum + num
			heur_aux = abs(heur_aux)
			print("aux %d"%heur_aux)
			if(heur_aux == 0):
				print('poto')
				heur = abs(heur_aux)
				head = numeros_in.index(num)
				recorridos.append(numeros_in[head])
				print('RESULTADO')
				print(numeros_in)
				print(recorridos)
				sys.exit(0)
				
			if heur_aux <= heur:
				heur = abs(heur_aux)
				head = numeros_in.index(num)
	print('se agrego %d'%(numeros_in[head]))
	recorridos.append(numeros_in[head])
	return head,heur

def next_num(head,heur,sum_acum):
	print('next')
	sum_acum = sum_acum + numeros_in[head]
	print("final s%d"%sum_acum)
	if(sum_acum == 0):
		print('RESULTADO')
		print(numeros_in)
		print(recorridos)
		return 'end'
	head,heur=heuristic(heur,head,sum_acum)
	if (heur != 0 and (len(recorridos) == len(numeros_in))):
		recorridos.clear()
		heur = 0
		sum_acum = 0
	resolve(numeros_in,heur,head)


init()