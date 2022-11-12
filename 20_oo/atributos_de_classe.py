class TV:

    cor = 'Preta'

    def __init__(self, tamanho):
        # state
        self.ligado = False 
        self.canal = '0'
        self.volume = 0

        self.tamanho = tamanho

    def mudar_canal(self, str_canal):
        self.canal = str_canal 


