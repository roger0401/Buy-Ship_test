from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# 設定 Chrome 選項（可選）
chrome_options = Options()

# 初始化 WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# 打開網站
driver.get('https://www.buyandship.com.tw/')

wait = WebDriverWait(driver, 30)

# 使用 CSS Selector 生成選擇器
for i in range (1,14):
    '''
    點擊選擇區域按鈕
    選擇區域
    回到台灣區
    重複上述動作
    '''
    button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'bs-header-top-bar__content__country__text')))
    button.click()
    css_selector = f"body > aside > div.bs-dialog-full-container > div.bs-dialog-full__body > ul > a:nth-child({i}) > span.bs-language-list__item__name"
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()
    driver.get('https://www.buyandship.com.tw/')

# 關閉瀏覽器
driver.quit()
