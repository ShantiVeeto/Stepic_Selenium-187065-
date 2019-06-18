# Задание - ждем нужный текст на странице
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import log, sin

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# Ждем цены 10000 RUR и жмем забронировать
price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR"))
browser.find_element_by_id("book").click()

# Капча для роботов (task2_1_1.py)
x = browser.find_element_by_css_selector('[id = "input_value"]').text
browser.find_element_by_css_selector('[id = "answer"]').send_keys(str(log(abs(12 * sin(int(x))))))

# Отправляем заполненную форму
browser.find_element_by_id("solve").click()