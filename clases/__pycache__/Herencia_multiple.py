class paredes:
  def __init__(self,orientacion,ventana):
    self.orientacion= orientacion 
    self.ventana= []

class ventana:
  def __init__(self,pared,superficie):
    self.pared= pared
    self.superficie= superficie
    self.pared.ventanas.append(self)
    
    


pared_norte = paredes('NORTE') #lo ponemos en mayúscula porque es una variable constante
pared_sur = paredes('SUR')
pared_este = paredes('ESTE')
pared_oeste = paredes('OESTE')
