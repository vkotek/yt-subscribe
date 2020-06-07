import re, time
from selenium.webdriver import Chrome, ChromeOptions

## Get your chromedriver at https://sites.google.com/a/chromium.org/chromedriver/

subs_file = "subscription_manager.xml"

chrome_profile = "Profile 1" # Set your profile that you want to use, visit "chrome://version" and check Profile Path
chrome_user_data_dir = r'C:\Users\kotek\AppData\Local\Google\Chrome\User Data' # check "chrome://version"

subscribe_url = "https://youtube.com/channel/{channel_id}?sub_confirmation=1"

# Read the subscriptions
with open(subs_file, 'r') as f:
    channel_ids = re.findall("channel_id=([A-z, 0-9,-]*)", f.read())

# Chrome setup
options = ChromeOptions()
options.add_argument(f'--user-data-dir={chrome_user_data_dir}')
options.add_argument(f'--profile-directory={chrome_profile}')

# Luanch chrome
chromedriver = f'./chromedriver.exe'
driver = Chrome(chromedriver, options=options)

# Confirm user is logged in
def login():
    driver.get("https://accounts.google.com/")
    time.sleep(2)
    if input("Confiurm you are logged into Chrome and into the correct account (Y/n)").lower() != 'y':
        login()

login()

# Iterate through youtube channels and log in
for channel_id in channel_ids:
    channel_url = subscribe_url.format(channel_id=channel_id)

    try:
        driver.get(channel_url)
        time.sleep(1)

        confirm_button = driver.find_element_by_id("confirm-button")
        confirm_button.click()

    except Exception as e:
        time.sleep(0.5)
        print("Error subscribing to ", channel_url)
        # print(str(e))

driver.quit()
