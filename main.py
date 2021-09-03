""" Reto 2 La puerta del castillo 
    Juan Sebastian Gamba Jacomussi
    Mayo 3-2021 """


print("+++La puerta del castillo+++")
print("+++Calculadora+++")

longitud_puerta = float(input("Escriba longitud de la puerta (Mts): "))
diametro_polea = float(input("Escriba el diametro de la polea (cms): "))
tiempo_cierre = float(input("Escriba el tiempo en el que desea cerrar la puerta (min.): "))

import math

def convertir_mtsacms():
  #Calcule la conversion de mts. a cms.
  longitud_puerta_cms = longitud_puerta * 100
  return longitud_puerta_cms


def calcular_radio_polea():
  #Calcule el radio de la polea
  radio = diametro_polea / 2
  return radio


def convertir_minaseg():
  #calcule conversión de min. a seg. 
  seg = tiempo_cierre * 60
  return seg 
 
def calcular_perimetro_polea():
  #Calcule el perimetro de la polea
  perimetro = 2 * math.pi * r
  return perimetro

lp = convertir_mtsacms()
r = calcular_radio_polea()
s = convertir_minaseg() 
perimetro_polea = calcular_perimetro_polea()

def calcular_nro_vueltas():
  #calcule el numero de vueltas que da la polea
  nv = lp / perimetro_polea
  return nv

nro_vueltas = calcular_nro_vueltas() 

#calcule el numero de hombres necesario
def calcular_nro_hombres():
  nh = nro_vueltas / 3
  redondeado = math.ceil(nh) #Se redonde al numero para trabajar con numero exactos 
  return redondeado

nro_hombres = calcular_nro_hombres()

def calcular_tiempo():
  #calcular velocidad angular
  w = nro_vueltas * 2 * math.pi / s
  #Calcular velocidad lineal
  v = w * r
  return v
  
velocidad = calcular_tiempo()


print("El numero de vueltas necesarias en la polea para cerrar la puerta completamente es:",nro_vueltas)
print("El numero de hombres necesarios para cerrar la puerta es:", nro_hombres)
print("Para cerrar la puerta en el tiempo estipulado la polea debe girar a una velocidad de:",velocidad,"cm/s")
