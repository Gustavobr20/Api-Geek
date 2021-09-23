import requests

headers = {'Authorization': 'Token 1bba29e9145144e5d9ad2fafa8d44383b34dca5f'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

# Cadastrar novo curso
novo_curso = {
    "titulo": "Curso de JavaScript do Básico ao Avançado",
    "url": "http://www.udemy.com"
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)

# Testando o código de status HTTP 201
assert resultado.status_code == 201

# Testando se o título do curso criado ou retornado é o mesmo do informado
assert resultado.json()['titulo'] == novo_curso['titulo']
