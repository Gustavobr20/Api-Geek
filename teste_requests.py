import requests

# GET Avaliações
avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# Acessando o código de status HTTP
# print(avaliacoes.status_code)


# Acessando os dados da resposta
# print(avaliacoes.json())
# print(type(avaliacoes.json()))

# Acessando a quantidade de registros
# print(avaliacoes.json()['count'])

# Acessando a próxima página de resultados
# print(avaliacoes.json()['next'])

# Acessando os resultados desta página
# print(avaliacoes.json()['results'])
# print(type(avaliacoes.json()['results']))

# Acessando o primeiro elemento da lista de resultados
# print(avaliacoes.json()['results'][0])

# Acessando somente o nome da pessoa que fez a ultima avaliação
# print(avaliacoes.json()['results'][-1]['nome'])

# Get Avaliação

# avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/1')

# print(avaliacao.json())


# GET CURSOS com autenticação via token

# Autenticação
headers = {'Authorization': 'Token 1bba29e9145144e5d9ad2fafa8d44383b34dca5f'}

cursos = requests.get(url='http://localhost:8000/api/v2/cursos/', headers=headers)
# é preciso colocar a tag url e headers para indicar a autenticação

print(cursos.status_code)

print(cursos.json())
