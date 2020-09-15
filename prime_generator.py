from sys import exit
from datetime import datetime
from math import sqrt

n = 0
zestawy = []
zestawy_unikalne = []
zestawy_slownik = {}

print("Wczytywanie zakresow z pliku")
print(datetime.now())

with open('test.txt') as file:
  lines = file.readlines()

counter = 0
for i in lines:
  if counter == 0:
    n = int(i)
  else:
    zestawy.append(list(map(int, i.split())))
  counter += 1

print("Parsowanie zmiennych wejsciowych")
print(datetime.now())

max_wartosc = 1
for i in range(0, n):
	# zestawy.append(list(map(int, input().split())))
	
	a = zestawy[i][1]
	if a > max_wartosc:
		max_wartosc = a
	
	try:
		indx = zestawy_unikalne.index(zestawy[i]) 
		zestawy_slownik.setdefault(indx, []).append(i)
	except ValueError:
		zestawy_slownik.setdefault(len(zestawy_unikalne), []).append(i)
		zestawy_unikalne.append(zestawy[i])
		

lenz = len(zestawy)
wyniki_zestawy = [0] * n
xlen = len(wyniki_zestawy)
pierwsze = [True for x in range(0, max_wartosc+1)]
plen = len(pierwsze)

print("Wyliczenie liczb pierwszych dla najwiekszego przedzialu")
print(datetime.now())

for i in range(2, int(sqrt(plen-1))+1):
	if pierwsze[i] != False:
		pierwsze[i+i::i] = [False] * ((plen-1)//i-1)

print("Przypisanie liczb pierwszych do zestawow")
print(datetime.now())

for i in zestawy_slownik:
  liczba = len([x for x in pierwsze[zestawy[i][0]:zestawy[i][1]+1] if x == True])
  for j in zestawy_slownik[i]:
      wyniki_zestawy[j] = liczba
	# leng = zestawy[i][1] - zestawy[i][0] + 1
	# pierwsze.count(True)
	
	# kk = len([x for x in pierwsze[zestawy[i][0]:zestawy[i][1]+1] if x == True])
	# kk = 0
	# indx = zestawy[i][0]-1
	# while indx > -1:
	# 	try:
	# 		indx = pierwsze.index(True, indx+1, zestawy[i][1]+1)
	# 		kk += 1
	# 	except ValueError:
	# 		indx = -1
	
	# wyniki_zestawy[i] = kk
	
	# kk = 0
	# for j in range(zestawy[i][0], zestawy[i][1]+1):
	# 	if pierwsze[j] != False:
	# 		kk += 1
	
	# pierwsze_zestaw = pierwsze[zestawy[i][0]:zestawy[i][1]+1]
	# leng = zestawy[i][1]+1
	# wyniki_zestawy[i] = len(pierwsze_zestaw) - pierwsze_zestaw.count(False)
	

# print(datetime.now())
# for i in pierwsze:
#   if i != False:
#     for k in range(0, xlen):
#         if i >= zestawy[k][0] and i <= zestawy[k][1]:
#           wyniki_zestawy[k] += 1
# print(datetime.now())


# for k in range(0, xlen):
  # temp_pierwsze = pierwsze[zestawy[k][0]:zestawy[k][1]+1]
  # temp2_pierwsze = [x for x in temp_pierwsze if x != False]
  # wyniki_zestawy[k] = len(temp2_pierwsze)

print("Wypisanie ilości liczb pierwszych dla kazdego zestawu")
print(datetime.now())

for i in wyniki_zestawy:
	print(i)

print("Koniec")
print(datetime.now())
