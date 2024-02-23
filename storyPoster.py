import time
import random
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Variáveis
USERNAME = 'juu.cardoso98'  # Insira aqui o nome de usuário ou email
PASSWORD = 'Giovanna98!'  # Insira aqui a senha de acesso

def post(arquivo):
    #Inicialização do Chrome
    chrome_options = Options()
    #Define o UserAgent como Iphone, possibilitando o upload de Stories
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
    #Define a resolução, para que o botão de upload esteja visível
    chrome_options.add_argument('--window-size=400,900')
    browser = webdriver.Chrome(options=chrome_options)
    browser.get('https://www.instagram.com/accounts/login/')
    time.sleep(random.int(3,5))

    # Login
    username = browser.find_element(By.NAME,'username')
    password = browser.find_element(By.NAME,'password')
    username.send_keys(USERNAME)
    password.send_keys(PASSWORD + Keys.ENTER)
    time.sleep(random.int(3,5))

    # Bypass Pop-Up de Salvar Senha
    browser.find_element(By.CLASS_NAME,'_ac8f').click()
    time.sleep(random.int(3,5))

    # Bypass Pop-Up de Adicionar a Home
    add_home = browser.find_element(By.CLASS_NAME,'_a9-z')
    a = add_home.find_elements(By.TAG_NAME, 'button')
    a[1].click()
    time.sleep(random.int(3,5))

    # Bypass de inatividade necessário para aparecer Pop-Up de Ligar Notificações
    ActionChains(browser)\
        .scroll_by_amount(0,20)\
        .scroll_by_amount(0,-20)\
        .perform()
    time.sleep(random.int(3,5))

    # Bypass Pop-up de Ligar Notificações
    ligar_not = browser.find_element(By.CLASS_NAME,'_a9-z')
    a = ligar_not.find_elements(By.TAG_NAME, 'button')
    a[1].click()
    time.sleep(random.int(3,5))

    time.sleep(1000)
    return "Post Realizado!"