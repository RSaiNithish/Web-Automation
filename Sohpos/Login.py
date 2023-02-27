from selenium import webdriver
from selenium.webdriver.common.by import By
import time

Uname = "[Username]"
Key = "[Password]"
options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')

browser = webdriver.Chrome(executable_path ="E:\Things\Py res\chromedriver_win32\chromedriver.exe", chrome_options=options)


website_URL ="https://192.168.34.1:8090/httpclient.html"
browser.get(website_URL)
time.sleep(2)
a = browser.find_element(By.XPATH,'//*[@id="username"]')
a.send_keys(Uname)
b = browser.find_element(By.XPATH,'//*[@id="password"]')
b.send_keys(Key)
browser.find_element(By.XPATH,'//*[@id="loginbutton"]').click()

print("Login Sucessful")
browser.minimize_window()
