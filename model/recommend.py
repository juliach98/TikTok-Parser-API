class Recommend:
    def __init__(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.chrome.options import Options

        url = "https://www.tiktok.com/en"

        chrome_options = Options()
        chrome_options.headless = True

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)

        self.accounts = ['https://www.tiktok.com/@' + element.text
               for element in driver.find_elements(By.XPATH, "//h3[@data-e2e='video-author-uniqueid']")]

    def to_json(self):
        import json

        return json.dumps(self, default=lambda o: o.__dict__)

r = Recommend()

r
r