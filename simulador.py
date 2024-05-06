import random

# Sorteia se você ganhou o 50/50
def fifty():

    # ff é de fifty fifty, e essa parte só faz um sorteio com 50% de chance
    ff = random.randint(1, 2)

    # O código sempre simula uma situação onde você não tem o próximo banner garantido
    if ff == 1:
        print('Ganhou o 50/50')
    if ff == 2:
        print('Perdeu o 50/50')


# O código repete quando aperta enter
while True:
    input('')

    # t4 conta a quantidade de itens 4 estrelas, e pT4 é o pity de 4 estrelas (1 garantido em cada 10 tiros)
    t4 = 0
    pT4 = 0

    # Simula os tiros até conseguir um personagem t5
    for x in range(90):
        
        rng = random.randint(1, 1000)
        pT4 += 1

        # Baseado no número sorteado informa se o item adquirido foi t4 ou t5, se não for nenhum dos dois o código não informa
        if x < 75:
            if rng <=6:
                print('5 estrelas')
                print(f'{t4} 4 estrelas')
                print(f'{x+1} tiros')
                fifty()
                break
            elif 6 < rng < 57:
                t4 += 1
                pT4 = 0
        elif x == 89:
            print('5 estrelas')
            print(f'{t4} 4 estrelas')
            print(f'{x+1} tiros')
            fifty()
            break
        else:
            if rng <=16:
                print('5 estrelas')
                print(f'{t4} 4 estrelas')
                print(f'{x+1} tiros')
                fifty()
                break
            elif 16 < rng < 67:
                t4 += 1
                pT4 = 0
        if pT4 == 9:
            pT4 = 0
            t4 +=1


# Auto-lembrete: colocar os prints fora do loop depois