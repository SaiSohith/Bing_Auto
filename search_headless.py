from selenium import webdriver
from time import sleep

if __name__=='__main__':
    
    edgeBrowser = webdriver.Edge(r"msedgedriver.exe")
    Dimension d = new Dimension(300,1080);
    #Resize current window to the set dimension
    driver.manage().window().setSize(d);
    edgeBrowser.get('https://www.facebook.com/')
    
    edgeBrowser.get('https://www.amazon.com/')
    