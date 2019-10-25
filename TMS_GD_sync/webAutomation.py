from selenium import webdriver
import time

#users input
print('please enter username and password for tms')
tms_username = input("enter username:")
tms_password = input("enter password:")

print('please enter username and password for google')
google_username = input("enter username:")
google_password = input("enter password:")

#opening chrome driver
browser = webdriver.Chrome("C:\Dylan'sFiles\Dev\Chromium-driver\chromedriver.exe")
browser.get('http://jeepme/webapp/tms/')

#gets input boxes and buttons
username_tms = browser.find_element_by_id("ctl00_ContentPlaceHolder1_logApplication_UserName")
password_tms = browser.find_element_by_id("ctl00_ContentPlaceHolder1_logApplication_Password")
submit_button_tms = browser.find_element_by_id("ctl00_ContentPlaceHolder1_logApplication_LoginButton")

#automatically logins using the input from above
username_tms.send_keys('BALAGTASM')
print("username pass")
time.sleep(2)
password_tms.send_keys('xUbwcSc+iO')
print("password pass")
time.sleep(2)
submit_button_tms.click()

#opens page with data
browser.get("http://jeepme/webapp/tms/WebApp/TimeAttendanceLogs.aspx")

#clicks on the export button
export = browser.find_element_by_id("ctl00_ContentPlaceHolder1_btnExport")
export.click()

#upload to drive.google.com

#opens google login page
browser.get('https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Dgoogle%2Blogin%26rlz%3D1C1GCEU_enPH868PH868%26oq%3Dgoogle%2Blogin%26aqs%3Dchrome..69i57j69i64.2367j0j1%26sourceid%3Dchrome%26ie%3DUTF-8&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

#gets input boxes and buttons for username
username_google = browser.find_element_by_id("identifierId")
next_btn_username_google = browser.find_element_by_id("identifierNext")


username_google.send_keys(google_username)
time.sleep(2)
next_btn_username_google.click()
time.sleep(2)

#gets input boxes and buttons for password
password_google = browser.find_element_by_name("password")
next_btn_password_google = browser.find_element_by_id('passwordNext')

password_google.send_keys(google_password)
time.sleep(2)
next_btn_password_google.click()
time.sleep(2)

browser.get('https://drive.google.com/drive/u/0/folders/1by0DliV7j4oHm_-RT0XA6IQ3SCRmkmPf')

# browser.quit()