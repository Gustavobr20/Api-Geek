import requests

headers = {'Authorization': 'Token 1bba29e9145144e5d9ad2fafa8d44383b34dca5f'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

curso_atualizado = {
    "titulo": "Novo Curso de Python 3",
    "url": "www.udemy.com.br/python3"
}

# Buscando o curso com id 1
# curso = requests.get(url=f'{url_base_cursos}1/', headers=headers)
# print(curso.json())


resultado = requests.put(url=f'{url_base_cursos}6/', headers=headers, data=curso_atualizado)

# Testando o código de status HTTP
assert resultado.status_code == 200

# Testando o título
assert resultado.json()['titulo'] == curso_atualizado['titulo']
