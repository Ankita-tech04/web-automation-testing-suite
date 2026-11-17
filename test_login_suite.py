"""
Automated UI Test Suite for Web Application Authentication
Author: Ankita Das
Framework: Selenium WebDriver + Pytest
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


class TestAuthenticationSuite:
    
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        """Setup headless Chrome browser before each test and teardown after."""
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Runs in background
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--window-size=1920,1080")
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.base_url = "https://the-internet.herokuapp.com/login"
        self.wait = WebDriverWait(self.driver, 10)
        
        yield
        self.driver.quit()

    def test_tc01_successful_login(self):
        """TC-01: Verify user can successfully log in with valid credentials."""
        self.driver.get(self.base_url)
        
        # Enter valid credentials
        self.driver.find_element(By.ID, "username").send_keys("tomsmith")
        self.driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        
        # Verify success banner is displayed
        flash_message = self.wait.until(
            EC.visibility_of_element_located((By.ID, "flash"))
        ).text
        assert "You logged into a secure area!" in flash_message
        print("TC-01 Passed: Successful login verified.")

    def test_tc02_invalid_password(self):
        """TC-02: Verify error message is displayed when entering invalid password."""
        self.driver.get(self.base_url)
        
        # Enter valid username but incorrect password
        self.driver.find_element(By.ID, "username").send_keys("tomsmith")
        self.driver.find_element(By.ID, "password").send_keys("WrongPassword123")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        
        # Verify error alert
        flash_message = self.wait.until(
            EC.visibility_of_element_located((By.ID, "flash"))
        ).text
        assert "Your password is invalid!" in flash_message
        print("TC-02 Passed: Invalid password error handled correctly.")

    def test_tc03_invalid_username(self):
        """TC-03: Verify error message is displayed when entering non-existent username."""
        self.driver.get(self.base_url)
        
        self.driver.find_element(By.ID, "username").send_keys("invalid_user_99")
        self.driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        
        flash_message = self.wait.until(
            EC.visibility_of_element_located((By.ID, "flash"))
        ).text
        assert "Your username is invalid!" in flash_message
        print("TC-03 Passed: Non-existent username error handled correctly.")

    def test_tc04_empty_fields_validation(self):
        """TC-04: Verify behavior when submitting blank username and password."""
        self.driver.get(self.base_url)
        
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        
        flash_message = self.wait.until(
            EC.visibility_of_element_located((By.ID, "flash"))
        ).text
        assert "Your username is invalid!" in flash_message
        print("TC-04 Passed: Empty fields validation passed.")
