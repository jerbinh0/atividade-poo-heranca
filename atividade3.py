#problema 1
class Publicacao:
    def __init__(self, titulo, ano_publicacao):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao

    def descrever(self):
        print(f"Título: {self.titulo} | Ano: {self.ano_publicacao}")


class Livro(Publicacao):
    def __init__(self, titulo, ano_publicacao, autor):
        super().__init__(titulo, ano_publicacao)
        self.autor = autor

    def descrever(self):
        super().descrever()
        print(f"Autor: {self.autor}")


class Revista(Publicacao):
    def __init__(self, titulo, ano_publicacao, edicao):
        super().__init__(titulo, ano_publicacao)
        self.edicao = edicao

    def descrever(self):
        super().descrever()
        print(f"Edição: {self.edicao}")


# Teste
livro = Livro("Dom Casmurro", 1899, "Machado de Assis")
revista = Revista("National Geographic", 2024, 78)

livro.descrever()
print()
revista.descrever()

#problema 2

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print(f"Marca: {self.marca} | Modelo: {self.modelo}")


class Carro(Veiculo):
    def __init__(self, marca, modelo, numero_portas):
        super().__init__(marca, modelo)
        self.numero_portas = numero_portas

    def exibir_info(self):
        super().exibir_info()
        print(f"Número de portas: {self.numero_portas}")


class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    def exibir_info(self):
        super().exibir_info()
        print(f"Cilindradas: {self.cilindradas}cc")


# Teste
carro = Carro("Toyota", "Corolla", 4)
moto = Moto("Honda", "CG", 160)

carro.exibir_info()
print()
moto.exibir_info()

#problema 3

class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base


class Gerente(Funcionario):
    def __init__(self, nome, salario_base, bonus):
        super().__init__(nome, salario_base)
        self.bonus = bonus

    def calcular_salario(self):
        return self.salario_base + self.bonus


class Programador(Funcionario):
    def __init__(self, nome, salario_base, horas_extras, valor_hora_extra):
        super().__init__(nome, salario_base)
        self.horas_extras = horas_extras
        self.valor_hora_extra = valor_hora_extra

    def calcular_salario(self):
        return self.salario_base + (self.horas_extras * self.valor_hora_extra)


# Lista heterogênea (polimorfismo)
funcionarios = [
    Gerente("Carlos", 5000, 1500),
    Programador("Ana", 3000, 20, 40),
    Programador("João", 2800, 10, 50)
]

for f in funcionarios:
    print(f"{f.nome} - Salário: R${f.calcular_salario():.2f}")

#problema 4

class Conta:
    def __init__(self, titular, numero_conta, saldo=0):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado. Novo saldo: R${self.saldo}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado. Saldo restante: R${self.saldo}")
        else:
            print("Saldo insuficiente!")

    def extrato(self):
        print(f"Titular: {self.titular} | Conta: {self.numero_conta} | Saldo: R${self.saldo}")


class ContaPoupanca(Conta):
    def render_juros(self, taxa):
        rendimento = self.saldo * (taxa / 100)
        self.saldo += rendimento
        print(f"Rendimento aplicado: R${rendimento}. Novo saldo: R${self.saldo}")

    def sacar(self, valor):
        if valor <= self.saldo:
            super().sacar(valor)
        else:
            print("Saque negado! A Conta Poupança não permite saldo negativo.")


class ContaCorrente(Conta):
    def __init__(self, titular, numero_conta, saldo, limite_cheque_especial):
        super().__init__(titular, numero_conta, saldo)
        self.limite_cheque_especial = limite_cheque_especial

    def sacar(self, valor):
        if valor <= self.saldo + self.limite_cheque_especial:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado (pode ter entrado no limite). Saldo atual: R${self.saldo}")
        else:
            print("Saque negado! Limite insuficiente.")


# Teste
p = ContaPoupanca("Maria", 123, 1000)
c = ContaCorrente("João", 456, 500, 300)

p.extrato()
p.render_juros(5)
p.sacar(2000)
p.sacar(300)

print()

c.extrato()
c.sacar(700)
c.sacar(500)
