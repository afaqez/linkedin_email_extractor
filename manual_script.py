import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# installing emailExtractor extension using crx3
chrome_options = Options()
chrome_options.add_extension('crx/email_extractor.crx')

# navigate to google
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com")

search_query = '"Retail" AND "Fashion" AND "Management Consulting" -intitle:"profiles" -inurl:"dir/ " email "@gmail.com" site:www.linkedin.com/in/ OR site:www.linkedin.com/pub/'
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys(search_query)
search_box.submit()

# scroll like a human
scroll_distance = 2000  # increase the value in order to get more emails
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
    time.sleep(2) 
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height >= last_height:
        break
    last_height = new_height



# access the popup page of email Extractor 
time.sleep(5)
driver.get('chrome-extension://jdianbbpnakhcmfkcckaboohfgnngfcc/popup.html')
time.sleep(5)

show_emails_div = driver.find_element(By.ID, "showEmails") # showEmails is the id of the <div> containing all the emails

emails_text = show_emails_div.text

emails = emails_text.split("\n")

for email in emails:
    print(email)

print('Emails Extracted')