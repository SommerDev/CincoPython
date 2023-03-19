matriz = []
for i in range(3):
    linha = []
    linha.append(input('Digite o nome do aluno ' + str(i) + ': '))
    for j in range(4):
        linha.append(float(input(f'Digite a nota {j+1} de ' + linha[0] + ': ')))
    matriz.append(linha)
print('=+' * 30)
print(f'Segue a montagem da Matriz: {matriz}')
print('=+' * 30)
# média de cada aluno:
media = 0
maior = 0
menor = 999
posicaoMaior = 0
posicaoMenor = 0
for i in range(3): # for para percorrer a linha
    media = (matriz[i][1]+matriz[i][2]+matriz[i][3]+matriz[i][4])
    media = media / 4
    if media > maior:
        maior = media
        posicaoMaior = i
    if media < menor:
        menor = media
        posicaoMenor = i
    print(f'A média do aluno {matriz[i][0]} é {media}')
print('=+' * 30)    
print (f'O aluno {matriz[posicaoMaior][0]} tem a maior média: {maior}')
print (f'O aluno {matriz[posicaoMenor][0]} tem a maior média: {menor}')

