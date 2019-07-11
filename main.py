from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import random
import string
import names

# For Generating Random Emails
def random_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

# Open The Chrome Window
chromedriver_path = r'C:\Users\Downloads\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)

# Open the Discord Register Page
driver.get('https://discordapp.com/register')
sleep(2)
email = random_generator()
email = f'{email}@gmail.com'
print(email)
email1 = 'abcd@gmail.com'
# Put the stuff in
email = driver.find_element_by_name('email')
email.send_keys(email1)
username1 = names.get_first_name()
username = driver.find_element_by_name('username')
username.send_keys(f'{username1}{random_generator(size=3)}')
print(f'{username}{random_generator(size=3)}')
password = driver.find_element_by_name('password')
password1 = random_generator()
password2 = 'test123'
password.send_keys(password2)
print(password1)

continueb = driver.find_element_by_css_selector('#app-mount > div.app-19_DXt.platform-web > div > div.leftSplit-1qOwnR.hasLogo-2bq2VW > div > form > div > div.block-egJnc0.marginTop20-3TxNs6 > div:nth-child(4) > button').click()
sleep(2)
