# importa um funçao que é aleatoria
import random
# importa um funçao que deixa fazer que demore um pouco para a chamada aparecer
import time 

#cartas de um baralho
baralho_cartas = {'2 de paus' : 2,
           '3 de paus' : 3,
           '4 de paus' : 4,
           '5 de paus' : 5,
           '6 de paus' : 6,
           '7 de paus' : 7,
           '8 de paus' : 8,
           '9 de paus' : 9,
           '10 de paus': 10,
           'rei de paus' : 10,
           'valete de paus' : 10,
           'dama de paus' : 10, 
           'as de paus' : 11,
           '2 de ouros' : 2,
           '3 de ouros' : 3,
           '4 de ouros' : 4,
           '5 de ouros' : 5,
           '6 de ouros' : 6,
           '7 de ouros' : 7,
           '8 de ouros' : 8,
           '9 de ouros' : 9,
           '10 de ouros': 10,
           'rei de ouros' : 10,
           'valete de ouros' : 10,
           'dama de ouros' : 10, 
           'as de ouros' : 11,
           '2 de copas' : 2,
           '3 de copas' : 3,
           '4 de copas' : 4,
           '5 de copas' : 5, 
           '6 de copas' : 6,
           '7 de copas' : 7,
           '8 de copas' : 8,
           '9 de copas' : 9,
           '10 de copas': 10,
           'rei de copas' : 10,
           'valete de copas' : 10,
           'dama de copas' : 10, 
           'as de copas' : 11,
           '2 de espadas' : 2,
           '3 de espadas' : 3,
           '4 de espadas' : 4,
           '5 de espadas' : 5,
           '6 de espadas' : 6,
           '7 de espadas' : 7,
           '8 de espadas' : 8,
           '9 de espadas' : 9,
           '10 de espadas': 10,
           'rei de espadas' : 10,
           'valete de espadas' : 10,
           'dama de espadas' : 10, 
           'as de espadas' : 11}

#pra ter muitas cartas 
monte_com_um = baralho_cartas
monte_com_dois = baralho_cartas
monte_com_tres = baralho_cartas
monte_com_quatro = baralho_cartas

#essa vai ser minha maior vigarice
maquina_malandra = ['sim', 'não']

#essa parte permite o usuário escolher o número de baralhos que irá utilizar: 

numero_de_baralhos = int(input('''Olá, antes de começarmos, escolha o número de baralhos que deseja utilizar. (1 a 4): '''))
while numero_de_baralhos > 4 or numero_de_baralhos < 1: 
    print("Opção inválida, por favor tente novamente.")
    time.sleep(2)
    numero_de_baralhos = int(input('''Olá, antes de começarmos, escolha o número de baralhos que deseja utilizar. (1 a 4): '''))
    
lista_de_baralhos = []

if numero_de_baralhos == 1: 
    lista_de_baralhos.append(monte_com_um)
    
    
elif numero_de_baralhos == 2: 
    lista_de_baralhos.append(monte_com_um)
    lista_de_baralhos.append(monte_com_dois)
    
elif numero_de_baralhos == 3: 
    lista_de_baralhos.append(monte_com_um)
    lista_de_baralhos.append(monte_com_dois)
    lista_de_baralhos.append(monte_com_tres)
    
else: 
    lista_de_baralhos.append(monte_com_um)
    lista_de_baralhos.append(monte_com_dois)
    lista_de_baralhos.append(monte_com_tres)
    lista_de_baralhos.append(monte_com_quatro)

#contrutor

jogadores = int(input('''Olá seja bem vindo ao ultimate blackjack, escolha a 
quantidade de jogadores (1 a 7): '''))
while jogadores > 7 or jogadores < 1: 
    print("Opção inválida, por favor tente novamente.")
    print('')
    jogadores = int(input('''Olá seja bem vindo ao ultimate blackjack, escolha a 
quantidade de jogadores (1 a 4): '''))

players = {
    'jogador_01': '',
    'jogador_02': '',
    'jogador_03': '',
    'jogador_04': '',
    'jogador_05': '',
    'jogador_06': '',
    'jogador_07': '',
    'dinero_01': '',
    'dinero_02': '',
    'dinero_03': '',
    'dinero_04': '',
    'dinero_05': '',
    'dinero_06': '',
    'dinero_07': '',
}

for i in range(jogadores):
    players['jogador_0' + str(i + 1)] = input("Digite seu nome jogador n°1: ")
    players['dinero_0' + str(i + 1)] = int(input("Digite aqui o saldo inicial, {0}: ".format(players['jogador_0' + str(i + 1)])))
  
jogador_01 = players['jogador_01']
jogador_02 = players['jogador_02']
jogador_03 = players['jogador_03']
jogador_04 = players['jogador_04']
jogador_05 = players['jogador_05']
jogador_06 = players['jogador_06']
jogador_07 = players['jogador_07']
dinero_01 = players['dinero_01']
dinero_02 = players['dinero_02']
dinero_03 = players['dinero_03']
dinero_04 = players['dinero_04']
dinero_05 = players['dinero_05']
dinero_06 = players['dinero_06']
dinero_07 = players['dinero_07']

