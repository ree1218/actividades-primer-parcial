#Calculadora de descuento
def Calculadora_de_Descuento():
  print("¿Cuánto pagó en su cuenta?")
  pago = input()
  print("¿Cuánto tenía de descuento?")
  descuento = input()
  x = int(pago)*int(descuento)/100
  y = int(pago)-x
  print("Pagará $",y,"ya aplicando el descuento")
Calculadora_de_Descuento()

#Calculadora del área de un rectángulo
def Calculadora_de_area():
  print("¿Cuál es la longitud de tu rectángulo?")
  longitud = input()
  print("¿Cuál es el ancho de tu rectángulo?")
  ancho = input()
  x= int(longitud)*int(ancho)
  y= int(longitud)*2+int(ancho)*2
  print("El área de tu rectángulo es",x)
  print("Y el perímetro de tu rectánculo es",y)
Calculadora_de_area()
