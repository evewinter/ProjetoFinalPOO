class Gravadora:
  def __init__(self, nome, pais):
      self.nome = nome
      self.pais = pais
      self.totaldecantores = []

  def contratar_artista(self, cantor):
      self.totaldecantores.append(cantor)
      cantor.gravadora = self
      print(f"{cantor.nome} foi contratado pela {self.nome}.\n")

class Subsidiaria(Gravadora):
   def __init__(self, nome, pais, selo):
      super().__init__(nome, pais)
      self.selo = selo

   def contratar_artista(self, cantor):
       super().contratar_artista(cantor) 
       print(f"{cantor.nome} agora faz parte do selo {self.selo}.\n")