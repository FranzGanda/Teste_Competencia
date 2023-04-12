primeiro_termo = 0
segundo_termo = 1
fibonacci = 0
numero_informado = int(input("Digite um numero: "))
while (fibonacci < numero_informado):
    fibonacci = primeiro_termo + segundo_termo
    primeiro_termo = segundo_termo
    segundo_termo = fibonacci
if (numero_informado == 0 or numero_informado == fibonacci):
    resposta = "Este numero pertence a sequencia de Fibonacci."
else:
    resposta = "Este numero não pertence a sequencia de Fibonacci."
print(resposta)


