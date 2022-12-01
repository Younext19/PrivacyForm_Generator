from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver import FirefoxOptions

import random
app_name_info="APP_NAME"
contact_info="MAIL"
id_info="nothing" #Fixed
app_type_info="Free" #Fixed
os_info="Android" # Fixed
owner_type_info="Individual" #Fixed
developer_name_info="Developer NAME"
def generate_privacy_policy(app_name_info,contact_info,id_info,app_type_info,os_info,owner_type_info,developer_name_info):
    
    browser = webdriver.Firefox()
    browser.get('https://app-privacy-policy-generator.firebaseapp.com/')
    app_name_input = '//*[@id="step-1"]/div/div[2]/div/input'
    contact_info_input = '//*[@id="step-1"]/div/div[2]/div[2]/input'
    id_info_input = '//*[@id="step-1"]/div/div[2]/div[3]/input'
    app_type_input = '//*[@id="step-1"]/div/div[2]/div[4]/div/select'
    mobile_os_input = '//*[@id="step-1"]/div/div[2]/div[5]/div/select'
    owner_type_input = '//*[@id="step-1"]/div/div[2]/div[7]/div/select'
    developer_name_input = '//*[@id="step-1"]/div/div[2]/div[8]/input'
    next_button='//*[@id="step-1"]/div/div[1]/img[2]'
    select_admob_step2='//*[@id="step-2"]/div/div[2]/a[2]/label'
    next_button2='//*[@id="step-2"]/div/div/div/img[2]'
    privacy_policy_button='//*[@id="step-3"]/div/div[2]/div[2]/a[1]'
    deploy_button='//*[@id="app"]/div/div/div[2]/footer/div/button'

    deploy_email_input='//body/div[2]/div[2]/div/div/div[2]/div/div/div/input'
    deploy_password_input='//body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/input'
    deploy_cricket_button='//body/div[2]/div[2]/div/div/div[2]/div/button'
    deploy_link='//body/div[3]/div/div/div[3]/div/div/div/div[2]/div[2]/div/small/a[2]'


    # print(app_name_input)
    # browser.find_element_by_xpath(app_name_input).click()
    assert "App Privacy Policy Generator" in browser.title

    first_input=browser.find_element(By.XPATH, app_name_input)
    first_input.send_keys(app_name_info)

    second_input=browser.find_element(By.XPATH, contact_info_input)
    second_input.send_keys(contact_info)

    third_input=browser.find_element(By.XPATH, id_info_input)
    third_input.send_keys(id_info)

    fourth_input=browser.find_element(By.XPATH, app_type_input)
    drop=Select(fourth_input)
    drop.select_by_visible_text(app_type_info)

    fifth_input=browser.find_element(By.XPATH, mobile_os_input)
    drop=Select(fifth_input)
    drop.select_by_visible_text(os_info)

    sixth_input=browser.find_element(By.XPATH, owner_type_input)
    drop=Select(sixth_input)
    drop.select_by_visible_text(owner_type_info)

    seventh_input=browser.find_element(By.XPATH, developer_name_input)
    seventh_input.send_keys(developer_name_info)

    time.sleep(4)
    eight_button=browser.find_element(By.XPATH, next_button)
    eight_button.click()
    time.sleep(4)

    ninth_button=browser.find_element(By.XPATH, select_admob_step2)
    ninth_button.click()

    time.sleep(4)

    tenth_button=browser.find_element(By.XPATH, next_button2)
    tenth_button.click()

    time.sleep(4)

    eleventh_button=browser.find_element(By.XPATH, privacy_policy_button)
    eleventh_button.click()

    time.sleep(4)


    twelvth_button=browser.find_element(By.XPATH, deploy_button)
    twelvth_button.click()

    time.sleep(4)

    #Generate Random Email
    letters = ["a", "b","c", "d","e", "f","g", "h","i", "j","k", "l","m", "n","o", "p","q", "r","s", "t","u", "v","w", "x","y", "z"]
    all=["a", "b","c", "d","e", "f","g", "h","i", "j","k", "l","m", "n","o", "p","q", "r","s", "t","u", "v","w", "x","y", "z","1","2","3","4",".","5","_"]
    email = ''
    for _ in range(2):
        letter = random.sample(letters,1)[0]
        email += letter
    for _ in range(5):
        al = random.sample(letters,1)[0]
        email += al
    for _ in range(2):
        letter = random.sample(letters,1)[0]
        email += letter

    email += '@gmail.com'

    time.sleep(20)

    # Focus on deply page
    browser.switch_to.window(browser.window_handles[-1])
    time.sleep(5)

    # Write email on input

    thirteeth=browser.find_element(By.XPATH, deploy_email_input)
    thirteeth.send_keys(email)

    time.sleep(5)

    # Write password
    fourteeth=browser.find_element(By.XPATH, deploy_password_input)
    fourteeth.send_keys("anyPasswordBro10+")

    time.sleep(5)

    # recap verify
    browser.switch_to.frame(browser.find_element(By.TAG_NAME, 'iframe'))
    fifteeth=browser.find_element(By.XPATH, '//body/div[2]/div[3]/div/div/div/span')
    fifteeth.click()

    time.sleep(5)

    # Focus flycricker deployement done
    browser.switch_to.window(browser.window_handles[-1])
    sixteeth=browser.find_element(By.XPATH, deploy_cricket_button)
    sixteeth.click()

    time.sleep(20)

    # Copy text of privacy policy
    browser.switch_to.window(browser.window_handles[-1])
    seventeeth=browser.find_element(By.XPATH, deploy_link).get_attribute('href')
    browser.close()
    browser.quit()
    return seventeeth

# ______________________ Call Generate Privacy Policy Function ________________
privacy_result_link=generate_privacy_policy(app_name_info,contact_info,id_info,app_type_info,os_info,owner_type_info,developer_name_info)
print(privacy_result_link)


