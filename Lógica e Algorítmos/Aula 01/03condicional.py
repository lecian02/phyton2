# condicional simples
idade = 17

if idade >= 18:
    print("pode obter a cnh")
else:
    print("não pode obter a cnh")

# condicional aninhada/composta
    media = 10

    if media == 10:
        print("nota máxima! Parabéns")
    elif media >= 9:
        print("ótimo!")
    elif media >= 8:
        print("bom!")
    elif media >= 7:
        print("na média!")
    elif media >= 5:
        print("em exame!")
    else:
        print("reprovado")

    # operadores lógicos
    valor = 85

    if valor >= 0 and valor <= 100:
        print("o valor está entre 0 e 100")
    else:
        print("o valor não está entre 0 e 100")

    total = 400
    formapagamento = "a prazo"

    if total >= 100 or formapagamento == "a vista":
        print("valor a pagar R$"+str(total * 0.9))
    else:
        print(" o valor a pagar R$" +str(total))




    
        
    
        
