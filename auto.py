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

def search(each):
    input = driver.find_element(By.XPATH, '//*[@id="textSearch"]')
    input.click()
    print(client_id[each])
    try:
        input.send_keys(client_id[each+1])
    except:
        return
    
    input.send_keys(Keys.ENTER)
    

    time.sleep(5)

for each in range(len(client_id)):
    search(each)




