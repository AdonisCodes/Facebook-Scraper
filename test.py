from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scroll import Scroll
import time


chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("start-maximized")
# chrome_options.add_argument("--user-data-dir=selenium") #Saves browser history
# chrome_options.add_experimental_option("prefs",{"download.default_directory" : "/home/runner/{REPL_NAME}"}) #Download Directory

# Setup Selenium Driver
driver = webdriver.Chrome(options=chrome_options)

# Open Facebook website
driver.get("https://www.facebook.com")

# Setup Cookies
cookies = [
    {"name": "datr", "value": "o2kBZfAJDj3PI93UBZlWDcoJ", "domain": ".facebook.com", "path": "/", "secure": True, "httpOnly": True},
    {"name": "sb", "value": "o2kBZecPI7AgppvB2y-BFsQm", "domain": ".facebook.com", "path": "/", "secure": True, "httpOnly": True},
    {"name": "c_user", "value": "100094654806004", "domain": ".facebook.com", "path": "/", "secure": True, "httpOnly": True},
    {"name": "xs", "value": "38%3Ad7hehynSKNOklg%3A2%3A1694591417%3A-1%3A-1%3A%3AAcUjkD7Ost4cL3Tl7PQaZ3MJmBUDgTMXKW7QegKM2A", "domain": ".facebook.com", "path": "/", "secure": True, "httpOnly": True},
    {"name": "fr", "value": "0gKgyTQA7qcJvzlcM.AWVW7DC_27HV7JmA3kPLV-03VxY.BlA-zh.XU.AAA.0.0.BlA-zh.AWV1JOQAJXc", "domain": ".facebook.com", "path": "/", "secure": True, "httpOnly": True},
    {"name": "i_user", "value": "61550964032031", "domain": ".facebook.com", "path": "/", "secure": True, "httpOnly": True},
    {"name": "dpr", "value": "0.8955223880597015", "domain": ".facebook.com", "path": "/", "secure": True, "httpOnly": True},
    {"name": "wd", "value": "834x718", "domain": ".facebook.com", "path": "/", "secure": True, "httpOnly": True}
]
for cookie in cookies:
    driver.add_cookie(cookie)
  
# Create infinite scroller until the bottom of the page
time.sleep(5)
Scroll().run(driver)

# Scrape all the user cards ( Image, username, bio & link to profile )

# Parse each into an object
# Write each object to an array
# Export objects to json format ( For transformer reasons )
# Write this entire list to a csv file