if jogadores == 1: 
    while dinero_01 > 0:
  
#monta .
        
        monte_com_um = baralho_cartas
        monte_com_dois = monte_com_um
        monte_com_tres = monte_com_dois
        monte_com_quatro = monte_com_tres
        
        print('''Status:
            
O saldo de {0} é de {1} reais.'''.format(jogador_01, dinero_01))
        time.sleep(1)
        resposta_jogador_01 = input('Deseja iniciar uma nova rodada? (sim ou nao): ')
        while resposta_jogador_01 != "sim" and resposta_jogador_01 != "nao":
            print("Opção inválida!")
            print('')
            resposta_jogador_01 = input('Deseja iniciar uma nova rodada? (sim ou nao): ')
            time.sleep(1)
        if resposta_jogador_01 == "sim":
           valor_aposta_jogador_01 =  int(input('Escolha um valor de aposta: '))
           
#essa parte não deixa o jogador apostar um valor maior que seu saldo   
           
           while valor_aposta_jogador_01 > dinero_01: 
                print('Valor maior que seu saldo!')
                time.sleep(1)
                valor_aposta_jogador_01 =  int(input('Escolha um valor de aposta: '))
                    
#essa parte define as cartas que vão para o jogador       
#deixando de vora cartas que ja foram sorteados
#variavel que quarda valor de cada usuorio 
#sorteia e exclui a carta
#retorna pro while e e nao da merda pq a soma foi feita antes
#da carta ser deletada.            
#esse quanto_as é uma variavel que meio que anota se sorteou um as.
#aí á o calculo com a posibilidade de o as valer 11 ou 1

           quantos_as = 0
           
           soma_pontos_jogador_01 = 0     
           baralho_aleatorio = random.choice(lista_de_baralhos)
           carta_01_jogador_01 = random.choice(list(baralho_aleatorio.keys()))
           soma_pontos_jogador_01 += baralho_aleatorio[carta_01_jogador_01]
           
           if carta_01_jogador_01 == "as espadas" or carta_01_jogador_01 == "as copas" or carta_01_jogador_01 == "as ouros" or carta_01_jogador_01 == "as paus":
                   quantos_as += 1 
                  
           del baralho_aleatorio[carta_01_jogador_01]
           
           baralho_aleatorio = random.choice(lista_de_baralhos)
           carta_02_jogador_01 = random.choice(list(baralho_aleatorio.keys()))
           soma_pontos_jogador_01 += baralho_aleatorio[carta_02_jogador_01]
           
           if carta_02_jogador_01 == "as espadas" or carta_02_jogador_01 == "as copas" or carta_02_jogador_01 == "as ouros" or carta_02_jogador_01 == "as paus":
                   quantos_as += 1 
                   
           del baralho_aleatorio[carta_02_jogador_01]
           
           if soma_pontos_jogador_01 == 22: 
               soma_pontos_jogador_01 -= 11
               soma_pontos_jogador_01 += 1
               quantos_as -= 1

#escolhe se quer mais carta ou nao        
        
           print("Suas cartas são {0}  e {1}, somando {2} pontos.".format(carta_01_jogador_01, carta_02_jogador_01, soma_pontos_jogador_01))
           time.sleep(1)
           while soma_pontos_jogador_01 < 21:
               mais_carta_jogador_01 = input("Queis pegar mais uma carta? (sim ou nao): ")
               if mais_carta_jogador_01 == "sim": 
                   baralho_aleatorio = random.choice(lista_de_baralhos)
                   carta_extra_jogador_01 = random.choice(list(baralho_aleatorio.keys()))
                   print("Sua carta é {0}.".format(carta_extra_jogador_01))
                   time.sleep(2)
                   print('')
                
#se o jogador tiver condicoes o as ira ser alterado
                
                   if soma_pontos_jogador_01  > 10 and  carta_extra_jogador_01 == "as espadas" or carta_extra_jogador_01 == "as copas" or carta_extra_jogador_01 == "as ouros" or carta_extra_jogador_01 == "as paus":
                       quantos_as += 1
                       baralho_aleatorio[carta_extra_jogador_01] = 1
                       soma_pontos_jogador_01 += baralho_aleatorio[carta_extra_jogador_01]
                       del baralho_aleatorio[carta_extra_jogador_01]
                       print("Total de pontos é {0}.".format(soma_pontos_jogador_01))
                       time.sleep(1)
                        
                   else: 
                       soma_pontos_jogador_01 += baralho_aleatorio[carta_extra_jogador_01]
                       del baralho_aleatorio[carta_extra_jogador_01]
                       print("Total de pontos é {0}.".format(soma_pontos_jogador_01))
                       time.sleep(1)
                       
                   while soma_pontos_jogador_01 > 21: 
                           if quantos_as > 0: 
                               soma_pontos_jogador_01 -= 11
                               soma_pontos_jogador_01 += 1
                               quantos_as -= 1
                               print('')
                               print('''Porém, como você já possuia uma ou duas carta do tipo "as" sorteada no incio do jogo, ela passou a valer 1, portanto sua nova pontuação é {0}.'''.format(soma_pontos_jogador_01))
                               break
                           
                           else:
                               break
              
