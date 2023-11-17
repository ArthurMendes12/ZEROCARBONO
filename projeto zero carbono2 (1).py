print ("------ CALCULADORA DE EMISSÃO DE CARBONO (CO2) ------")

consumo_energia = float(input("Digite o consumo de energia (em kWh): "))
carbono_utilizado = float(input("Digite a quantidade de carbono armazenada (em toneladas): "))

# Define o fator de emissão de carbono (em kg CO2 por kWh)
fator_emissao = 0.5   

# Calcula a emissão de carbono (em kg CO2)
emissao_carbono = consumo_energia * fator_emissao

# Calcula os créditos de carbono restantes
creditos_carbono = carbono_utilizado - (emissao_carbono / 1000)  # Convertendo kg para toneladas

# Solicita ao usuário que insira o preço atual dos créditos de carbono no mercado
preco_credito_carbono = float(input("Digite o preço atual dos créditos de carbono (por tonelada): "))

# Calcula o valor de vendas dos créditos de carbono restantes
valor_vendas_creditos = creditos_carbono * preco_credito_carbono

# Exibe a emissão de carbono, os créditos de carbono restantes e o valor de vendas
print(f"Emissão de carbono: {emissao_carbono:.2f} kg CO2")
print(f"Créditos de carbono restantes: {creditos_carbono:.2f} toneladas")
print(f"Valor de vendas dos créditos de carbono restantes: R${valor_vendas_creditos:.2f}")

# Verifica se houve lucro ou prejuízo com os créditos de carbono
if creditos_carbono > 0:
    print("Você obteve lucro com os créditos de carbono!")
elif creditos_carbono < 0:
    print("Você ultrapassou a quantidade de carbono utilizada. Há um prejuízo de créditos de carbono.")
else:
    print("Você está equilibrado em termos de créditos de carbono.")
