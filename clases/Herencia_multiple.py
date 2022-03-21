class paredes:
  def __init__(self,orientacion,ventana):
    self.orientacion= orientacion 
    self.ventana= []

class ventana:
  def __init__(self,pared,superficie):
    self.pared= pared
    self.superficie= superficie
    self.pared.ventanas.append(self)
    
class casa:
  def __init__(self,pared):
    self.pared=pared
    
  def superficie_acristalada(self):
    superficie = 0
    for pared in self.pared:
      for ventana in pared.ventanas:
        superficie += ventana.superficie
      return superficie

  


pared_norte = paredes('NORTE') #lo ponemos en mayúscula porque es una variable constante
pared_sur = paredes('SUR')
pared_este = paredes('ESTE')
pared_oeste = paredes('OESTE')

ventana_norte = ventana(pared_norte)
ventana_sur = ventana(pared_sur)
ventana_este = ventana(pared_este)
ventana_oeste = ventana(pared_oeste)

casa= casa([pared_norte, pared_sur, pared_este, pared_oeste])
print(casa.superficie_acristalada)

class paredcortina(paredes, ventana):
  def __init__(self, orientacion, superficie):
    paredes.__init__(self,orientacion)
    ventana.__init__(self, self, superficie)
  
