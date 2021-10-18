class Pessoa:
    def __init__(self, *filhos, nome = None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar (self):
        return  f'Olá {id(self)}'


if __name__=='__main__':
    Guilherme = Pessoa (nome='Guilherme')
    Fernanda = Pessoa(Guilherme, nome ='Fernanda')
    print(Pessoa.cumprimentar(Fernanda))
    print(id(Fernanda))
    print(Fernanda.cumprimentar())
    print(Fernanda.nome)
    print(Fernanda.idade)
    for filhos in Fernanda.filhos:
        print(filhos.nome)








