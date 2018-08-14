from selenium import webdriver
em=input('email or mobile number')
pa=input('password')
browser=webdriver.Chrome('C:/Users/lenovo/Downloads/chromedriver_win32/chromedriver.exe')
type(browser)
browser.get('https://www.facebook.com/')
browser.find_element_by_id('email').send_keys(em)
browser.find_element_by_id('pass').send_keys(pa)
browser.find_element_by_id('loginbutton').click()