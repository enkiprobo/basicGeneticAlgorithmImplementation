### Program UTS AI menggunakan GA
import random

### Setting Up
# Membuat konstanta
nK = 100 # Jumlah Kromosom dalam satu populasi
nG = 13 # Jumlah gen dalam satu kromosom
pJ = [0.1,0.234,0.167,0.1,0.067,0.4,0.25,0.3,0.067,0.067,0.15,0.15,0.15] # panjang masing2 jalur
cP = 0.8 # crossover probability
mP = 0.2 # mutation probality
jG = 200 # jumlah Generasi

# Membuat fungsi-fungsi
def fungsiObjektif(kromosom):
	# menghitung panjang dari gen kromosom yang dipilih
	panjang = sum([x*y for x,y in zip(kromosom,pJ)])
	# cek ke valid-an kromosom
	if sum(kromosom[:3]) != 1:
		panjang +=1000
	if sum(kromosom[5:8]) !=1:
		panjang +=1000
	if sum(kromosom[10:13]) !=1:
		panjang +=1000

	if kromosom[3]*(kromosom[4]+kromosom[2]+kromosom[1]) > 1:
		panjang += 1000
	if kromosom[4]*(kromosom[3]+kromosom[2]+kromosom[1]) > 1:
		panjang += 1000
	if kromosom[3]*kromosom[2]==1 :
		panjang += 1000*(1-kromosom[4])
	if kromosom[4]*kromosom[0]==1:
		panjang += 1000*(1-kromosom[3])

	if kromosom[5]*(kromosom[0]+kromosom[3])>1:
		panjang += 1000
	if kromosom[6]*(kromosom[3]+kromosom[4]+kromosom[1])>1:
		panjang += 1000
	if kromosom[7]*(kromosom[4]+kromosom[2])>1:
		panjang += 1000
	if kromosom[5]==1:
		if kromosom[2]==1:
			panjang += 1000*(1-kromosom[4]*kromosom[3])
		elif kromosom[1]==1:
			panjang += 1000*(1-kromosom[3])
	if kromosom[6]==1:
		if kromosom[0]==1:
			panjang += 1000*(1-kromosom[3])
		elif kromosom[2]==1:
			panjang += 1000*(1-kromosom[4])
	if kromosom[7]==1:
		if kromosom[0]==1:
			panjang += 1000*(1-kromosom[4]*kromosom[3])
		elif kromosom[1]==1:
			panjang += 1000*(1-kromosom[4])

	if kromosom[8]*(kromosom[9]+kromosom[5]+kromosom[6]) > 1:
		panjang += 1000
	if kromosom[9]*(kromosom[8]+kromosom[7]+kromosom[6]) > 1:
		panjang += 1000
	if kromosom[8]*kromosom[7]==1:
		panjang += 1000*(1-kromosom[9])
	if kromosom[9]*kromosom[5]==1:
		panjang += 1000*(1-kromosom[8])

	if kromosom[10]*(kromosom[8]+kromosom[5])>1:
		panjang += 1000
	if kromosom[11]*(kromosom[9]+kromosom[8]+kromosom[6])>1:
		panjang += 1000
	if kromosom[12]*(kromosom[9]+kromosom[7])>1:
		panjang += 1000
	if kromosom[10]==1:
		if kromosom[7]==1:
			panjang += 1000*(1-kromosom[9]*kromosom[8])
		elif kromosom[6]==1:
			panjang += 1000*(1-kromosom[8])
	if kromosom[11]==1:
		if kromosom[5]==1:
			panjang += 1000*(1-kromosom[8])
		elif kromosom[7]==1:
			panjang += 1000*(1-kromosom[9])
	if kromosom[12]==1:
		if kromosom[5]==1:
			panjang += 1000*(1-kromosom[8]*kromosom[9])
		elif kromosom[6]==1:
			panjang += 1000*(1-kromosom[9])

	return panjang

def fitness(kromosom):
	return 1.0/fungsiObjektif(kromosom)

def rouletteWheel(populasi, fitnesses):
	prob = [x/sum(fitnesses) for x in fitnesses] # probability masing2 populasi
	nRandom = random.random() 
	# roulette wheel
	i = 0
	while nRandom>sum(prob[:i]) and i<nK-1:
		i +=1

	return populasi[i]

def crossover(kromosom1,kromosom2):
	# one point crossover
	# point di mulai di gen ke 2
	anak1, anak2 = [x for x in kromosom1],[x for x in kromosom2]
	anak1[3:],anak2[3:] = anak2[3:],anak1[3:]
	
	return anak1, anak2

def mutasi(kromosom):
	# mutasi menggunakan flip
	# hanya ada beberapa gen saja yang bermutasi tergantung dari mutation probability nya
	for genKe in [random.randint(0,nG-1) for x in range(int(mP*nG))]:
		kromosom[genKe] = 1 - kromosom[genKe]

def sortByFitness(population, fitnesses):
	for i in range(nK-1):
		j = i+1
		while fitnesses[j]>fitnesses[j-1] and j>0:
			fitnesses[j-1],fitnesses[j] = fitnesses[j],fitnesses[j-1]
			population[j-1],population[j] = population[j],population[j-1]
			j -= 1

# memulai generasi
populasi = [[random.choice([0,1]) for x in range(nG)] for y in range(nK)] # mengisi populasi dengan kromosom random
fitnesses = []
for j in range(nK):
	fitnesses.append(fitness(populasi[j]))
sortByFitness(populasi, fitnesses)

# ### Memulai pencarian solusi
for i in range(jG):
	bestKromosom1, bestKromosom2 = [x for x in populasi[0]],[x for x in populasi[1]]
	populasiBaru = []
	while len(populasiBaru)<nK:
		p1,p2 = rouletteWheel(populasi,fitnesses), rouletteWheel(populasi,fitnesses)
		# while berikut digunakan untuk menghindari crossover dengan diri sendiri
		while fitness(p1) == fitness(p2):
			p2 = rouletteWheel(populasi,fitnesses)
		if random.random() < cP:
			anak1,anak2 = crossover(p1,p2)
		else:
			anak1,anak2 = p1,p2
		mutasi(anak1)
		mutasi(anak2)
		populasiBaru.extend([anak1,anak2])
	populasi = populasiBaru
	populasi[0], populasi[1] = bestKromosom1, bestKromosom2
	for j in range(nK):
		fitnesses[j] = fitness(populasi[j])
	sortByFitness(populasi, fitnesses)
	# melihat populasi terbaik di tiap generasi
	print fitness(populasi[0]), populasi[0], fungsiObjektif(populasi[0])

# jawaban yang benar
# [1,0,0,1,0,0,1,0,0,0,0,1,0]


# populasi = [[1,1,0,1,0,0,1,0,0,0,0,1,0],
# [1,0,0,1,0,0,1,1,1,0,0,1,0],
# [1,0,0,1,0,0,1,0,0,1,1,1,1],
# [1,0,0,1,1,0,1,0,1,0,1,1,1],
# [1,1,1,1,1,1,1,0,0,0,0,1,0],
# [1,0,0,1,0,0,1,0,0,0,0,1,0]]
# print fitness(populasi[0])

# anak1, anak2 = crossover(populasi[0],populasi[1])
 
# for j in range(nK):
# 	fitnesses.append(fitness(populasi[j]))
# sortByFitness(populasi, fitnesses)

print fitness(populasi[0]), populasi[0], fungsiObjektif(populasi[0])