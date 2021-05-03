from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def send_proton_email(email_to, email_subject, email_message, username, password):
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = ''
    try:
        driver = webdriver.Firefox(options=options)
        driver.get('https://mail.protonmail.com/login')
        sleep(1)
        
        print("Logging in...")
        driver.find_element_by_id('username').send_keys(username)
        driver.find_element_by_id('password').send_keys(password)
        sleep(1)
        driver.find_element_by_id('login_btn').click()
        print('Logged in :)')
        sleep(5)
        driver.find_element_by_class_name('sidebar-btn-compose').click()
        sleep(1)

        # normally you should end up straight in the recepient field
        driver.switch_to.active_element.send_keys(email_to + Keys.TAB)
        sleep(1)

        # switch to subject field
        driver.switch_to.active_element.send_keys(Keys.TAB)
        sleep(1)
        #driver.find_element_by_class_name('composer-field-Subject').click()
        driver.switch_to.active_element.send_keys(email_subject)
        sleep(1)

        # compose email
        driver.switch_to.active_element.send_keys(Keys.TAB)
        sleep(1)
        driver.switch_to.active_element.send_keys(email_message)
        sleep(1)
        driver.find_element_by_class_name('composer-btn-send').click()  
        sleep(5)
        driver.quit()
        print('E-mail Sent!')
        del email_subject
        del email_message
        del driver
    except Exception as err:
        driver.quit()
        print('\nError Occurred while sending e-mail!!')
        status = (str(err), 'Error Origin: Proton Mail Script')
        print(status)
        del err
        del status
        del driver

recepient = ''
subject = ''
msg = ''
username = ''
password = ''

send_proton_email(recepient, subject, msg, username, password)