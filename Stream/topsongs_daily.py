from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import shutil
import glob
import os

# instantiate a chrome options object so you can set the size and headless preference
# some of these chrome options might be uncessary but I just used a boilerplate
chrome_options = Options()

# initialize driver object and change the <path_to_chrome_driver> depending on your directory where your chromedriver should be
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:/Users/TheSandyOne/Desktop/Diddly/Python/LoR/chromedriver.exe")
print("Headless Chrome Initialized")
driver.get('https://spotifycharts.com/regional/global/daily/latest')

set1 = driver.find_element_by_link_text('DOWNLOAD TO CSV')
set1.click()

time.sleep(5)
driver.quit()

print("Moving Data to Destination")
os.chdir(r"C:\Users\TheSandyOne\Downloads")
destination_folder = "C:/Users/TheSandyOne/Desktop/Diddly/Python/Stream/Data"
for file in glob.glob("*.csv"):
    shutil.move(file, destination_folder)
print("Finished Moving Data")