class Pessoa:
    def __init__(self, altura, cor_cabelo, peso):
        self.altura = altura
        self.cor_cabelo = cor_cabelo
        self.peso = peso

    def falar(self, frase):
        return frase

    def andar(self, velocidade=5):
        velocidade_real = velocidade - 0.01 * self.peso
        return velocidade_real

class Professor(Pessoa):

    def __init__(self, altura, cor_cabelo, peso, salario):
        super().__init__(altura, cor_cabelo, peso)
        self.salario = salario

def main():
        pessoaObj = Pessoa(1.8, 'castanho', 95.0)
        print(pessoaObj.falar('Python é top'))
        print(pessoaObj.andar(7))

        professorObj = Professor(1.9, 'loiro', 89.0, 2000.0)
        print(professorObj.falar('Python é jegas'))
        print(professorObj.andar(9))

if __name__ == '__main__':
        main()
    