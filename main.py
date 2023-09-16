import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import json

user_cards = []


class FacebookScraper:
    def __init__(self):
        chrome_options = Options()
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

    def scroll_to_bottom(self, scroll_amount=100000):
        global user_cards

        current_iter = 0
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        retry = 0
        while True:
            user_cards = self.scrape_user_cards()
            print(len(user_cards))
            print(f'Current iteration - {current_iter}')
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight + 1000);")
            time.sleep(2)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                print(f'trying again {retry}/10')
                retry += 1
                if retry >= 10:
                    break
                continue

            if scroll_amount < current_iter:
                break

            last_height = new_height
            current_iter += 1
            retry = 0

    def scrape_user_cards(self):
        # Get the page source using Selenium
        page_source = self.driver.page_source

        # Parse the page source with BeautifulSoup
        soup = BeautifulSoup(page_source, 'html.parser')

        # Find user card elements using bs4 (adjust the selector as needed)
        user_card_elements = soup.find_all('div',
                                           class_='x6s0dn4 x1lq5wgf xgqcy7u x30kzoy x9jhf4c x1olyfxc x9f619 x78zum5 x1e56ztr x1gefphp x1y1aw1k x1sxyh0 xwib8y2 xurb0ha')

        new_elements = []
        for element in user_card_elements:
            new_el = {}
            # Extract the username and bio from the user card element
            username_bio_text = element.text.split('\n')
            new_el['Username'] = username_bio_text[0] if len(username_bio_text) > 0 else 'n/a'
            new_el['Bio'] = username_bio_text[1] if len(username_bio_text) > 1 else 'n/a'

            new_el['Link to Profile'] = element.find('a', href=True)['href']
            new_el['Image'] = element.find('img', src=True)['src']
            new_elements.append(new_el)

        return new_elements

    def export_to_csv(self, data):
        with open('facebook_users.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Image', 'Username', 'Bio', 'Link to Profile']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for user in data:
                writer.writerow(user)

    def run(self, cookies):
        self.login_with_cookies(cookies)
        time.sleep(5)  # Wait for the page to load
        self.driver.get('https://www.facebook.com/profile.php?id=61550964032031&sk=followers')
        time.sleep(5)
        self.scroll_to_bottom()
        user_data = self.scrape_user_cards()
        self.export_to_csv(user_data)
        self.driver.quit()


if __name__ == "__main__":
    # Setup Cookies
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

    except:
        with open('inspect.json', 'w') as f:
            json.dump(user_cards, open('test.json', 'a+'), indent=4)
