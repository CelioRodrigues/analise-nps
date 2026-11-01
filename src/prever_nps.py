from pathlib import Path

import joblib
import pandas as pd

def solicitar_regiao():
    regioes = ["Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"]

    while True:
        regiao = input(
            "Região do cliente (Norte, Nordeste, Centro-Oeste, Sudeste ou Sul): "
        ).strip()

        if regiao in regioes:
            return regiao

        print("Região inválida. Escolha uma das opções apresentadas.\n")

# Localizar o modelo salvo
caminho_modelo = Path(__file__).resolve().parent.parent / "models" / "modelo_nps.joblib"

# Carregar o Pipeline treinado
modelo = joblib.load(caminho_modelo)


print("=== Previsão de Nota NPS ===")

# Informações do cliente e do pedido
dados_cliente = {
    "customer_age": int(input("Idade do cliente: ")),
    "customer_region": solicitar_regiao(),
    "customer_tenure_months": int(input("Tempo como cliente (meses): ")),
    "order_value": float(input("Valor do pedido: ")),
    "items_quantity": int(input("Quantidade de itens: ")),
    "discount_value": float(input("Valor do desconto: ")),
    "payment_installments": int(input("Número de parcelas: ")),
    "delivery_time_days": float(input("Tempo de entrega (dias): ")),
    "delivery_delay_days": float(input("Atraso na entrega (dias): ")),
    "freight_value": float(input("Valor do frete: ")),
    "delivery_attempts": int(input("Tentativas de entrega: ")),
    "customer_service_contacts": int(input("Contatos com atendimento: ")),
    "resolution_time_days": float(input("Tempo de resolução (dias): ")),
    "complaints_count": int(input("Quantidade de reclamações: "))
}

# Converter as entradas em um DataFrame
entrada = pd.DataFrame([dados_cliente])

# Executar a previsão
nota_prevista = modelo.predict(entrada)[0]

# Classificar a nota prevista
if nota_prevista < 7:
    classificacao = "Detrator"
elif nota_prevista < 9:
    classificacao = "Neutro"
else:
    classificacao = "Promotor"

print("\n=== Resultado da Previsão ===")
print(f"Nota de NPS prevista: {nota_prevista:.2f}")
print(f"Classificação prevista: {classificacao}")