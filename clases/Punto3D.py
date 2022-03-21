class Punto3D():
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
print(Punto3D.punto3d(1,2,4))
print("Puntos translacion:")
print(Punto3D.punto3dtranslacion(5,3,0))
print("Puntos suma:")
print(Punto3D.sumapuntos(1+5, 3+2, 4+0))