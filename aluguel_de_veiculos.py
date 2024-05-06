dias = int(input('\033[34mQuantos dias o veiculo ficou alugado? '))
km = float(input('\033[34mQuantos km o veiculo rodou? '))
custo = dias * 60 + km * 0.15
print('\033[36mO valor do aluguel ficou em: R$ \033[31m{:.2f}'.format(custo))
