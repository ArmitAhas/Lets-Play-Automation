import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

user = input("Enter username : ")
password = input("Enter password : ")
to_email = input("Enter receiver email : ")
subject = input("Enter subject : ")
text = input("Enter your text : ")

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()

driver.get("https://www.gmail.com/")
time.sleep(2)

user_box = driver.find_element(By.ID,'identifierId')
user_box.send_keys(user)

btn = driver.find_element(By.ID,"identifierNext")
btn.click()
time.sleep(5)

pass_box= driver.find_element(By.ID,'passwordNext')
pass_box.send_keys(password)
time.sleep(5)

compose_btn = driver.find_element(By.XPATH,'//div[contains(text(),"Compose")]')
compose_btn.click()

to_email_box= driver.find_element(By.ID,':19j')
to_email_box.send_keys(to_email)

subject_box= driver.find_element(By.ID,':15m')
subject_box.send_keys(subject)

text_box = driver.find_element(By.ID,":16v")
text_box.click()
text_box.send_keys(text)

driver.get_screenshot_as_file('sending_email.png')

send_btn = driver.find_element(By.ID,":15c")
send_btn.click()
time.sleep(5)


driver.quit()


