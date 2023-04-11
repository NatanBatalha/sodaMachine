#Variables
monster = 12
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
piggyBank = 0
loan = (monster - piggyBank)
balance = 0
ballot2 = 0
ballot5 = 0
ballot10 = 0
ballot20 = 0
ballot50 = 0
ballot100 = 0
ballot200 = 0
coin5 = 0
coin10 = 0
coin25 = 0
coin50 = 0
coin1 = 0
sequenceOfBallots = [ballot2,ballot5,ballot10,ballot20,ballot50,ballot100,ballot200]
sequenceOfCois = [coin5,coin10,coin25,coin50,coin1]
billOrCoin = 0
ballots = [2,5,10,20,50,100,200]
coins = [0.05,0.10,0.25,0.50,1]
change = (piggyBank - monster)
choiceBallot = []
turnChoiceBallot = 0
valueOfChoiceBallot = 0
turnChoiceCoin = 0
valueOfChoiceCoin = 0




# Aqui iremos colocar a primeira opção para o usuário.


#Lógica para o Administrador:
while counter2 == 0:
    counter3 = 0
    myself = int(input("Digite 1 - Consumidor, 2 - Administrador, 3 - Reset Machine"))
    if myself == 2:
        admOption = int(input("Digite: 1- para ver saldo, 2 - Atualizar os valores das cédulas e moedas"))
        counter4 = 0
        print(counter4)
        if admOption == 1:
            while counter4 == 0:
                print("O saldo da máquina é de:R$", balance)
                i = 0
                while i <=6:
                    if admOption == 1:
                        print("Há:",sequenceOfBallots[i],"unidades na nota de R$", ballots[i])
                        i = (i +1)
                        y = 0
                while y <=4:
                    print("Há:", sequenceOfCois[y], "unidades da moeda de R$", coins[y])
                    y = (y +1)
                counter4 = int(input("Digite 0 - Para ver saldo Novamente ou 1 para Voltar ao menu principal"))
        elif admOption == 2:
            print(counter3)
            while counter3 == 0:
                billOrCoin = int(input("Se você deseja Alterar o valor de uma cédula, Digite - 1 ou Moeda - 2 ou 0 - para sair "))
                if billOrCoin == 1:
                    print("coloque o número correspondente a cédula que você deseja alterar:"
                          "\n 0 - R$",ballots[0],
                          "\n 1 - R$",ballots[1],
                          "\n 2 - R$",ballots[2],
                          "\n 3 - R$",ballots[3],
                          "\n 4 - R$",ballots[4],
                          "\n 5 - R$",ballots[5],
                          "\n 6 - R$",ballots[6],)
                    turnChoiceBallot = int(input("Digite Aqui:"))
                    valueOfChoiceBallot = int(input("Alterar para qual valor?"))
                    if turnChoiceBallot >= 0:
                        del ballots[turnChoiceBallot]
                        ballots.insert(turnChoiceBallot,valueOfChoiceBallot)
                        print(ballots)
                        counter3 = int(input("Digite 0 - para escolher outra alteração ou 1 - para voltar ao menu principal"))
                elif billOrCoin == 2:
                    print("coloque o número correspondente a moeda que você deseja alterar:"
                          "\n 0 - R$", coins[0],
                          "\n 1 - R$", coins[1],
                          "\n 2 - R$", coins[2],
                          "\n 3 - R$", coins[3],
                          "\n 4 - R$", coins[4],)
                    turnChoiceCoin = int(input("Digite Aqui:"))
                    valueOfChoiceCoin = float(input("Alterar para qual valor?"))
                    if turnChoiceCoin >= 0:
                        del coins[turnChoiceCoin]
                        coins.insert(1,valueOfChoiceCoin)
                    print((coins))
                    counter3 = int(input("Digite 0 - para escolher outra alteração ou 1 - para voltar ao menu principal"))
                elif billOrCoin == 0:
                    counter3 += 1

# Lógica do Consumidor
    elif myself == 1:
        print("O Monster custa R$12,00, Por favor, agora insira seu dinheiro")
        while counter1 < 1:
            paymentOption = int(input("Você irá inserir: 1 - Somente cédulas, 2 - Somente moedas, 3 - Cédulas e Moedas, 4 - Voltar"))
            if paymentOption == 1:
                valueOfBallots = int(input("Qual Valor da cédula que será inserida?"))
                totalOfBallots = int(input("Quantas cédulas serão inseridas ?"))
                piggyBank += (valueOfBallots*totalOfBallots)
                counter1 = int(input("Você precisa inserir mais dinheiro: 0 - Sim ou 1 - Não ?"))
                counter2 = 1
                print(piggyBank) #teste - depois retirar
            elif paymentOption == 2:
                valueOfCoins = int(input("Qual Valor da moeda que será inserida?"))
                totalOfCoins = int(input("Quantas moedas dessas serão inseridas ?"))
                piggyBank += (valueOfCoins * totalOfCoins)
                counter1 = int(input("Você precisa inserir mais dinheiro: 0 - Sim ou 1 - Não ?"))
                counter2 = 1
            elif paymentOption == 3:
                valueOfBallots = int(input("Qual Valor da cédula que será inserida?"))
                totalOfBallots = int(input("Quantas cédulas serão inseridas ?"))
                valueOfCoins = int(input("Qual Valor da moeda que será inserida?"))
                totalOfCoins = int(input("Quantas moedas dessas serão inseridas ?"))
                piggyBank += ((valueOfBallots*totalOfBallots) + (valueOfCoins*totalOfCoins))
                counter1 = int(input("Você precisa inserir mais dinheiro: 0 - Sim ou 1 - Não ?"))
                counter2 = 1
            elif paymentOption == 4:
                counter1 = 0
            else:
                print("Opção inválida, Digite uma opção correspondente")
                change = (piggyBank - monster)
                balance += change
    elif myself == 3:
        print("MÁQUINA DESLIGADA E RESETADA")
        counter2 = 1

    if piggyBank == monster and piggyBank > 0:
        print("compra aprovada, retire seu produto")
        counter2 = 0
    elif piggyBank > monster and piggyBank > 0:
        print("compra aprovada, retire seu produto e receba seu troco")
        print("Seu troco é de: R$",(change))
        counter2 = 0
    elif piggyBank < monster and piggyBank > 0:
        print("O dinheiro que vc inseriu é insuficiente, ainda restam, R$", loan)
        counter2 = 0







