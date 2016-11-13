### Program UTS AI menggunakan GA
import random

### Setting Up
# Membuat konstanta
nK = 6 # Jumlah Kromosom dalam satu populasi
nG = 6 # Jumlah gen dalam satu kromosom
# Membuat fungsi-fungsi
def fungsiObjektif(kromosom):
	# dekode
	return 1.0
def fitness(kromosom):
	return 1.0/fungsiObjektif(kromosom)
def rouletteWheel(populasi, fitnesses):
	pass
def crossover(kromosom1,kromosom2):
	return 1, 2
def mutasi(kromosom):
	for i in range(len(kromosom)):
		kromosom[i] = 1 - kromosom[i]
def sortByFitness(population, fitnesses):
	pass


#Membuat populasi yang berisi kromosom kromosom
populasi = [[random.choice([0,1]) for x in range(nG)] for y in range(nK)] # mengisi populasi dengan kromosom random
fitnesses = [0.0 for x in range(nK)]

### Memulai pencarian solusi
for i in range(1):
	for i in range(nK):
		fitnesses.append(fitness(populasi[i]))
	sortByFitness(populasi, fitnesses)
	bestKromosom1, bestKromosom2 = populasi[0],populasi[1]
	populasiBaru = []
	while len(populasiBaru)<nK:
		p1,p2 = rouletteWheel(populasi,fitnesses), rouletteWheel(populasi,fitnesses)
		anak1,anak2 = crossover(p1,p2)
		anak1,anak2 = mutasi(anak1), mutasi(anak2)
		populasiBaru.extend([anak1,anak2])
	populasi = populasiBaru
	populasi[0], populasi[1] = bestKromosom1, bestKromosom2