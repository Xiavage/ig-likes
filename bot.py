from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import NoSuchElementException

import os
from time import sleep


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.driver = webdriver.Chrome()

        self.login()

    def login(self):
        self.driver.get('https://www.instagram.com/')
        sleep(2)
        # send username to bot
        self.driver.find_element_by_name('username').send_keys(self.username)
        # send password to bot
        self.driver.find_element_by_name('password').send_keys(self.password)
        # click the login button
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div').click()
        sleep(4)
        # delete the not now notfication one
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/div/div/div/button').click()
        sleep(4)
        # delete the not now notification two
        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        sleep(2)

        # look at profile
    def nav_user(self, user):
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(user)
        sleep(2)

        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div').click()

        sleep(2)
        # click on first photo
        self.driver.find_element_by_class_name(
            '_9AhH0').click()
        sleep(2)
        self.like_photos()

    def like_photos(self):
        # we want it so that the program continues to like photos until there is no right arrow
        self.like_photo()
        # check if there is a right arrow

        while True:
            next_pic = self.next_picture()

            if next_pic != False:
                # like the photo
                next_pic.click()
                sleep(2)
                self.like_photo()
            else:
                print("End of Posts!")
                break

    def next_picture(self):
        sleep(2)

        nex = self.driver.find_element_by_class_name(
            "_65Bje")
        sleep(1)
        return nex

    def like_photo(self):
        # like the photo
        sleep(2)
        actionChains = ActionChains(self.driver)
        photo = self.driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
        actionChains.move_to_element_with_offset(
            photo, -20, 0).double_click().perform()

        # move left and up and like the photo
        sleep(2)


if __name__ == '__main__':
    ig_bot = InstagramBot('xiavage', 'Aixtrebla1')

    # ig_bot.nav_user('isabellahouston_')

    ig_bot.nav_user('jjulievu')
