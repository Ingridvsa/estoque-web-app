import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class EstoqueTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:5000/")
        time.sleep(1)

    def cadastrar_produto(self, nome="teste", preco="10.00", quantidade="5"):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Cadastrar Produto").click()
        time.sleep(1)
        driver.find_element(By.NAME, "name").send_keys(nome)
        driver.find_element(By.NAME, "price").send_keys(preco)
        driver.find_element(By.NAME, "quantity").send_keys(quantidade)
        driver.find_element(By.NAME, "submit").click()
        time.sleep(1)

    def test_cadastrar_produto(self):
        self.cadastrar_produto()
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.find_element(By.LINK_TEXT, "Visualizar Estoque").click()
        time.sleep(1)
        body = self.driver.find_element(By.TAG_NAME, "body").text.lower()
        self.assertIn("teste", body)
        self.assertIn("un", body)

    def test_adicionar_estoque(self):
        self.cadastrar_produto()
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Adicionar ao Estoque").click()
        time.sleep(1)
        driver.find_element(By.NAME, "name").send_keys("teste")
        driver.find_element(By.NAME, "amount").send_keys("3")
        driver.find_element(By.TAG_NAME, "button").click()
        time.sleep(1)

        driver.get("http://127.0.0.1:5000/")
        driver.find_element(By.LINK_TEXT, "Visualizar Estoque").click()
        time.sleep(1)
        body = driver.find_element(By.TAG_NAME, "body").text.lower()
        self.assertIn("teste", body)

    def test_remover_estoque(self):
        self.cadastrar_produto()
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Remover do Estoque").click()
        time.sleep(1)
        driver.find_element(By.NAME, "name").send_keys("teste")
        driver.find_element(By.NAME, "amount").send_keys("2")
        driver.find_element(By.TAG_NAME, "button").click()
        time.sleep(1)

        driver.get("http://127.0.0.1:5000/")
        driver.find_element(By.LINK_TEXT, "Visualizar Estoque").click()
        time.sleep(1)
        body = driver.find_element(By.TAG_NAME, "body").text.lower()
        self.assertIn("teste", body)

    def test_atualizar_nome(self):
        self.cadastrar_produto()
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Atualizar Nome").click()
        time.sleep(1)
        driver.find_element(By.NAME, "current_name").send_keys("teste")
        driver.find_element(By.NAME, "new_name").send_keys("produto-teste")
        driver.find_element(By.TAG_NAME, "button").click()
        time.sleep(1)

        driver.get("http://127.0.0.1:5000/")
        driver.find_element(By.LINK_TEXT, "Visualizar Estoque").click()
        time.sleep(1)
        body = driver.find_element(By.TAG_NAME, "body").text.lower()
        self.assertIn("produto-teste", body)

def test_atualizar_preco(self):
    self.cadastrar_produto(nome="produto-teste", preco="10.00", quantidade="18")
    driver = self.driver
    driver.find_element(By.LINK_TEXT, "Atualizar Preço").click()
    time.sleep(1)
    driver.find_element(By.NAME, "name").send_keys("produto-teste")
    driver.find_element(By.NAME, "price").send_keys("19.99")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)

    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.LINK_TEXT, "Visualizar Estoque").click()
    time.sleep(1)

    body = driver.find_element(By.TAG_NAME, "body").text
    self.assertIn("R$ 359.82", body)  # 18 × 19.99


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()


