import requests
a = str(input('Qual seu CEP?'))

while len(a) != 8:
    a = str(input('quantidade de numeros nao confere, favor inserir novamente:'))
cep = a
response = requests.get('https://viacep.com.br/ws/'+cep+'/json/')
dados_cep = response.json()

if 'erro' not in response.json():
    print('Seu logradouro é:')
    print(dados_cep['logradouro'])
    print(dados_cep['bairro'])
    print(dados_cep['localidade'])
    print(dados_cep['uf'])
else:
    (print('CEP nao localizado, favor verificar'))

