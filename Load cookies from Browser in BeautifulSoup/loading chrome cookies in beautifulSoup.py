import requests
from bs4 import BeautifulSoup
import browser_cookie3
cj = browser_cookie3.load()
s = requests.Session()
for c in cj:
	s.cookies.set_cookie(c)