from selenium import webdriver

def googleSearch(searchItem, browser) :

	browser.get('https://google.com/search?q='+searchItem)


if __name__=="__main__": 
    
  searchItem = input('Enter Search Item: ')

  chromedriverPath = './chromedriver.exe'
  browser = webdriver.Chrome(chromedriverPath)
  browser.maximize_window()

  googleSearch(searchItem, browser)