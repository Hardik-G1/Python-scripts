from selenium import webdriver
from time import sleep
import shutil
import re
options = webdriver.ChromeOptions();
options.add_argument('headless');
driver=webdriver.Chrome("C:/Users/ronni/Downloads/chromedriver_win32/chromedriver.exe",options=options)
driver.set_page_load_timeout(30000)
url='https://kissmanga.com/'
driver.get(url)
sleep(5)
u=driver.find_element_by_xpath("//*[@id='aRandomMangaResult']/img").get_attribute("src")
t=driver.find_element_by_xpath("//*[@id='divRandomManga']/div/a").text
print(u,t)


    

        
        
