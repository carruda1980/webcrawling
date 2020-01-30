from selenium import webdriver

# import sqlite3
#
# conn = sqlite3.connect('dados.db')
# # definindo um cursor
# cursor = conn.cursor()
#
# # criando a tabela (schema)
# cursor.execute("""
# CREATE TABLE dados (
#         id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#         texto TEXT NOT NULL
# );
# """)
#
# print('Tabela criada com sucesso.')

class Google:
    def __init__(self, driver):
        self.driver = driver
        # self.url = 'http://google.com.br' # url a ser crawleada
        self.url = 'https://meu.xxxxx.com.br/' # url a ser crawleada
        self.user = 'user' # element name
        self.password = 'password' # element name
        # self.search_bar = 'q' # element name
        # self.btn_search = 'btnK' # element name
        self.btn_login = 'btn-login' # element name
        # self.class_search = 'st'

    # Inicia a navegação
    def navigate(self):
        self.driver.get(self.url)

    # Faz a busca passando como paramentro a palavra e da o submit na busca
    def login(self, user='None', password='None'):
        self.driver.find_element_by_name(
            self.user).send_keys(user)
        self.driver.find_element_by_name(
            self.password).send_keys(password)
        self.driver.find_element_by_id(self.btn_login).submit()
    # def search(self, word='None'):
    #     self.driver.find_element_by_name(
    #         self.search_bar).send_keys(word)
    #     self.driver.find_element_by_name(self.btn_search).submit()

    # def dataclass(self):
    #     import ipdb; ipdb.set_trace()
    #     classe = self.driver.find_elements_by_class_name("st")
    #     count = 1
    #     for c in classe:
    #         print(c.text)
    #         cursor.execute('INSERT INTO dados VALUES(?,?)', (count, c.text,))
    #
    #         conn.commit()
    #         count +=1
    #
    #         print('Dados inseridos com sucesso.')
    #
    #     conn.close()

# Web driver Firefox
wbf = webdriver.Firefox()

# Instanciando o objeto
google = Google(wbf)

# Navegando
google.navigate()

# Buscandon
# google.search('Live de python')
google.login('xxxxxxxxx@gmail.com', 'xxxxx')

# google.dataclass()
