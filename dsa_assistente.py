class Veiculo: # Classe pai (Super classe)

    def __init__(self, marca, modelo): # Método construtor
        self.marca = marca
        self.modelo = modelo
        self.ligado = False

    def ligar(self):
        self.ligado = True
        print(f"O Veículo {self.modelo} foi ligado!")

    def deslifar(self):
        self.ligado = False
        print(f"O veículo {self.modelo} foi desligado.")

    def exibir_detalhes(self):
        print(f"Veículo genérico da marca {self.marca} e modelo {self.modelo}.")


class Carro(Veiculo): # Classe filho (herança)

    def __init__(self, marca, modelo, ano): # Método construtor
        super().__init__(marca, modelo) # Chama o construtor da classe pai
        self.ano = ano
        self._velocidade = 0
        self.__horsepower = 300

    def get_velocidade(self):
        return self._velocidade
    
    def acelerar(self, valor):
        if valor > 0:
            self._velocidade += valor
            print(f"O {self.modelo} acelerou para {self._velocidade} km/h.")
        else:
            print("A velocidade deve ser maior que zero.")
    
    def desacelerar(self, valor):
        if valor > 0:
            self._velocidade -= valor
            if self._velocidade < 0:
                self._velocidade = 0
                print(f"O {self.modelo} desacelerou para {self._velocidade} km/h.")
        else:
            print("O valor da frenagem deve ser maior que zero.")

    def exibir_detalhes(self):
        print(f"Carro da marca {self.marca}, modelo {self.modelo} e ano {self.ano}.")


class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def exibir_detalhes(self):
        print(f"Moto da marca {self.marca} e modelo {self.modelo} com {self.cilindrada} cilindradas.")


veiculos = [
    Carro("Honda", "Civic", 2020),
    Moto("CF Moto", "Ibex 450", 449),
    Veiculo("Caloi", "Ceci")
]

for v in veiculos:
    v.exibir_detalhes()