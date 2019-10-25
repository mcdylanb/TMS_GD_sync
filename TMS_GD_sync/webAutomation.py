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
tms_username_input = browser.find_element_by_id("ctl00_ContentPlaceHolder1_logApplication_UserName")
tms_password_input = browser.find_element_by_id("ctl00_ContentPlaceHolder1_logApplication_Password")
tms_submit_button = browser.find_element_by_id("ctl00_ContentPlaceHolder1_logApplication_LoginButton")

#automatically logins using the input from above
tms_username_input.send_keys('BALAGTASM')
print("username pass")
time.sleep(2)
tms_password_input.send_keys('xUbwcSc+iO')
print("password pass")
time.sleep(2)
tms_submit_button.click()

#opens page with data
browser.get("http://jeepme/webapp/tms/WebApp/TimeAttendanceLogs.aspx")

#clicks on the export button
export = browser.find_element_by_id("ctl00_ContentPlaceHolder1_btnExport")
export.click()

#upload to drive.google.com

#opens google login page
browser.get('https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Dgoogle%2Blogin%26rlz%3D1C1GCEU_enPH868PH868%26oq%3Dgoogle%2Blogin%26aqs%3Dchrome..69i57j69i64.2367j0j1%26sourceid%3Dchrome%26ie%3DUTF-8&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

#gets input boxes and buttons for username
google_username_inp = browser.find_element_by_id("identifierId")
googlenext_btn_username = browser.find_element_by_id("identifierNext")


google_username_inp.send_keys(google_username)
time.sleep(2)
googlenext_btn_username.click()
time.sleep(2)

#gets input boxes and buttons for password
google_password_input = browser.find_element_by_name("password")
google_next_btn_password = browser.find_element_by_id('passwordNext')

google_password_input.send_keys(google_password)
time.sleep(2)
google_next_btn_password.click()
time.sleep(2)

browser.get('https://drive.google.com/drive/u/0/folders/1by0DliV7j4oHm_-RT0XA6IQ3SCRmkmPf')

# browser.quit()