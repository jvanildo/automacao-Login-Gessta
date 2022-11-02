import time
import win32com.client as win32
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc
servico = Service(ChromeDriverManager().install())
if __name__ == '__main__':
  navegador = uc.Chrome(service = servico)
  navegador.get("https://app.gestta.com.br/#/sidebar/overview/dashboard?role=ROLE_ADMIN&start_date=2022-10-01T03:00:00.000Z&end_date=2022-11-01T02:59:59.999Z")
  time.sleep(5)



  navegador.find_element(By.XPATH,'//*[@id="email"]').send_keys("fiscal7@pr2consult.com.br")
  navegador.find_element(By.XPATH,'//*[@id="password"]').send_keys("Fiscal7!")
  navegador.find_element(By.XPATH, '//*[@id="login-auth-screen"]/div/div/div[2]/div/form/div[4]/div/button').click()
  time.sleep(86400)

