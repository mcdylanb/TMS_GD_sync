from selenium import webdriver
import time

#opening chrome driver
browser = webdriver.Chrome("C:\Dylan'sFiles\Dev\Chromium-driver\chromedriver.exe")
browser.get('http://jeepme/webapp/tms/')

#add here your username and password
username = browser.find_element_by_id("ctl00_ContentPlaceHolder1_logApplication_UserName")
password = browser.find_element_by_id("ctl00_ContentPlaceHolder1_logApplication_Password")
submit_button = browser.find_element_by_id("ctl00_ContentPlaceHolder1_logApplication_LoginButton")

#automatically logins using the input from above
username.send_keys('BALAGTASM')
print("username pass")
time.sleep(2)
password.send_keys('xUbwcSc+iO')
print("password pass")
time.sleep(2)
submit_button.click()

#
browser.get("http://jeepme/webapp/tms/WebApp/TimeAttendanceLogs.aspx")

export = browser.find_element_by_id("ctl00_ContentPlaceHolder1_btnExport")
export.click()

#upload to drive.google.com

# browser.quit()