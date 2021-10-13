import time
import webbrowser

from selenium import webdriver
import requests

url = 'http://ecquery.y0k.cn/#/login'
data = requests.get(url)
print(data)

driver = webdriver.Chrome()
webdriver.Chrome().maximize_window()

driver.get("http://ecquery.y0k.cn/#/login")
print(driver.title)



driver.find_element_by_xpath("/html/body/div[1]/div/form/div/div[2]/div/div/input").send_keys("hl001")
time.sleep(1)

driver.find_element_by_xpath("/html/body/div/div/form/div/div[3]/div/div/input").send_keys("@@mima0077")
time.sleep(1)
# driver.find_element_by_class_name("imgEye").click()
# time.sleep(1)
driver.find_element_by_xpath("/html/body/div/div/form/div/div[4]/div/div/div[1]/input").send_keys("896931")
driver.find_element_by_xpath("/html/body/div/div/form/div/button").click()
driver.quit()




# time.sleep(3)
# driver.close()