from datetime import datetime

# função para calcular juros
def calcular_valor(valor, vencimento, pagamento):

    dias_atraso = (pagamento - vencimento).days

    