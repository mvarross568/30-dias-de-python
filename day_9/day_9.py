a = int(input("Inserte su edad: ")) #level 1: 1
if a > 18: print("You are old enough to drive")
if a < 18: print(f"le faltan {18 - a} años para conducir")

b = int(input("Inserte su edad: "))
mi_edad = 16
if b < mi_edad:
    print(f"soy {mi_edad- b} años mayor que tú")
    
if b > mi_edad:
    print(f"Eres {b - mi_edad} años mayor que yo")

if b == mi_edad:
    print(f"Tienes la misma edad que yo")

n1 = int(input("inserta un número:"))
n2 = int(input("inserta otro número: "))
if n1 > n2:
    print(f"{n1} es mayor que {n2}")

if n1 <  n2:
    print(f"{n1} es menor que {n2}")

if n1 == n2:
    print(f"{n1} es igual que {n2}")

nota = int(input("¿ual es tu nota?: "))
A = 90, 100
B = 70, 89
C = 60,90
D = 50,59
F = 0, 49

if nota >= 90 and nota <= 100:
    print("You got an A")

elif nota >= 70 and nota <=89:
    print("You got a B")

elif nota >= 60 and nota <=69:
    print("You got a C")

elif nota >= 50 and nota <=59:
    print("You got a D")

elif nota >= 0 and nota <=49:
    print("You failed")


season = str(input("en que mes estamos "))
season_capitalized = season.capitalized()
Autumn = "september, october or november"
Winter = "december, january o febrruary"
Spring = "march, april or may"
Summer = "june, july or august"

if season_capitalized == "september" or season_capitalized == "october" or season_capitalized == "november":
    print(" it is Autumn")

elif season_capitalized == "december" or season_capitalized == "january" or season_capitalized == "february":
    print("it is winter")

elif season_capitalized == "march" or season_capitalized == "april" or season_capitalized == "may":
    print("it is spring")

elif season_capitalized == "june" or season_capitalized == "july" or season_capitalized == "august":
    print("it is summer")

fruits = ["banana", "orange", "mango", "lemon"]
new_fruit =str(input("dime una fruta: "))
season_capitalized = season.capitalize()

if new_fruit in fruits:
    print("la fruta ya esta en la lista")

else:
    fruits.append(new_fruit)
    print(fruits)