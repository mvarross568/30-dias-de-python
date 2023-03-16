cont = 0 #level 1-1
while cont < 10:
    print(cont)
    cont = cont + 1
    
cont = 10 #level1-2
while cont > 0:
    print(cont)
    cont = cont - 1

for n in range (7): #level1-3
    print("#" * n )

for x in range(1,4): #level1-4
    for y in range (1,4):
        print ("# "*8)

numbers = (0,1,2,3,4,5,6,7,8,9,10) #level1-5
for number in numbers:
    if number == 3:
        continue

langs = ["Python", "Numpy", "Pmndas", "Django", "Flask"] #level1-6
for Langs in langs:
    print(1)

     