import requests


class TestCursos:
    headers = {'Authorization': 'Token 1bba29e9145144e5d9ad2fafa8d44383b34dca5f'}
    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        resposta = requests.get(url=self.url_base_cursos, headers=self.headers)

        assert resposta.status_code == 200

    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url_base_cursos}5/', headers=self.headers)

        assert resposta.status_code == 200

    def test_post_curso(self):
        novo_curso = {
            "titulo": "Curso de programação com Ruby10",
            "url": "www.udemy.com/ruby10"
        }
        resposta = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo_curso)

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo_curso['titulo']

    def test_put_curso(self):
        atualizado = {
            "titulo": "Novo Curso de Ruby 3",
            "url": "www.udemy.com/novo-ruby 3"
        }
        resposta = requests.put(url=f'{self.url_base_cursos}5/', headers=self.headers, data=atualizado)

        assert resposta.status_code == 200

    def test_put_titulo_curso(self):
        atualizado = {
            "titulo": "Novo Curso de Ruby22",
            "url": "www.udemy.com/novo-ruby22"
        }
        resposta = requests.put(url=f'{self.url_base_cursos}5/', headers=self.headers, data=atualizado)

        assert resposta.json()['titulo'] == atualizado['titulo']

    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_base_cursos}4/', headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0
