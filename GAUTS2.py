import random

nK = 6 
nG = 6 

def buatKromosom():
	kromosom = []
	while len(kromosom)<nG:
		node = random.choice("abcdef")
		if node not in kromosom:
			kromosom.append(node)
	return kromosom

print buatKromosom()

def nilaiNode(node):
	if node=='a':
		return 1
	elif node=='b':
		return 2
	elif node=='c':
		return 3
	elif node=='d':
		return 4
	elif node=='e':
		return 5
	else:
		return 6

def temukanJalurYangLayak(kromosom):
	while(kromosom[0]==1):
		pass

def fungsiObjektif(kromosom):
	#dekode
	biaya = 0.0