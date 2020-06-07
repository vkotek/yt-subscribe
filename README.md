# yt-subscribe
Autosubscribe to YouTube channels from exported subscriptions. This script allows you to automatically subscribe exported youtube subscriptions to another account.

# Installation 

- Install Python and create a virtualenv
- pip install -r requirements.txt
- Download chromedriver.exe and place it in the script's folder. Make sure it corresponds to your chrome version.

# How to use

- Go to https://youtube.com/subscription_manager
- At the bottom, export the RSS of subscriptions, place the file in the script's folder
- Open chrome and open the destination profile (it is recommended to use a separate profile)
- Login with the google account to which you want to transfer subscriptions
- Visit 'chrome://version' and check the 'Profile Path' value. Make sure it corresponds to the values in main.py line numbers 8, 9
- Close chrome (make sure it's not running minimized)


# Example

```
cd {project folder}

pip install virtualenv 

virtualenv venv

venv/Scripts/activate
source venv/bin/activate

pip install -r requirements.txt

python main.py
```