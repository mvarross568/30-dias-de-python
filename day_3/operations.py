age = 16 #1
height = 1.68 #2
complex_number = 4j #3
b = input("Cual es la base: ")
print(f"La base es {b}")
h = input("Cual es la altura: ")
print(f"La altura es {h}")
area_triangle = o.5 * b * h #4

a = input("Cual es el valor del lado a: ") #5
print(f"El valor del lado a es {a}")
b = input("Cual es el valor del lado b: ")
print(f"El valor del lado b es {b}")
c = input("Cual es el valor del lado c ")
print(f"El valor del lado c es {c}")
perimetrer = a + b + c
print(perimetrer)

lenght = input("Cual es el valor de la longitud del rectángulo") #6
print(f"El valor de la longitud es {lenght}")
width = input("Cual es el valor del ancho del rectángulo")
print(f"El valor del ancho es {width}")
area_of_rectangle = lenght * width
print(area_of_rectangle)
perimeter_of_rectangle  = 2 * (lenght + width)
print(perimeter_of_rectangle)

pi = 3.14
radius = input("Cual es el valor del radio: ") #7
area_of_circle = pi * radius * radius
print(area_of_circle)
circumference_of_circle = 2 * pi * radius
print(circumference_of_circle)

funcion1 = "y = 2x - 2" #8
print("Su función es: " +funcion1)
pendientef1 = str(2)
print("Su pendiente es: " +penfientef1)
interceptx= (2*0 -2)
print("el intercepto de x es:")
print(0,interceptx)
intercepty = (0+2)/2
print("el intercepto de y es:")
print(intercepty,0)

punto1=(2,2)
punto2=(6,10)
x1=2
x2=6
y1=2
y2=10
m= (y2-y1)/(x2-x1)
print(f"su pendiente es:{m}")
euclideandistance = (x2-x1)**2 + (y2-y1)**2
print(f"la distancia eucliana es de: {euclideandistance}")

print(pendientef1==m)

numeros_prueba= (2,-3,4,5,6)
for n in numeros_prueba:
    print(n**2 + 6*n +9)

print(len("python"))
print(len("dragon"))
print(len("python")!=len("dragon"))

print("on" in "python")
print("on" in "dragon")
print("jarcon" in "I hope this curse is not full of jargon")
print("on" not in "dragon")
print("on" not in "python")

lenghtpython = len("python")
print(lenghtpython)
print(float(lenghtpython))
print(str(lenghtpython))

numero = int(input("inserta un número cualquiera:"))
print(numero)
if numero%2 == 0:
    print("su numero es par")
else:
    print("su numero no es par")

print(7//3 == int(2.7))
print(type("10") == type(10))
print(int(9.8)==10)