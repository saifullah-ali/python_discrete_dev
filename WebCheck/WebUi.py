from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
import re
import smtplib, ssl
#Code developed by Saifullah Ali

email_init = 0
email_body = "Below Items found :\n"
print("Customized search automation:: Browser Chrome")
ex_path = r'C:\Users\Saifullah Ali\.PyCharmCE2018.3\config\scratches\chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options = options, executable_path=ex_path)

main_window = driver.current_window_handle
driver.set_page_load_timeout(60)
print("SR1")
driver.get("https://www.costco.ca/northrock-sr1-68.58-cm-(27-in.)-road-bike.product.100674087.html")
time.sleep(5)
driver.find_element_by_css_selector("input[type='radio'][value='ON']").click()
time.sleep(5)
driver.find_element_by_id("language-region-set").click()
time.sleep(5)
try:
    driver.find_element_by_xpath("//h1[text()='Product not found!']")
    print("SR1 not found")
except:
    print("SR1 found")
    email_init = 1
    email_body = email_body + "SR1 [https://www.costco.ca/northrock-sr1-68.58-cm-(27-in.)-road-bike.product.100674087.html]\n"

driver.close()

time.sleep(5)
driver = webdriver.Chrome(options = options, executable_path=ex_path)
main_window = driver.current_window_handle
driver.set_page_load_timeout(60)
print("XC29")
driver.get("https://www.costco.ca/northrock-xc29-73.6-cm-%2829-in.%29-mountain-bike.product.100674055.html")
time.sleep(5)
driver.find_element_by_css_selector("input[type='radio'][value='ON']").click()
time.sleep(5)
driver.find_element_by_id("language-region-set").click()
time.sleep(5)
try:
    driver.find_element_by_xpath("//h1[text()='Product not found!']")
    print("XC29 not found")
except:
    print("XC29 found")
    email_init = 1
    email_body = email_body + "XC29 [https://www.costco.ca/northrock-xc29-73.6-cm-%2829-in.%29-mountain-bike.product.100674055.html]\n"

driver.close()

time.sleep(5)
driver = webdriver.Chrome(options = options, executable_path=ex_path)
main_window = driver.current_window_handle
driver.set_page_load_timeout(60)
print("XC27")
driver.get("https://www.costco.ca/northrock-xc27-69.9-cm-%2827.5-in.%29-mountain-bike.product.100673681.html")
time.sleep(5)
driver.find_element_by_css_selector("input[type='radio'][value='ON']").click()
time.sleep(5)
driver.find_element_by_id("language-region-set").click()
time.sleep(5)
try:
    driver.find_element_by_xpath("//h1[text()='Product not found!']")
    print("XC27 not found")
except:
    print("XC27 found")
    email_init = 1
    email_body = email_body + "XC27 [https://www.costco.ca/northrock-xc27-69.9-cm-%2827.5-in.%29-mountain-bike.product.100673681.html]\n"

driver.close()

time.sleep(5)
driver = webdriver.Chrome(options = options, executable_path=ex_path)
main_window = driver.current_window_handle
driver.set_page_load_timeout(60)
print("XCW")
driver.get("https://www.costco.ca/northrock-xcw-66-cm-%2826-in.%29-mountain-crossover-bike.product.100673608.html")
time.sleep(5)
driver.find_element_by_css_selector("input[type='radio'][value='ON']").click()
time.sleep(5)
driver.find_element_by_id("language-region-set").click()
time.sleep(5)
try:
    driver.find_element_by_xpath("//h1[text()='Product not found!']")
    print("XCW not found")
except:
    print("XCW found")
    email_init = 1
    email_body = email_body + "XCW [https://www.costco.ca/northrock-xcw-66-cm-%2826-in.%29-mountain-crossover-bike.product.100673608.html]\n"

driver.quit()

time.sleep(5)

if email_init == 0:
    email_body = "No Items found this time :( "

print(email_body)


port = 587  # For SSL
smtp_server = "smtp.gmail.com"
password = "%$$$"
sender_email = "notificati.product.13@gmail.com"
receiver_email = "abcd"
message = """\
Subject:[DoNotReply] Automated Notification

""" + email_body
context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()
    server.starttls(context=context)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

