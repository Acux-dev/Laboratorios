#ejercicio 1
for x in range(21):
  print(x,x**3)

#ejercicio 2
for x in range(10,0,-1):
  print(x)
print("Feliz año nuevo!!!")

#ejercicio 3
for i in [0,1,2,3,4]:
  print ("Hola")

#ejercicio 4
for i in range(5):
  print ("Ahora i vale",i,"y su cuadrado", i**2)

#ejercicio 5
for i in ['JLo', 'Benito', 'Rosalia', 2021]:
  print ("Hola. Ahora i vale",i)

#ejercicio 6
for n in range(8):
  print(n)

#ejercicio 7
for n in range(1,13):
  print(n)

#ejercicio 8
c = 0
for i in range(1000):
    ultimo_digito = (i ** 3) % 10
    if ultimo_digito == 7:
        c = c + 1
print(c)

#bucles anidados
for i in range (5):
  for j in range(3):
    print ("i vale", i, "y j vale", j)

for i in range (6):
  for j in range(i):
    print ("i vale", i, "y j vale", j)