from selenium import webdriver
from selenium.webdriver.common.by import By
import time

TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""
PROMISED_UP = 10
PROMISED_DOWN = 150


class InternetSpeedTwitterBot:
	def __init__(self):
		self.up = 0
		self.down = 0
		self.driver = webdriver.Chrome()
		self.email = TWITTER_EMAIL
		self.password = TWITTER_PASSWORD

	def get_internet_speed(self):
		self.driver.get("https://www.speedtest.net/")
		self.driver.maximize_window()

		time.sleep(5)
		go_button = self.driver.find_element(By.XPATH,
											 '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
		go_button.click()

		time.sleep(50)

		close = self.driver.find_element(By.XPATH,
										 '// *[ @ id = "container"] / div / div[3] / div / div / div / div[2] / div[3] '
										 '/ div[3] / div / div[8] / div / div / div[2] / a')
		close.click()

		self.up = self.driver.find_element(By.XPATH,
										   '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div['
										   '3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
		self.down = self.driver.find_element(By.XPATH,
											 '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
											 '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

	def tweet_at_provider(self):
		self.driver.get("https://twitter.com/login")
		self.driver.maximize_window()

		time.sleep(5)

		email = self.driver.find_element(By.XPATH,
										 '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div['
										 '2]/div/div/div/div[5]/label/div/div[2]/div/input')
		email.send_keys(self.email)

		go_next = self.driver.find_element(By.XPATH,
										   '// *[ @ id = "layers"] / div / div / div / div / div / div / div[2] / div[2] / div / div / div[2] / div[2] / div / div / div / div[6]')
		go_next.click()

		time.sleep(5)

		password = self.driver.find_element(By.XPATH,
											'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div['
											'2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
		password.send_keys(self.password)

		time.sleep(5)

		login_in = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
													  '2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
		login_in.click()

		time.sleep(15)

		tweet_compose = self.driver.find_element(By.XPATH,
												 '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[''1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[''1]/div/div/div/div/div/div[2]/div')

		tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
		tweet_compose.send_keys(tweet)
		time.sleep(10)

		tweet_button = self.driver.find_element(By.XPATH,
												'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div['
												'1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]')
		tweet_button.click()

		time.sleep(10)
		self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
