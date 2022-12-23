class Video:
    def __init__(self, preview, ref, watched_count):
        self.preview = preview
        self.ref = ref
        self.watched_count = watched_count


class UserPage:
    def __init__(self, account='dream_team_house'):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.chrome.options import Options

        url = "https://www.tiktok.com/@" + account

        chrome_options = Options()
        chrome_options.headless = True

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)

        self.title = driver.find_element(By.XPATH, "//h2[@data-e2e='user-title']").text
        self.subtitle = driver.find_element(By.XPATH, "//h1[@data-e2e='user-subtitle']").text
        self.followers = driver.find_element(By.XPATH, "//strong[@data-e2e='followers-count']").text
        self.following = driver.find_element(By.XPATH, "//strong[@data-e2e='following-count']").text
        self.likes = driver.find_element(By.XPATH, "//strong[@data-e2e='likes-count']").text
        self.bio = driver.find_element(By.XPATH, "//h2[@data-e2e='user-bio']").text

        self.avatar = driver.find_element(By.XPATH, "//div[@data-e2e='user-avatar']/following::img").get_attribute("src")

        preview = [element.get_attribute("src")
                for element in driver.find_elements(By.XPATH, "//div[@data-e2e='user-post-item']/div/div/a/div/div/img")]
        ref = [element.get_attribute("href")
                for element in driver.find_elements(By.XPATH, "//div[@data-e2e='user-post-item']/div/div/a")]
        watched_count = [element.get_attribute("textContent")
                for element in driver.find_elements(By.XPATH, "//div[@data-e2e='user-post-item']/div/div/a/div/div/strong[@data-e2e='video-views']")]

        self.videos = []

        for i in range(len(preview)):
            self.videos.append(Video(preview[i], ref[i], watched_count[i]))

    def to_json(self):
        import json

        return json.dumps(self, default=lambda o: o.__dict__)
