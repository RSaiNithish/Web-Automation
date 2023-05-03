import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def init():
	options = webdriver.ChromeOptions()
	options.add_argument('ignore-certificate-errors')

	browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
	return browser

def login(username,pas,browser):
    website_URL ="https://exam.sssihl.edu.in/mod/feedback/complete.php?id=13125&courseid"
    browser.get(website_URL)
    time.sleep(1)
    email = browser.find_element(By.XPATH,'//*[@id="username"]')
    email.send_keys(username)
    pswd = browser.find_element(By.XPATH,'//*[@id="password"]')
    pswd.send_keys(pas)
    login = browser.find_element(By.XPATH,'//*[@id="loginbtn"]')
    login.click()
    

def check_form(url):   
    browser.get(url)
    for i in range(15):
        a = browser.find_element(By.XPATH,f'//*[@id="id_multichoicerated_600{37+i}_6"]')
        a.click()
    browser.find_element(By.XPATH,'//*[@id="id_savevalues"]').click()


browser = init()
login("user","pswd",browser)
check_form("https://exam.sssihl.edu.in/mod/feedback/complete.php?id=13125&courseid")
check_form("https://exam.sssihl.edu.in/mod/feedback/complete.php?id=13126&courseid")
check_form("https://exam.sssihl.edu.in/mod/feedback/complete.php?id=13127&courseid")
browser.close()
