from selenium import webdriver
from time import sleep 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date

class Test_Homework:
    
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True) 

    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self,locator):
        WebDriverWait(self.driver,10).until(ec.visibility_of_element_located(locator))

    @pytest.mark.parametrize("username,password",[("77","88"), ("kullanici","sifre"), ("asdf","12345")])
    def test_empty_login(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID, "password")      
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-empty-login-{username}-{password}.png")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
    
    def test_empty_password(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")  
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID, "password")      
        usernameInput.send_keys("a")
        passwordInput.send_keys("")
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-empty-password-'a'.png")
        assert errorMessage.text == "Epic sadface: Password is required"

    def test_invalid_login(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")  
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID, "password")   
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-'locked_out_user'-'secret_sauce'.png")
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."

    def test_product_numbers(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")  
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID, "password") 
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        self.driver.get("https://www.saucedemo.com/inventory.html")     
        numberProducts = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        self.driver.save_screenshot(f"{self.folderPath}/test-products-numbers.png")
        assert len(numberProducts) == 6

    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce"),("problem_user","secret_sauce"),
    ("performance_glitch_user","secret_sauce")])    
    def test_login(self,username,password):
        usernameInput = self.driver.find_element(By.ID,"user-name")
        usernameInput.send_keys(username)
        passwordInput = self.driver.find_element(By.ID,"password")
        passwordInput.send_keys(password)
        self.driver.find_element(By.ID,"login-button").click() 
        self.driver.save_screenshot(f"{self.folderPath}/test-login.png")
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html"

    def test_error_icon(self):       
        loginBtn = self.driver.find_element(By.ID, "login-button")     
        loginBtn.click()      
        errorCloseIcon = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")   
        self.driver.save_screenshot(f"{self.folderPath}/test-error-icon.png") 
        errorCloseIcon.click()


    def test_add_cart(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")  
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID, "password") 
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        self.driver.get("https://www.saucedemo.com/inventory.html")
        self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
        self.driver.save_screenshot(f"{self.folderPath}/test-add-cart.png")
    
    def test_remove(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")  
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID, "password") 
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        self.driver.get("https://www.saucedemo.com/inventory.html")
        self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.ID,"remove-sauce-labs-backpack").click()
        self.driver.save_screenshot(f"{self.folderPath}/test-remove.png")




