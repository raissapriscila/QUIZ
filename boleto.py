from datetime import datetime

def calcular(valor, venc, pag):
    dias = (pag - venc).days

    if dias > 0:
        valor = valor + (valor * 0.02) + (valor * 0.01 * dias)
    else:
        dias = 0

    return valor, dias


while True:

    cliente = input("Cliente: ")
    produto = input("Produto: ")
    valor = float(input("Valor: "))

    venc = input("Vencimento (dd/mm/aaaa): ")
    pag = input("Pagamento (dd/mm/aaaa): ")

    venc = datetime.strptime(venc, "%d/%m/%Y")
    pag = datetime.strptime(pag, "%d/%m/%Y")

    valor_final, dias = calcular(valor, venc, pag)

    print("\n--- RESUMO ---")
    print("Cliente:", cliente)
    print("Produto:", produto)

    if dias > 0:
        print("Atraso:", dias, "dias")
    else:
        print("Pago em dia")

    print("Valor final: R$", round(valor_final, 2))

    continuar = input("\nOutra venda? (s/n): ")
    if continuar != "s":
        break