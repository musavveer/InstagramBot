from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import os
from os import environ


class InstagramBot:
	def __init__(self,username,password):
		self.username = username
		self.password = password
		self.bot = webdriver.Firefox(executable_path = '/Users/Musavveer Rehaman/Downloads/geckodriver.exe')	

	def login(self):
		bot = self.bot
		bot.get('https://www.instagram.com/accounts/login/')
		time.sleep(3)

		email = bot.find_element_by_name('username').send_keys(self.username)
		password = bot.find_element_by_name('password').send_keys(self.password + Keys.RETURN)
		time.sleep(3)

	def searchHashtag(self,hashtag):
		bot = self.bot
		bot.get('https://www.instagram.com/explore/tags/' + hashtag)

	def likePhotos(self,amount):
		bot = self.bot
		bot.find_element_by_class_name('v1Nh3').click()

		i = 1
		while i <= amount:
			time.sleep(1)
			bot.find_element_by_class_name('fr66n').click()
			bot.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
			time.sleep(1)

			i += 1

insta = InstagramBot(environ['Your_Username'], environ['Your_Password'])
insta.login()
insta.searchHashtag('Hashtags')
insta.likePhotos(2)
