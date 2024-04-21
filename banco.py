from datetime import date

print("\n\n\n======Bem Vindo ao Banco Nacional da Sbornia!======")

menu = """ 
***Escolha a operação desejada:***
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""
saldo = 0
limite_valor_saque = 500
extrato = ""
numero_saques = 0
LIMITE_QUANTIDADE_SAQUES = 3
data = date.today()

while True:
    opcao = input(menu)

    if opcao == "d":
        
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        
        while valor_deposito <= 0:
            print("Favor informar um valor positivo!")
            valor_deposito = float(input("Digite o valor a ser depositado: "))
        else:
            saldo += valor_deposito
            print("Depósito realizado com sucesso!")
            extrato += f"\nDepósito: R$ {valor_deposito:.2f}"
    
    elif opcao == "s":
        
        valor_saque = float(input("Digite o valor que deseja sacar:"))
        
        limite_saldo_excedido = valor_saque > saldo
        limite_valor_saque_excedido = valor_saque > limite_valor_saque
        limite_numero_saques_excedido = numero_saques >= LIMITE_QUANTIDADE_SAQUES

        while valor_saque <= 0:
            print("Favor informar um valor positivo!")
            valor_saque = float(input("Digite o valor que deseja sacar:"))
        
        if limite_saldo_excedido:
            print("Seu saldo é insuficiente para sacar o valor solicitado!")
            opcao = input(menu)
        elif limite_valor_saque_excedido:
            print("O valor informado excede o valor limite para saque por operação!")
            
        elif limite_numero_saques_excedido:
            print("O número de saques diários foi excedido!")
            
        else:
            saldo -= valor_saque
            print("Saque realizado com sucesso!")
            numero_saques += 1
            extrato += f"\nSaque: R$ {valor_saque:.2f}"

    elif opcao == "e":
        print("\n============================Extrato===========================")
        print("Não há registro de movimentações em sua conta!" if not extrato else extrato)
        print(f"\nSaldo Atual: R$ {saldo:.2f}")
        print(f"======Resumo das movimentações finaceiras até {data}======") 
    
    elif opcao == "q":
        print("\nObrigado por utilizar nosso sistema. É muito bom ter você como cliente!")
        break
        

    else:
        ("Opção inválida!")
        