#para o while referente a 21 pontos ou ao caso de não querer comprar mais cartas
                
               elif mais_carta_jogador_01 == 'nao':
                   break
                   
#maldede    
           dificultar = random.choice(maquina_malandra)
           if dificultar == 'sim': 
               soma_pontos_mesa = random.randint(18,21)
                    
           else: 
               
#define as cartas da mesa 
                 
               quantos_as = 0 
               soma_pontos_mesa = 0
               baralho_aleatorio = random.choice(lista_de_baralhos)
               carta_01_mesa = random.choice(list(baralho_aleatorio.keys()))
               soma_pontos_mesa += baralho_aleatorio[carta_01_mesa]
               if carta_01_mesa == "as espadas" or carta_01_mesa == "as copas" or carta_01_mesa == "as ouros" or carta_01_mesa == "as paus":
                  quantos_as += 1 
               del baralho_aleatorio[carta_01_mesa]
               
               
               baralho_aleatorio = random.choice(lista_de_baralhos)
               carta_02_mesa = random.choice(list(baralho_aleatorio.keys()))
               soma_pontos_mesa += baralho_aleatorio[carta_02_mesa]
               if carta_02_mesa == "as espadas" or carta_02_mesa == "as copas" or carta_02_mesa == "as ouros" or carta_02_mesa == "as paus":
                  quantos_as += 1 
               del baralho_aleatorio[carta_02_mesa]
              
               if soma_pontos_mesa == 22: 
                   soma_pontos_mesa -= 11
                   soma_pontos_mesa += 1
                   quantos_as -= 1  
                 
#Deixa o jogo mais dificil
                    
               while soma_pontos_mesa <= 14:
                   baralho_aleatorio = random.choice(lista_de_baralhos)
                   carta_extra_mesa = random.choice(list(baralho_aleatorio.keys()))
                   
                   if soma_pontos_mesa > 11 and  carta_extra_mesa == "as espadas" or carta_extra_mesa == "as copas" or carta_extra_mesa == "as ouros" or carta_extra_mesa == "as paus":
                      quantos_as += 1
                      baralho_aleatorio[carta_extra_mesa] = 1
                      soma_pontos_mesa += baralho_aleatorio[carta_extra_mesa]
                      del baralho_aleatorio[carta_extra_mesa]
                     
                   else: 
                       soma_pontos_mesa += baralho_aleatorio[carta_extra_mesa]
                       del baralho_aleatorio[carta_extra_mesa]
                          
                   while soma_pontos_mesa > 21: 
                           if quantos_as > 0: 
                               soma_pontos_mesa -= 11
                               soma_pontos_mesa += 1
                               quantos_as -= 1
                               break
                           
                           else:
                               break
                            
           if soma_pontos_jogador_01 > 21:
               print ("você perdeu a rodada!!! Tururuu")
               dinero_01 -= valor_aposta_jogador_01
               
           elif soma_pontos_jogador_01 < 21 and soma_pontos_mesa > 21:
               print("Sua pontuação foi {0}.".format(soma_pontos_jogador_01))
               print('A mesa estourou!!')
               print('')
               time.sleep(1)
               print("Você venceu da mesa nesta rodada!!!")
               dinero_01 += valor_aposta_jogador_01
                   
                   
                
           elif soma_pontos_jogador_01 < soma_pontos_mesa:
               print("Sua pontuação foi {0}.".format(soma_pontos_jogador_01))
               print('A pontuação da mesa foi {0}.'.format(soma_pontos_mesa))
               print('')
               time.sleep(1)
               print("Você perdeu a rodada!!!")
               dinero_01 -= valor_aposta_jogador_01
                   
           elif soma_pontos_jogador_01 == 21:
               print ("Você venceu a rodada!!!")
               dinero_01 += valor_aposta_jogador_01
               
           elif soma_pontos_jogador_01 == soma_pontos_mesa:
               print("Sua pontuação foi {0}.".format(soma_pontos_jogador_01))
               print('A pontuação da mesa foi {0}.'.format(soma_pontos_mesa))
               print('')
               time.sleep(1)
               print("Empate!!! 'O'")
               
           else:
               print("Sua pontuação foi {0}.".format(soma_pontos_jogador_01))
               print('A pontuação da mesa foi {0}.'.format(soma_pontos_mesa))
               print('')
               time.sleep(1)
               print("Você venceu da mesa nesta rodada!!!")
               dinero_01 += valor_aposta_jogador_01
                 
        if resposta_jogador_01 == 'nao':
            print("jogo interrompido!")
            break
        
    if dinero_01 == 0:
        print('')
        print("Seu saldo acabou!! Consiga mais dinheiro para jogar novamente.")
        for i in 'GAME OVER':
            print(i)
            time.sleep(1)
    else:
        print('')
        print('O saldo final devolvido foi {0} reais.'.format(dinero_01))
        time.sleep(1.0)
        print('')
        for i in 'GAME OVER' :
            print(i)
            time.sleep(1)