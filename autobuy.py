
import time
from datetime import datetime
from selenium import webdriver

LOGIN_ID = 'Email ID Daalo'
LOGIN_PASSWORD = 'Password Daalo'

ITEM_URL = 'URL do product ka'    

ACCEPT_SHOP = 'Amazon'
LIMIT_VALUE = 33500    # Max amount

def l(str):
    print("%s : %s"%(datetime.now().strftime("%Y/%m/%d %H:%M:%S"),str))

if __name__ == '__main__':

    # Launch Browser
    try:
        b = webdriver.Chrome('./chromedriver')
        b.get(ITEM_URL)
    except:
        l('Failed to open browser.')
        exit()

    while True:
        # Product Availibity Check
        while True:
            try:
                #Confirm Seller
                shop = b.find_element_by_id('merchant-info').text
                shop = shop.split('Is for sale')[0].split('This Product ')[1]

                if ACCEPT_SHOP not in shop:
                    raise Exception("not Amazon.")

                # Adding to cart
                b.find_element_by_id('add-to-cart-button').click()
                break
            except:
                time.sleep(60)
                b.refresh()

        
	
	
	
print (' Made with love by Ritika ')
