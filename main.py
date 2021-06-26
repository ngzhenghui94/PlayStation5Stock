from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from time import sleep
import datetime

#Chrome Driver Options, Headless prevents the actual browser from being launched.
options = Options()
options.headless = True
#Infinite 60sec loop
while(True):
    current = datetime.datetime.now()
    print("Running @ " + str(current.day) + "/"+ str(current.month) + " " + str(current.hour) + ":" + str(current.minute))
    driver = webdriver.Chrome('/Users/danielninetyfour/Downloads/chromedriver', options=options)
    driver.get("https://store.sony.com.sg/collections/playstation-consoles/products/playstation%C2%AE5-and-dualsense%E2%84%A25-wireless-controller-black")
    #Print the HTML's title
    print(driver.title)
    #Check if page is correct.
    assert "PlayStation®5" in driver.title
    #Getting the btn element via xPath
    elem = driver.find_element_by_xpath('//*[@id="product_form_6834194186395"]/div[3]/button')
    #Or can get the btn element via class
    # elem = driver.find_element_by_class_name('product__add-to-cart.button.button--primary')
    #Check Btn is disabled
    checkDisabled = elem.get_property('disabled')
    if checkDisabled == True:
        print("Out of Stock")
    elif checkDisabled == False:
        print("In Stock")
    driver.close()
    print("Sleeping @ {}/{} {}:{}".format(current.day, current.month, current.hour, current.minute))
    sleep(60)
