questionario = [
{"id":1,"pergunta":"Qual estrutura usa chave e valor?","altA":"Lista","altB":"Fila","altC":"Dicionário","altD":"Tupla","altE":"Pilha","altCorreta":"C"},

{"id":2,"pergunta":"Qual estrutura não pode ser alterada?","altA":"Tupla","altB":"Lista","altC":"Fila","altD":"Pilha","altE":"Dicionário","altCorreta":"A"},

{"id":3,"pergunta":"Qual estrutura funciona em FIFO?","altA":"Pilha","altB":"Fila","altC":"Lista","altD":"Tupla","altE":"Dicionário","altCorreta":"B"},
]

resposta = []
acertos = 0

for q in questionario:

    print(q["pergunta"])
    print("A)", q["altA"])
    print("B)", q["altB"])
    print("C)", q["altC"])
    print("D)", q["altD"])
    print("E)", q["altE"])

    resposta = input("Digite a alternativa escolhida: ")

    if resposta == q["altCorreta"]:
        print("Resposta correta")
        acertos += 1
    else:
        print("Resposta errada")
        print("Alternativa correta:", q["altCorreta"])

for i in resposta:
    print(resposta)

print("Total de acertos:", acertos)
print("Total de erros:", len(questionario) - acertos)