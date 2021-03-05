import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def location(filePath):
	searchUrl = 'http://www.google.hr/searchbyimage/upload'
	multipart = {'encoded_image': (filePath, open(filePath, 'rb'))}
	response = requests.post(searchUrl, files=multipart, allow_redirects=False)
	fetchUrl = response.headers['Location']


	chrome_options = Options()  
	chrome_options.add_argument("--headless")      
	driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
	driver.get(fetchUrl)
	source = driver.page_source
	driver.quit()

	result = source.find('h" value="')
	ans = ""
	i = result + 10
	while True:
		if source[i] == '"':
			break
		ans += source[i]
		i += 1
	return ans 