import unittest
from app import app
import re

class TestHomeView(unittest.TestCase):

    '''
      As all 3 test cases do a get home "/"
      from our application, we define the setUp function. she is executed
      automatically whenever unittest instantiates the TestHomeView class.
      The setUp function is similar to a constructor method.
    '''

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