
precos = [
    [150, 200, 180, 220, 170],
    [155, 205, 185, 225, 175],
    [160, 210, 190, 230, 180],
    [165, 215, 195, 235, 185],
    [170, 220, 200, 240, 190],
    [175, 225, 205, 245, 195],
    [180, 230, 210, 250, 200]
]

media = [0, 0, 0, 0, 0]
variacao = [0, 0, 0, 0, 0]
maiorpreco_B = -float('inf')
menorpreco_B = float('inf')
dia_maiorpreco_B = -1
dia_menorpreco_B = -1
numdias = 7
empresas = 5

for i in range(empresas):
    soma = 0
    maximo = -float('inf')
    minimo = float('inf')
    for j in range(numdias):
        preco = precos[j][i]
        soma += preco
        if preco > maximo:
            maximo = preco
        if preco < minimo:
            minimo = preco
        if i == 1:  
            if preco > maiorpreco_B:
                maiorpreco_B = preco
                dia_maiorpreco_B = j + 1
            if preco < menorpreco_B:
                menorpreco_B = preco
                dia_menorpreco_B = j + 1
    media[i] = soma / numdias
    variacao[i] = maximo - minimo

print("A média dos preços das ações ao longo da semana é:")
print(media)

print("A variação diária das ações ao longo da semana:")
print(variacao)

print("O dia em que a empresa B teve o maior preço foi:", dia_maiorpreco_B)
print("O dia em que a empresa B teve o menor preço foi:", dia_menorpreco_B)

precosacoes_aumentados = []
for i in range(numdias):
    precosdia = []
    for j in range(empresas):
        precosdia.append(precos[i][j] * 1.05)
    precosacoes_aumentados.append(precosdia)

nova_media_diaria = [0, 0, 0, 0, 0]
for i in range(empresas):
    soma = 0
    for j in range(numdias):
        soma += precosacoes_aumentados[j][i]
    nova_media_diaria[i] = soma / numdias

print("A média diária após aumento de 5% é:")
print(nova_media_diaria)
