import json

with open("dados.json", encoding='utf-8') as dados_json:
    faturamento_mensal = json.load(dados_json)

maior_faturamento = 0

for cursor in faturamento_mensal:    
   if(cursor['valor'] > maior_faturamento):
        maior_faturamento  = cursor['valor']    

print('O maior dia de faturamento no mês foi de', maior_faturamento)

menor_faturamento = maior_faturamento

for cursor in faturamento_mensal:    
   if(cursor['valor'] < menor_faturamento and cursor['valor'] != 0):        
   
        menor_faturamento = cursor['valor']

print('O menor dia de faturamento no mês foi de', menor_faturamento)

total_mensal_faturamento = 0
total_mensal_faturamento = 0
dias_faturamento = 0
dias_faturamento_superior_media = 0

for cursor in faturamento_mensal:
    if(cursor['valor'] != 0):
        total_mensal_faturamento = total_mensal_faturamento + cursor['valor']
        dias_faturamento = dias_faturamento + 1

media_faturamento = total_mensal_faturamento / dias_faturamento

for cursor in faturamento_mensal:
    if(cursor['valor'] > media_faturamento):
        dias_faturamento_superior_media = dias_faturamento_superior_media + 1

print('Foram', dias_faturamento_superior_media, 'dias com faturamento superior a média ')