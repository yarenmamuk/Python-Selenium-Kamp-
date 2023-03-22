from selenium import webdriver
from time import sleep 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class TestSauce:

    def test_empty_login(self):

        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5) 
        
        usernameInput = driver.find_element(By.ID, "user-name")  
        passwordInput = driver.find_element(By.ID, "password")      
        sleep(2)
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"TEST SONUCU: {testResult}")


    def test_empty_password(self):

        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5) 
        
        usernameInput = driver.find_element(By.ID, "user-name")  
        passwordInput = driver.find_element(By.ID, "password")      
        sleep(2)
        usernameInput.send_keys("a")
        passwordInput.send_keys("")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"TEST SONUCU: {testResult}")


    def test_invalid_login(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5) 
        usernameInput = driver.find_element(By.ID, "user-name")  
        passwordInput = driver.find_element(By.ID, "password")      
        sleep(2)
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"TEST SONUCU: {testResult}")
    

    def test_red_button(self):

        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2) 
        
        usernameInput = driver.find_element(By.ID, "user-name")  
        passwordInput = driver.find_element(By.ID, "password")      
        sleep(2)
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        red_button = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3/button/svg/path")
        red_button.click()
        sleep(5)


    def test_product_numbers(self):

        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5) 
        
        usernameInput = driver.find_element(By.ID, "user-name")  
        passwordInput = driver.find_element(By.ID, "password")      
        sleep(2)
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        driver.get("https://www.saucedemo.com/inventory.html")
        
        numberProducts = driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(f"Kullanıcıya gösterilen üyün sayısı: {len(numberProducts)}")


testClass = TestSauce()
# testClass.test_empty_login()
# testClass.test_empty_password()
# testClass.test_invalid_login()
# testClass.test_red_button()
testClass.test_product_numbers()
while True:
     continue
    