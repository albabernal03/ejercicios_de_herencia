class Punto2D:
  def __init__(self,a1,a2,b1,b2):
    self.a1 = a1
    self.a2 =a2
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
print(Punto2D.punto2d(1,2,4,6))
print("Puntos translacion:")
print(Punto2D.punto2dtranslacion(5,3,0,1))
print("Puntos suma:")
print(Punto2D.sumapuntos(1+5, 3+2, 4+0, 6+1))