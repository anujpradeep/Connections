from selenium import webdriver
from time import sleep
from pynput.keyboard import Key, Controller
#from se import pw

keyboard = Controller()

class Follow:
	def __init__(self, username, pw):
		self.driver = webdriver.Chrome()
		self.username = username
		self.driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
		sleep(2)
		#self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]")\
		#	.click()
		sleep(2)
		self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
			.send_keys(username)
		self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
			.send_keys(pw)
		# self.driver.find_element_by_xpath('//button[@type="submit"]')\
		# 	.click()
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
		sleep(4)
		#sleep(10) #need to use to open the with serc. code
		self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
			.click()
		sleep(2)
	def followuser(self,username2):
		self.driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys(username2)
		delay(2)
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
		# keyboard.press(Key.enter)
		# keyboard.release(Key.enter)

		
#class Follow:

#pw = 'y6bs^Vm^RKT$tD?'
pw = 'thisisatest'
username = 'anujpradeep'
my_bot = Follow('test.aaccc', pw)
my_bot.followuser(username)
