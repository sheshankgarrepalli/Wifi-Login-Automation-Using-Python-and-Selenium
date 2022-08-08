from selenium import webdriver
import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
def startBot(username, password, url):
	path = r" " #please give the chromedriver location path
	
	# giving the path of chromedriver to selenium webdriver
	options=Options()
	options = webdriver.ChromeOptions()
	options.add_experimental_option('excludeSwitches', ['enable-logging'])
	
	driver = webdriver.Chrome(executable_path = path)

	#driver = webdriver.Chrome(path)
	
	
	# opening the website in chrome.
	driver.get(url)
	
	# find the id or name or class of
	# username by inspecting on username input
	driver.find_element_by_name(
        "username").send_keys(username)
	driver.find_element_by_name(
        "password").send_keys(password)
	#driver.find_element(By.XPATH, "username").send_keys(username)
	#driver.find_element(
	#	"identifierId/whsOnd zHQkBf/Email or phone").send_keys(username)
	
	# find the password by inspecting on password input
	#driver.find_element(By.XPATH, "password"
	#	).send_keys(password)
	
	# click on submit
	driver.find_element_by_id(
		"loginbtn").click()


# Driver Code
# Enter below your login credentials
username = "" #please enter the username of your wifi - ISP username
password = "" #please enter the username of your wifi - ISP password

# URL of the login page of site
# which you want to automate login.
url = " "

# Call the function
startBot(username, password, url)
