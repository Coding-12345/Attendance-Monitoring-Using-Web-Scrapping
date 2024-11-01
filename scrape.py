from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
from twilio.rest import Client

driver = webdriver.Chrome()
driver.get("https://www.webprosindia.com/Gokaraju/")

username = driver.find_element(By.XPATH, '//*[@id="txtId2"]')
username.send_keys("2124******") #Enter respective UserId.

password = driver.find_element(By.ID, "txtPwd2")
password.send_keys("01******") #Enter respective Passcode

login = driver.find_element(By.ID, "imgBtn2")
login.click()

time.sleep(8)
marks = driver.find_element(By.XPATH, '//*[@id="tblscreens"]/tbody/tr[29]/td[2]/div/a')
marks.click()
frames_add = driver.find_element(By.ID, 'capIframeId')
driver.switch_to.frame(frames_add)

performance = driver.find_element(By.XPATH, '//*[@id="divMarks"]/table/tbody/tr[5]/td/table/tbody/tr[4]/td[11]')
message = f"Your previous attendence is {performance.text}%"

account_sid = '***************************' #Enter your account SID
auth_token = '*****************' #Enter auth token
client = Client(account_sid, auth_token)

message = client.messages.create(
    body=f"{message}",
    from_="+***********",
    to='+91**********' #Enter your number.
)