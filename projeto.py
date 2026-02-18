aparelhos = ['Ventilador', 'Geladeira', 'Computador', 'Notebook', 'Ar condicionado']
preco = 0.65  # preço do kWh

# Função para calcular consumo mensal
def calcular_consumo(potencia, horas):
    consumo = (potencia * horas * 30) / 1000  # kWh
    return consumo

# Função para calcular custo
def calcular_custo(consumo):
    return consumo * preco


# Pergunta o aparelho
aparelho = input("Digite o nome do aparelho: ")
aparelho = aparelho.title()

# caso não estiver na lista, cadastrar novo produto
if aparelho not in aparelhos:
    print("Aparelho não encontrado, cadastrando...")
    aparelhos.append(aparelho)

# entrada de dados
potencia = float(input("Potência em Watts (W): "))
horas = float(input("Horas de uso por dia: "))

# Calcula
consumo = calcular_consumo(potencia, horas)
custo = calcular_custo(consumo)

# Mostra os resultados
print("Relatório de Consumo\n")
print(f"Aparelho: {aparelho}\n")
print(f"Consumo mensal: {consumo:.2f} kWh\n")
print(f"Custo mensal: R$ {custo:.2f}\n")




















