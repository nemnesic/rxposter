from os import abort
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import SUBS
import sys
import time


subreddit_list = SUBS.split(",")
subreddit_list = [SUBS.strip() for SUBS in subreddit_list]
if len(subreddit_list) < 1:
    print("SUBS is not configured in the config.py")
    sys.exit()

username = input("Enter reddit username: ")
password = input("Enter reddit password: ")
reddit_post = input("Enter reddit post that  you want to X-post: ")
reddit_post_id = reddit_post.split("/")[6]
print("Reddit post id: {}".format(reddit_post_id))

print("1. Login using username: {} and password: {}".format(username, password))
print(
    "2. Post {} will be cross-posted to the following subreddits: {}".format(
        reddit_post, subreddit_list
    )
)

continue_y_n = input("Continue [y/n]: ")
if continue_y_n != "y":
    sys.exit()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument('--headless')
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-setuid-sandbox")
chrome_options.add_argument("--ignore-certificate-errors")
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)


driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2F")
driver.find_element(By.ID, "loginUsername").send_keys(username)
password_input_field = driver.find_element(By.ID, "loginPassword")
password_input_field.send_keys(password)
password_input_field.send_keys(Keys.RETURN)

time.sleep(10)

for sub in subreddit_list:
    if sub != "":
        url_forxpost = (
            "https://www.reddit.com/r/" + sub + "/submit?source_id=t3_" + reddit_post_id
        )
        print(url_forxpost)
        driver.get(url_forxpost)
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Post')]"))
        ).click()
        time.sleep(7)
