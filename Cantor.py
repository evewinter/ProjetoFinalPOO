class Cantor:
  def __init__(self, nome, nacionalidade, gravadora, salario=0):
      self.nome = nome
      self.nacionalidade = nacionalidade
      self.gravadora = gravadora
      self.__salario = salario

  def apresentar(self):
        return f"O/A artista {self.nome}, faz um show vocal na casa de shows."

class Solista(Cantor):
    def __init__(self, nome, nacionalidade, gravadora, salario=0, estilo_musical=None):
        super().__init__(nome, nacionalidade, gravadora, salario)
        self.estilo_musical = estilo_musical

    def apresentar(self):
        return f"O/A artista {self.nome}, se apresenta em um estádio para centenas de pessoas."

class Grupo(Cantor):
    def __init__(self, nome, nacionalidade, gravadora, nome_do_grupo, salario=0):
        super().__init__(nome, nacionalidade, gravadora, salario)
        self.nome_do_grupo = nome_do_grupo
        self.membros = []

    def adicionar_membro(self, cantor):
        self.membros.append(cantor)

    def apresentar(self):
        return f"O grupo {self.nome_do_grupo}, faz um show com dançarinos de apoio em um clube."