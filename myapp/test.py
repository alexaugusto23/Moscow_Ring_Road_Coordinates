import unittest
from app import app
import re

# url = "https://www.bytebank.com.br/cambio"
# padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
# match = padrao_url.match(url)

# if not match:
#     raise ValueError("A URL não é válida.")
# print("A URL é válida.")


class TestHomeView(unittest.TestCase):

    '''
      Como todos os 3 casos de teste fazem um get na home "/"
      da nossa aplicacao, definimos a funcao setUp. Ela e executada
      automaticamente sempre que o Pytest instancia a classe TestHomeView.
      A funcao setUp e semelhante a um metodo construtor.
    '''

    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')

    def setUp(self):
        my_app = app.test_client()
        self.response_root = my_app.get('/')
        self.response_form = my_app.get('/form')

    # Testamos se a resposta e 200 ("ok")
    def test_get(self):
        self.assertEqual(200, self.response_root.status_code)

    # Testamos se o content_type da resposta da home esta correto
    def test_content_type(self):
        self.assertIn('text/html', self.response_root.content_type)

    # Testamos se a nossa home retorna a string "ok"
    def test_html_string_response(self):
        self.assertEqual("ok", self.response_form.data.decode('utf-8'))
    
     
if __name__ == '__main__':
   log_file = 'log_file.txt'
   with open(log_file, "w") as file:
       runner = unittest.TextTestRunner(file)
       unittest.main(testRunner=runner)
       runner.close()

# python -m unittest test.py