# tests/automated_login_test.py
# Author: Johnpaul
# Description: AI-Enhanced Automated Login Test using Selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Launch Chrome
driver = webdriver.Chrome()

# Load local login page
file_path = os.path.abspath("../app/index.html")
driver.get(f"file:///{file_path}")
driver.maximize_window()

# ---------- Test Case 1: Valid Login ----------
driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("12345")
driver.find_element(By.ID, "loginButton").click()
time.sleep(2)
message = driver.find_element(By.ID, "message").text
assert "successful" in message
print("✅ Test Case 1 Passed: Valid credentials accepted.")

# ---------- Test Case 2: Invalid Login ----------
driver.find_element(By.ID, "username").clear()
driver.find_element(By.ID, "password").clear()
driver.find_element(By.ID, "username").send_keys("fakeuser")
driver.find_element(By.ID, "password").send_keys("wrongpass")
driver.find_element(By.ID, "loginButton").click()
time.sleep(2)
message = driver.find_element(By.ID, "message").text
assert "Invalid" in message
print("❌ Test Case 2 Passed: Invalid credentials rejected.")

# Save test evidence
if not os.path.exists("../results"):
    os.makedirs("../results")

driver.save_screenshot("../results/login_test_results.png")

driver.quit()
print("📸 Screenshot saved and browser closed successfully.")
