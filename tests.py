from django.test import LiveServerTestCase
from selenium import webdriver

class AnimalsTestCase(LiveServerTestCase):
    def setUp(self):
        """ Executado no inicio de cada teste para subir um servidor de testes """
        self.browser = webdriver.Chrome('/home/robson/Projects/tdd-animals/chromedriver')

    def tearDown(self):
        """ Executado no final de cada teste para destruir o servidor de testes """
        self.browser.quit()

    def test_window_open_verify(self):
        """ Abre o navegador e acessa determinada URL """
        self.browser.get('https://cursos.alura.com.br/')

    def test_fail(self):
        """ Exempre de um teste que falha """
        self.fail('Teste Falhou - Exemplo de um teste falhando!')
