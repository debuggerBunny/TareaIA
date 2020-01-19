import time
import os
import random
import sys

#Tarea de Heurística IA 2019-02
#Matías Robles, Cristobal Sanchez y Tamara Salgado

numeros_in = []
recorridos = []
indices = []

cont = 0
contador = 0
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
	contador = 0
	numeros_in = llamada()
	for i in numeros_in:
		indices.append('x')
	resolve(numeros_in,heur,head,indices)

# Método que lee el conjunto de entrada
def llamada():
	num = -1
	cont = 0
	while num != 0: 
		num = int(input())
		if num != 0:
			numeros_in.append(num)
	# barrita de carga inutil ( PARA EJECUCIÓN MÁS RÁPIDA COMENTAR TODO HASTA EL PROXIMO COMENTARIO)
	while cont<=100:
		os.system ("clear")
		print('%sPROCESANDO%s'%(pnt,pnt))
		print("%s%s"%(cont, porcentaje))
		time.sleep(0.2)
		nm=int(random.randrange(20))
		cont = cont+nm
		if cont>100:
			os.system ("clear")
			print('%sPROCESANDO%s'%(pnt,pnt))
			print('100%')
			break
	print('%s.COMPLETED.%s'%(pnt,pnt))
	# COMENTAR HASTA ACA! PARA MÁS VELOCIDAD!, pero dejar para más placer
	return numeros_in


def resolve(numeros_in,heur,head,indices):
	head = random.randrange(len(numeros_in))
	heur = sys.maxsize
	sum_acum = numeros_in[head]
	recorridos.append(numeros_in[head])
	indices[head] = head
	head,heur=heuristic(heur,head,sum_acum)
	while heur != 0:
		heur,indices=next_num(head,heur,sum_acum)
	print('CONJUNTO DE ENTRADA')
	print(numeros_in)
	print('SUBCONJUNTO DE SALIDA')
	print(recorridos)

def heuristic(heur,head,sum_acum):
	heur_aux = 0
	num = numeros_in[0]
	for num in numeros_in:
		ind = numeros_in.index(num)
		if ( ind in indices):
			print('')
		else:
			heur_aux = sum_acum + num
			heur_aux = abs(heur_aux)
			if(heur_aux == 0):
				heur = abs(heur_aux)
				head = numeros_in.index(num)
				recorridos.append(numeros_in[head])
				indices[head] = head
				print('CONJUNTO DE ENTRADA')
				print(numeros_in)
				print('SUBCONJUNTO DE SALIDA')
				print(recorridos)
				sys.exit(0)
			if heur_aux <= heur:
				heur = abs(heur_aux)
				head = numeros_in.index(num)
	recorridos.append(numeros_in[head])
	indices[head] = head
	return head,heur

def next_num(head,heur,sum_acum):
	sum_acum = sum_acum + numeros_in[head]
	head,heur=heuristic(heur,head,sum_acum)
	if (heur != 0 and (len(recorridos) == len(numeros_in))):
		recorridos.clear()
		c = 0
		for i in numeros_in:
			indices[c] = 'x'
			c += 1
		heur = 0
		sum_acum = 0
		resolve(numeros_in,heur,head,indices)
	return heur,indices


init()