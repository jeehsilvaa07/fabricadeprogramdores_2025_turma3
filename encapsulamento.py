class Pessoa:
    def __init__(self, nome, idade, altura, peso, email, senha, cpf, endereco):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.email = email
        self.ativo = True
        self.interesses = []
        self._senha = senha
        self.endereco = endereco
        self._cpf = cpf

    @property
    def senha(self):
        return "Acesso negado. Use o método apropriado para verificar a senha."
    print("acesso permitido")

    def verificar_senha(self, senha):
        return self._senha == senha

    def alterar_senha(self, senha_atual, nova_senha):
        if self._senha == senha_atual:
            self._senha = nova_senha
            return True
        return False

    @property
    def cpf(self):
        return "Acesso negado."

    def get_cpf(self, senha):
        if senha == self._senha:
            return self._cpf
        return "Senha incorreta."

    def set_cpf(self, novo_cpf, senha):
        if senha == self._senha:
            self._cpf = novo_cpf
            return True
        return False

 
    def adicionar_interesse(self, interesse):
        self.interesses.append(interesse)

    def desativar(self):
        self.ativo = False

    def ativar(self):
        self.ativo = True

    def _calcular_imc(self):
        return self.peso / (self.altura ** 2)

    def mostrar_imc(self):
        return round(self._calcular_imc(), 2)

    def resumo(self):
        return f"{self.nome}, {self.idade} anos, email: {self.email}"

p = Pessoa("Ana", 30, 1.65, 65.0, "ana@email.com", "senha123", "123.456.789-00", {"cidade": "SP", "rua": "Av. Brasil"})
p.adicionar_interesse("leitura")
print(p.mostrar_imc())
print(p.verificar_senha("senha123"))
print(p.get_cpf("senha123"))