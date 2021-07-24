import time
print('Olá, bem vindo ao assistente de criptografia.')
f = input('Por favor, informe a frase:')

# verificar se o usuário inseriu uma frase
while (len(f) <= 6):
    # Pedir a frase novamente
    f = input('Informe a frase, por favor:')

print(f'A frase original é: {f}')

# Início da criptografia; crie uma variável tipo char para representar a frase criptografada
c = ''

# Pega a hora do sistema
hora = time.strftime('%H', time.localtime())
minuto = time.strftime('%M', time.localtime())
segundo = time.strftime('%S', time.localtime())

# Define a fórmula com base na hora do sistema
h = int(hora)
m = int(minuto)
s = int(segundo)

z = (s * m * h)

while (z < 0):
    z += 100
while (z > 127):
    z -= 100

# Crie uma fórmula, o resultado numérico deve ser correspondente a um char da tabela ASCII
for i in range(0, len(f)):
    cd = ord(f[i]) + z
    nc = chr(cd)
    c += nc

# Mostra a nova frase
print('Aqui está sua frase criptografada:')
print(c)

x = input('Deseja descriptografar? Responda sim ou não:')

while ((x != 'sim') and (x != 'não')):
    x = input('Inválido. Responda novamente.')

if (x == 'sim'):
    print(f)
    print('Obrigada por utilizar nosso programa!')

elif (x == 'não'):
    print('Obrigada por utilizar nosso programa!')
