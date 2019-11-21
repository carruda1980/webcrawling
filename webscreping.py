from selenium import webdriver


class Google:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://google.com.br' # url a ser crawleada
        self.search_bar = 'q' # element name
        self.btn_search = 'btnK' # element name

    # Inicia a navegação
    def navigate(self):
        self.driver.get(self.url)

    # Faz a busca passando como paramentro a palavra e da o submit na busca
    def search(self, word='None'):
        self.driver.find_element_by_name(
            self.search_bar).send_keys(word)
        self.driver.find_element_by_name(self.btn_search).submit()

# Web driver Firefox
wbf = webdriver.Firefox()

# Instanciando o objeto
google = Google(wbf)

# Navegando
google.navigate()

# Buscando
google.search('Live de python')