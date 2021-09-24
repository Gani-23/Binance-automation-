import selenium 
from selenium import webdriver as wd 
import time
import mouse

opt = wd.ChromeOptions()
opt.add_argument("--disable-infobars")
opt.add_argument(" --disable-notifications")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_argument("--start-maximized")
opt.add_argument("no-sandbox")
opt.add_argument("--disable-gpu")
opt.add_argument("--disable-dev-shm-usage")
opt.add_argument("--disable-xss-auditor")
opt.add_argument("--disable-web-security")
opt.add_argument("--allow-running-insecure-content")
opt.add_argument("--disable-setuid-sandbox")
opt.add_argument("--disable-webgl")
opt.add_argument("--disable-popup-blocking")




driver = wd.Chrome(chrome_options=opt)

driver.get('https://www.binance.com')



#Login
time.sleep(2.5)
print("ENTER YOUR CHOICE :")
print("MAIN_MENU \n1.Login \n2.REGISTER BY MAIL \n3.REGISTER BY PHONE NUMBER")
b = int(input())
if(b==1):
    email = input('Enter your mail : ')
    password = input("Enter your password :")
    driver.find_element_by_xpath("//a[normalize-space()='Log In']").click()
    time.sleep(5)
    mails = driver.find_element_by_xpath("//input[@name='email']")
    mails.send_keys(email)
    passs = driver.find_element_by_xpath("//input[@name='password']")
    passs.send_keys(password)
    time.sleep(2)
    driver.find_element_by_xpath("//button[normalize-space()='Log In']").click()
    print("PLEASE FILL CAPTCHA AS SOON AS POSSIBLE")
    time.sleep(35)
    driver.find_element_by_xpath("//div[@class='css-1mme6xj']").click()
    Vkey = int(input("Enter Your OTP"))
    verification = driver.find_element_by_xpath("//input[@aria-label='Phone verification code']")
    driver.send_keys(Vkey)
    EV = driver.find_element_by_xpath('//*[@id="__APP"]/div/main/div/div/div/div/div[3]/div[1]/div')
    EV.press()
    try:
        eVer = int(input())
        ER = driver.find_element_by_xpath('//*[@id="__APP"]/div/main/div/div/div/div/div[3]/div[1]/div/input')
        ER.send_keys(eVer)
        time.sleep(2.5)
    finally:
        driver.find_element_by_xpath('//*[@id="__APP"]/div/main/div/div/div/div/div[5]/button')
#REGISTRATION
elif(b==2):
    Login = input('Enter Your mail')
    keyz = input('Enter Your password')
    driver.find_element_by_xpath("//a[normalize-space()='Register']").click()

    mail = driver.find_element_by_xpath('//*[@id="__APP"]/div/main/div/div/div/div/div[3]/form/div/div[1]/div[2]/div/input')
    mail.send_keys(Login)
    time.sleep(1.5)
    password = driver.find_element_by_xpath("//input[@name='password']")
    password.send_keys(keyz)
    driver.find_element_by_xpath("//button[normalize-space()='Create Account']").click()
    print('CHECK MAIL')
    time.sleep(50)

    

else:
    driver.find_element_by_xpath("//a[normalize-space()='Register']").click()
    phone = int(input('Enter Mobile Number'))
    keyzz = input("Enter Password")

    pnum = driver.find_element_by_xpath("//input[@name='mobile']")
    pnum.send_keys(phone)
    keyzzz = driver.find_element_by_xpath("//input[@name='password']")
    keyzzz.send_keys(keyzzz)
    driver.find_element_by_xpath("//button[normalize-space()='Create Account']").click()
    time.sleep(120)
    print("Do the process")

