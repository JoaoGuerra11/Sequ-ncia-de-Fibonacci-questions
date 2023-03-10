# Sequência de Fibonacci
numero = int(input("Digite um número inteiro para verificar se pertence à sequência de Fibonacci: "))
if numero < 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    anterior, atual = 0, 1
    while atual < numero:
        proximo = anterior + atual
        anterior = atual
        atual = proximo
    if atual == numero:
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")

# Vetor que guarda o valor de faturamento diário de uma distribuidora
with open('faturamento.json') as f:
    faturamento = json.load(f)
minimo = float('inf')
maximo = float('-inf')
for valor in faturamento:
    if valor < minimo:
        minimo = valor
    if valor > maximo:
        maximo = valor
soma = 0
dias_com_faturamento = 0
for valor in faturamento:
    if valor > 0:
        soma += valor
        dias_com_faturamento += 1
media = soma / dias_com_faturamento
dias_acima_da_media = 0
for valor in faturamento:
    if valor > media:
        dias_acima_da_media += 1
print(f'Menor faturamento: R$ {minimo:.2f}')
print(f'Maior faturamento: R$ {maximo:.2f}')
print(f'Número de dias com faturamento acima da média mensal: {dias_acima_da_media}')
faturamento_por_estado = {'SP': 67836.43, 'RJ': 36678.66, 'MG': 29229.88, 'ES': 27165.48, 'Outros': 19849.53}
total_faturamento = sum(faturamento_por_estado.values())
percentual_por_estado = {estado: (faturamento / total_faturamento) * 100 for estado, faturamento in faturamento_por_estado.items()}
print('Percentual de representação do faturamento por estado:')
for estado, percentual in percentual_por_estado.items():
    print(f'{estado}: {percentual:.2f}%')
entrada = input('Digite uma string para ser invertida: ')
saida = ''
for i in range(len(entrada) - 1, -1, -1):
    saida += entrada[i]
print(f'String invertida: {saida}')

# detalhado por estado
faturamento_por_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

try:
    total = sum(faturamento_por_estado.values())
except TypeError:
    print('Erro: Valor inválido encontrado.')
    total = 0

valor_total_esperado = 180759.98
if total != valor_total_esperado:
    print(f'Aviso: Valor total de faturamento inesperado. Esperado: {valor_total_esperado:.2f}, '
          f'Encontrado: {total:.2f}')

for estado, valor in faturamento_por_estado.items():
    try:
        percentual = (valor / total) * 100
    except Zero



