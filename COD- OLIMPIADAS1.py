def suma(a,b):
  x = a + b
  return x

def resta(a,b):
  x= a - b
  return x

print ("Dame el primer número")
a = int(input())
print ("Dame el segundo número")
b = int(input())
print ("La suma da", suma(a,b), "y la resta de", resta(a,b))

#1era ronda

def multiplicación(a,b):
  x = a*b
  return x

def división(a,b):
  x = a/b
  return x

print ("Dame el primer número")
a = int(input())
print ("Dame el segundo número")
b = int(input())
print ("La multiplicación da", multiplicación(a,b), "y la división da", división(a,b))

#2da ronda

def conversión():
  print ("¿Cuantos kilometros recorriste")
kilometros = int(input())
metros = kilometros*1000
print("Los metros que recorriste fueron", metros)


#3ra ronda

def area_triángulo(base, altura):
  x = (base*altura)/2
  return x
  
print("¿Cual es tu base?")
base = int(input())
print ("¿Cual es tu altura?")
altura = int(input())
print ("El área de tu triángulo es de", area_triángulo(base,altura))

