#driver
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import date
from api.api import main
valores, sheet = main()

#login automatico
from config import CHROME_PROFILE_PATH

#planilha
import pandas as pd
document = pd.DataFrame(valores, columns=valores[0]).drop(0,axis=0).reset_index(drop=True)
# print(document.head)

#driver
options = webdriver.ChromeOptions()
options.add_argument(CHROME_PROFILE_PATH)
driver = webdriver.Chrome(options=options)
driver.get("https://app.contaazul.com/#/financeiro/contas-a-receber?view=revenue&amp;source=Financeiro%20%3E%20Contas%20a%20Receber&source=Menu%20Principal")

#starting
client_id = document['ID DO CLIENTE']

while True:
    try:
        control = driver.find_element(By.XPATH, '//*[@id="statement-list-container"]/table[1]/tbody')
        if (control):
            time.sleep(1)
            break
    except:
        time.sleep(2)


#exibir
driver.find_element(By.XPATH, '//*[@id="type-filter-controller"]/span').click()
time.sleep(.5)

#recebido
driver.find_element(By.XPATH, '//*[@id="typeFilterContainer"]/li[4]/a/span[1]').click()

#aplicar
driver.find_element(By.XPATH, '//*[@id="type-filter"]/ul/li[2]/div/button').click()
time.sleep(3)

#filtrar contas
driver.find_element(By.XPATH, '//*[@id="bank-filter"]/button').click()

#all
#listar a ordem e largar num loop
driver.find_element(By.XPATH, '//*[@id="bank-filter"]/ul/li[1]/a/span[1]').click()
time.sleep(0.3)

#bradesco
driver.find_element(By.XPATH, '//*[@id="bank-filter"]/ul/div/li[2]/a/span').click()

#itau
driver.find_element(By.XPATH, '//*[@id="bank-filter"]/ul/div/li[3]/a/span').click()

#sap
driver.find_element(By.XPATH, '//*[@id="bank-filter"]/ul/div/li[4]/a/span').click()

#sicredi
driver.find_element(By.XPATH, '//*[@id="bank-filter"]/ul/div/li[5]/a/span').click()

#churn provavel
driver.find_element(By.XPATH, '//*[@id="bank-filter"]/ul/div/li[9]/a/span').click()

#inad
driver.find_element(By.XPATH, '//*[@id="bank-filter"]/ul/div/li[10]/a/span').click()

#franq inad
driver.find_element(By.XPATH, '//*[@id="bank-filter"]/ul/div/li[11]/a/span').click()

#nova data
driver.find_element(By.XPATH, '//*[@id="bank-filter"]/ul/div/li[16]/a/span').click()

#cartao iugu
driver.find_element(By.XPATH, '//*[@id="bank-filter"]/ul/div/li[35]/a/span').click()

#renovaçao
driver.find_element(By.XPATH, '//*[@id="bank-filter"]/ul/div/li[42]/a/span').click()

#aplicar
driver.find_element(By.XPATH, '//*[@id="bank-filter"]/ul/li[3]/div/button').click()
time.sleep(3)

#ir para cima
driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.CONTROL, Keys.HOME)
time.sleep(1)

#filtrar data
driver.find_element(By.XPATH, '//*[@id="financeTopFilters"]/div[2]/button/span').click()

#mostrar todos
driver.find_element(By.XPATH, '//*[@id="financeTopFilters"]/div[2]/ul/li[5]/a').click()
time.sleep(3)

def search(each):
    input = driver.find_element(By.XPATH, '//*[@id="textSearch"]')
    input.click()
    input.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
    try:
        input.send_keys(client_id[each+1])
    except:
        return
    
    input.send_keys(Keys.ENTER)
    

    time.sleep(5)

for each in range(len(client_id)):
    search(each)




