menu = """ 

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair    

=> """

saldo = 0
extrato = ""
limite_saque = 500
numero_saque= 0
SAQUES_DIARIOS = 3

while True:

    opcao = int(input(menu))
    
    if opcao == 1:

      movimento = float(input("Informe o valor a ser depositado: ")) 

      if movimento > 0:
         
         saldo += movimento
         extrato += f"Depósito de R${movimento:.2f} realizado com sucesso!\n"

      else: 
         print("Valor inválido, a operação falhou.")


    elif opcao == 2:
      
      movimento = float(input("Informe o valor a ser sacado: "))

      excedeu_saque = numero_saque >= SAQUES_DIARIOS
      excedeu_limite = movimento > limite_saque
      excedeu_saldo = movimento > saldo

      if excedeu_saldo:
         print(f"Saldo insuficiente! Seu saldo atual é de: R${saldo}.")

      elif excedeu_limite:
         print(f"Operação falhou! Seu limite de saque atual é de: R${limite_saque}.")
      
      elif excedeu_saque:
         print("Não foi possível realizar saque! Número de saques excedido.")
      
      elif movimento > 0:
         saldo -= movimento
         extrato += f"Saque:R${movimento:.2f}\n"
         numero_saque += 1
      
      
      else:
         print ("Operação falhou! Valor de saque é inválido.")
         

    elif opcao == 3:
    
      print("\n__________________| EXTRATO |_________________")
      print("Nenhum movimento foi registrado." if not extrato else extrato)
      print(f"\nSaldo: R${saldo:.2f}")
      print("_______________________________________________")


    elif opcao == 4:
       break


    else:
        print("Opção inválida, por favor escolha uma das opções abaixo.")