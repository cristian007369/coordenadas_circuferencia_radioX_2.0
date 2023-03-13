# Programa que permite obtener las coordenadas de una circuferencia 2.0

print("---------------------------------------------")
print("-------------Coordenadas (x,y)---------------")
print("---------------------------------------------")

# Input

import math
radio=int(input("Dígite el valor del radio: "))
n=int(input("Dígite en cuantas partes quieres dividir la circuferencia: "))
decimas=int(input("Ingrese el número de decimales máximo que quieres ver: "))
print("---------------------------------------------")
print("("+str(radio)+",0)")
angulo=math.pi*2/n
a=1

# Processing y output

while n!=a:
    contador=angulo*a
    a=a+1
    y=round(math.sin(contador)*radio,decimas)
    x=round(math.cos(contador)*radio,decimas)
    print("("+str(x)+","+str(y)+")")
