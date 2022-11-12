class Pessoa:
    # method
    def __init__(self, nome, sobrenome, idade):
        self.name = nome
        self.last_name = sobrenome
        self.age = idade
        self.namorade = None
        self._cpf = '123.123.123-12' # privado -> so pode ser acessado através de um metodo

    @staticmethod
    def _data_e_hora_criacao_class():
        ...

    def se_apresentar(self):
        print(f'Oi! Me chamo {self.name}')

    def definir_namorade(self, nome):
        self.namorade = nome
        print('Ta namorando né...')
    

class TV:
    # method
    def __init__():
        ...

pessoa = Pessoa('Fernando', 'Santos', 18)
pessoa.se_apresentar()
