from selenium.webdriver.chrome.options import Options




def make_driver_options(headless=True):
opts = Options()
if headless:
opts.add_argument('--headless=new')
opts.add_argument('--no-sandbox')
opts.add_argument('--disable-dev-shm-usage')
opts.add_argument('--disable-gpu')
# add common headers via experimental options if needed
opts.add_argument("--window-size=1920,1080")
return opts
