#before using webdiver - install driver into you system
#from here :https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver

from selenium import webdriver                         

#if getting chrome version error
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())  

# else use this
# driver = webdriver.Chrome()                               

driver.get("https://youtube.com") #open the chrome with youtube

searchbox = driver.find_element_by_xpath('//*[@id="search"]')
searchbox.send_keys("about selenium")

searchbtn = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchbtn.click()