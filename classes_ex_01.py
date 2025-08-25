class Pássaro():

    def __init__(self, tamanho, cores, espécie, sexo):
        self.tamanho = tamanho
        self.cores = cores
        self.espécie = espécie
        self.sexo = sexo

    def cantar(self):
        return print(f'Sou um {self.especie}cantando uma canção ')

    def voar(self):
        return print('batendo as asas e: voando...')

Pássaro1 = Pássaro(0.14, ['Marrom', 'Branco', 'Cinza'], 'Pardal', 'M')
Pássaro1.cantar()





class Animais_Marinhos():

    def __init__(self, tamanho, cores, sexo, velocidade, especie):
        self.tamanho = tamanho
        self.cores = cores
        self.sexo = sexo
        self.velocidade = velocidade
        self.especie = especie

    def pular(self):
        return print(f'Eu gosto viajar{self.valocidade} pulando')

    def viajar(self):
        return print(f'SOu um {self.especie} adiante')

    def caçar(self):
        return print(f'Eu me adapto bem com meu {self.tamanho} correndo')

    def adaptação(self):
        return print(f'')

    def alimentação(self):
        return print(f'Tenho brilhos como uma{self.cores} brilhante')

Marinhos1 = Animais_Marinhos(1.90, ['azul', 'macho', '60km/h'], 'golfinho')
Marinhos1.velocidade()







