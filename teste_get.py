import requests

headers = {'Authorization': 'Token 1bba29e9145144e5d9ad2fafa8d44383b34dca5f'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)

# print(resultado.json())

# Testando se o endpoint está correto
assert resultado.status_code == 200

# Testando a quantidade de registros
assert resultado.json()['count'] == 5

# Testando se o título do primeiro curso está correto
assert resultado.json()['results'][0]['titulo'] == 'APIs REST Com DRF'
