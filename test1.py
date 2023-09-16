import time
import json
from selenium import webdriver

class FacebookScraper:
    def __init__(self):
        self.driver = None

    def create_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument('--blink-settings=imagesEnabled=false')

        self.driver = webdriver.Chrome(options=chrome_options)

    def login_with_cookies(self, cookies):
        self.driver.get("https://www.facebook.com")
        for cookie in cookies:
            self.driver.add_cookie(cookie)

    def scroll_to_bottom(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def capture_network_requests(self):
        self.driver.get("https://www.facebook.com")
        time.sleep(5)  # Wait for the page to load

    def export_har_file(self, filename):
        har = self.driver.execute_cdp_cmd("Network.getAllInterceptedRequests", {})
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(har, file, indent=2)

    def run(self, cookies):
        try:
            self.create_driver()
            self.login_with_cookies(cookies)
            time.sleep(5)  # Wait for the page to load
            self.driver.get('https://www.facebook.com/profile.php?id=61550964032031&sk=followers')
            time.sleep(5)  # Wait for the followers page to load
            self.scroll_to_bottom()
            self.capture_network_requests()
            self.export_har_file('network_traffic.har')
            self.driver.quit()
            print("Success")  # Print "Success" when the task is completed
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    try:
        cookies = [
            {"name": "datr", "value": "o2kBZfAJDj3PI93UBZlWDcoJ", "domain": ".facebook.com", "path": "/",
             "secure": True, "httpOnly": True},
            {"name": "sb", "value": "o2kBZecPI7AgppvB2y-BFsQm", "domain": ".facebook.com", "path": "/", "secure": True,
             "httpOnly": True},
            {"name": "c_user", "value": "100094654806004", "domain": ".facebook.com", "path": "/", "secure": True,
             "httpOnly": True},
            {"name": "xs",
             "value": "38%3Ad7hehynSKNOklg%3A2%3A1694591417%3A-1%3A-1%3A%3AAcUjkD7Ost4cL3Tl7PQaZ3MJmBUDgTMXKW7QegKM2A",
             "domain": ".facebook.com", "path": "/", "secure": True, "httpOnly": True},
            {"name": "fr",
             "value": "0gKgyTQA7qcJvzlcM.AWVW7DC_27HV7JmA3kPLV-03VxY.BlA-zh.XU.AAA.0.0.BlA-zh.AWV1JOQAJXc",
             "domain": ".facebook.com", "path": "/", "secure": True, "httpOnly": True},
            {"name": "i_user", "value": "61550964032031", "domain": ".facebook.com", "path": "/", "secure": True,
             "httpOnly": True},
            {"name": "dpr", "value": "0.8955223880597015", "domain": ".facebook.com", "path": "/", "secure": True,
             "httpOnly": True},
            {"name": "wd", "value": "834x718", "domain": ".facebook.com", "path": "/", "secure": True, "httpOnly": True}
            # Add more cookies here if needed
        ]

        scraper = FacebookScraper()
        scraper.run(cookies)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
