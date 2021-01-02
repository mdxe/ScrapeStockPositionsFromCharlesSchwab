import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path_to_json = "./credentials.json"
with open(path_to_json, "r") as handler:
        info = json.load(handler)

def main():
    username = info["user"]
    password = info["password"]

    login_url = 'https://client.schwab.com/Login/SignOn/CustomerCenterLogin.aspx'

    opts = Options()
    # opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
    driver = webdriver.Chrome('./chromedriver', options=opts)
    # driver = webdriver.Firefox(executable_path=r'./geckodriver/geckodriver', options=opts)
    driver.maximize_window()

    login(driver, username, password)
    getPositions(driver)
    driver.close()

def login(driver, username, password):
    login_url = 'https://client.schwab.com/Login/SignOn/CustomerCenterLogin.aspx'
    
    driver.get(login_url)
    
    WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"lmsSecondaryLogin")))
    username_textbox = driver.find_element_by_id('LoginId')
    username_textbox.send_keys(username)
    password_textbox = driver.find_element_by_id("Password")
    password_textbox.send_keys(password)
    password_textbox.send_keys("\n") # send enter to login
    #login_button = driver.find_element_by_id("LoginSubmitBtn")
    #login_button.submit()
    
    # If Log Out is an option, then we successfully logged in
    try:
        WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.CLASS_NAME,"logout")))
        logoutelement = driver.find_element_by_class_name("logout")
    except:
        driver.close()
        print("\nUnable to login...\n")
        return
    print("\nSuccessfully logged in...\n")

def getPositions(driver):
    driver.implicitly_wait(10)
    driver.find_element_by_partial_link_text("Positions").click()

    myStocks = driver.find_elements_by_class_name("data-row")
    print("Ticker", "QTY", "Cost Basis", "Share Price", sep=',')
    for row in myStocks:
        stockTicker = row.get_attribute("data-pulsr-symbol")
        if stockName is not None:
            stockQty       = row.get_attribute("data-pulsr-quantity")
            stockCostBasis = row.get_attribute("data-pulsr-cbdata")
            stockPrice     = row.find_element_by_css_selector('span.evt-tooltip[data-pulsr-field="TradePrice"]').text
            print(stockTicker, stockQty, "$"+stockCostBasis, stockPrice, sep=',')
    return

if __name__ == "__main__":
    main()