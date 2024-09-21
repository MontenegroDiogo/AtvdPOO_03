class Veiculo:
    def __init__(self, velocidade_maxima):
        self._velocidade_maxima = velocidade_maxima
    
    def get_velo_max(self):
        return self._velocidade_maxima
    
    def acelerar(self, valor):
        if self._velocidade_maxima + valor <= 200:
            self._velocidade_maxima += valor
        else:
            self._velocidade_maxima = 200

class Carro(Veiculo):
    def acelerar(self, valor):
        if self._velocidade_maxima + valor <= 180:
            self._velocidade_maxima += valor
        else:
            self._velocidade_maxima = 180
    
    def frear(self, valor):
        if self._velocidade_maxima - valor >= 0:
            self._velocidade_maxima -= valor
        else:
            self._velocidade_maxima = 0

carro = Carro(100)
carro.acelerar(50)
print(carro.get_velo_max()) 
carro.frear(100)
print(carro.get_velo_max())  
