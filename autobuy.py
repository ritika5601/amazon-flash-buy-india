
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
		
	# Purchase Begins
        b.get('https://www.amazon.in/gp/cart/view.html?ref_=nav_cart')
        b.find_element_by_name('proceedToCheckout').click()

        # Login Starts
        try:
            b.find_element_by_id('ap_email').send_keys(LOGIN_ID)
            b.find_element_by_id('ap_password').send_keys(LOGIN_PASSWORD)
            b.find_element_by_id('signInSubmit').click()
        except:
            l('LOGIN PASS.')
            pass

        # Price Check
        p = b.find_element_by_css_selector('td.grand-total-price').text
        if int(p.split(' ')[1].replace(',', '')) > LIMIT_VALUE:
            l('PLICE IS TOO LARGE.')
            continue

        # Order Confirmation
        b.find_element_by_name('placeYourOrder1').click()
        break

    l('ALL DONE.')


print (' Made with love by Ritika ')
