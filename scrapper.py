from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from .utils import make_driver_options




def fetch_page_html(url, wait_time=2, driver=None):
"""Return fully rendered HTML of a page using Selenium."""
own_driver = False
if driver is None:
opts = make_driver_options()
driver = webdriver.Chrome(options=opts)
own_driver = True


try:
driver.get(url)
# simple wait — for production replace with explicit waits
time.sleep(wait_time)
return driver.page_source
finally:
if own_driver:
driver.quit()




def scrape_example(url, driver=None):
html = fetch_page_html(url, driver=driver)
soup = BeautifulSoup(html, 'html.parser')


# example extraction (change to suit target site)
title = soup.title.string.strip() if soup.title else ''
content_el = soup.find('div', {'class': 'main-content'})
content = content_el.get_text(separator=' ', strip=True) if content_el else ''


return {
'url': url,
'title': title,
'content': content,
}