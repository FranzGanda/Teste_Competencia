sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

total_representacao = sp + rj + mg + es + outros

representacao_sp =  ( sp / total_representacao) * 100 
representacao_rj =  ( rj / total_representacao) * 100 
representacao_mg =  ( mg / total_representacao) * 100 
representacao_es =  ( es / total_representacao) * 100 
representacao_outros =  ( outros / total_representacao) * 100 

print(f'São Paulo representa {representacao_sp:.2f}%')
print(f'Rio de Janeiro representa {representacao_rj:.2f}%')
print(f'Minas Gerais representa {representacao_mg:.2f}%')
print(f'Espirito Santo representa {representacao_es:.2f}%')
print(f'Outos estados representam {representacao_outros:.2f}%')