<h1 align="center">	Ejercicios de herencia</h1>

<h2>Repositorio:</h2>

Este es el link del [repositorio](https://github.com/albabernal03/ejercicios_de_herencia)

***
<h2>¿De qué trata esta tarea?</h2>

En esta tarea hemos resuelto una serie de ejercicios, en los cuales se utiliza la herencia. Asimismo en cada uno de los ejercicios adjuntamos su UML.

***
## Indice

1. 44
2. e
3. e
4. e

***

## Ejercicio 1:

**código:**
```

class punto2D:
  def __init__(self,a1,a2,b1,b2):
    self.a1 = a1
    self.a2 = a2
    self.b1 = b1
    self.b2 = b2 
  def punto2d(a1,a2,b1,b2):
    print("A = X: {}".format(a1), " ; Y: {}".format(a2))
    print("B = X: {}".format(b1), " ; Y: {}".format(b2))
  print(punto2d) 
  def punto2dtranslacion(a1,a2,b1,b2):
    print("A = X: {}".format(a1), " ; Y: {}".format(a2))
    print("B= X: {}".format(b1), " ; Y: {}".format(b2))
  print(punto2dtranslacion)
  def sumapuntos(a1,a2,b1,b2):
    print("A = X: {}".format(a1), " ; Y: {}".format(a2))
    print("B= X: {}".format(b1), " ; Y: {}".format(b2))
  
print("Puntos iniciales:") 
print(punto2D.punto2d(1,2,4,6))
print("Puntos translacion:")
print(punto2D.punto2dtranslacion(5,3,0,1))
print("Puntos suma:")
print(punto2D.sumapuntos(1+5, 3+2, 4+0, 6+1))``
```


```
class punto3D():
  def __init__(self,c1,c2,c3):
    self.c1 = c1
    self.c2 = c2
    self.c3 = c3
  def punto3d(c1,c2,c3):
    print("C = X: {}".format(c1), " ; Y: {}".format(c2), ", Z :{}".format(c3) )
  print(punto3d) 
  def punto3dtranslacion(c1,c2,c3):
    print("C = X: {}".format(c1), " ; Y: {}".format(c2), ", Z :{}".format(c3) )
  print(punto3dtranslacion)
  def sumapuntos(c1,c2,c3):
   print("C = X: {}".format(c1), " ; Y: {}".format(c2), ", Z :{}".format(c3) )
   
print("Puntos iniciales:") 
print(punto3D.punto3d(1,2,4))
print("Puntos translacion:")
print(punto3D.punto3dtranslacion(5,3,0))
print("Puntos suma:")
print(punto3D.sumapuntos(1+5, 3+2, 4+0))

```


**UML:**


***



## Ejercicio 2:

**código:**
```
class Base: 
 
    def __init__(self): 
        self.a = "a" 
        self.b = "b" 
        self.c = "c" 
 
    def A(self): 
        print(self.a) 
 
    def B(self): 
        print(self.b) 
 
    def C(self): 
        print(self.c) 
 
class Derivada(Base): 
 
    def __init__(self): 
        self.a = "aa" 
        super().__init__() 
        self.c = "cc" 
 
    def A(self): 
        print(self.a) 
 
    def B(self): 
        self.b = "bb" 
        super().B() 
        print(self.b) 
 
base = Base() 
derivada = Derivada() 
 
base.A() 
derivada.A() 
print() 
base.B() 
derivada.B() 
base.C() 
derivada.C() 
derivada = base 
derivada.C()

#La solución es:
#a
#a

#b
#bb
#bb
#c
#cc
#c
```

**UML:**


<img width="296" alt="puzzle" src="https://user-images.githubusercontent.com/91721875/159308882-06663bc3-0751-4163-a72b-5c2d8ace3417.png">


***


## Ejercicio 3:


***


## Ejercicio 4:

**código:**
```
class Pared:
    def __init__(self, orientacion):
        self.orientacion = orientacion
        self.ventanas = []

class Ventana:
    def __init__(self, pared, superficie):
        self.pared = pared
        self.superficie = superficie
        self.pared.ventanas.append(self)

class Casa:
    def __init__(self, paredes):
        self.paredes = paredes

    def superficie_cristal(self):
        superficie = 0
        for pared in self.paredes:
            for ventana in pared.ventanas:
                superficie += ventana.superficie
        return superficie

pared_norte = Pared("NORTE")
pared_oeste = Pared("OESTEE")
pared_sur = Pared("SUR")
pared_este = Pared("ESTE")
ventana_norte = Ventana(pared_norte, 0.5)
ventana_oeste = Ventana(pared_oeste, 1)
ventana_sur = Ventana(pared_sur, 2)
ventana_este = Ventana(pared_este, 1)
casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este])
print(casa.superficie_cristal())

class ParedCortina(Pared, Ventana):
    def __init__(self, orientacion, superficie):
        Pared.__init__(self, orientacion)
        Ventana.__init__(self, self, superficie, "Ninguna")

pared_cortina = ParedCortina("SUR", 10)
casa.paredes[2] = pared_cortina
print(casa.superficie_cristal())

```
**UML:**

<img width="599" alt="casa" src="https://user-images.githubusercontent.com/91721875/159310510-6c2d66db-8306-42e5-abbf-5d54cdc78f19.png">


***
