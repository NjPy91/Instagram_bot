from itertools import count
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from local_settings import *
from random import choice


# ----------------------------------------------#

# ----------------------------------------------#
# Login
def login(driver, username, password, user_choice, *args):


    driver.implicitly_wait(100)
    sleep(3)

    user_input = driver.find_element(By.XPATH,login_user_input_path)
    user_input.clear()
    user_input.send_keys(username)
    sleep(3)
    
    pass_input = driver.find_element(By.XPATH, login_pass_input_path)
    pass_input.clear()
    pass_input.send_keys(password)
    sleep(3)

    login_input = driver.find_element(By.XPATH, login_btn_input_path)
    login_input.click()
    sleep(5)
    driver.implicitly_wait(30)

    if driver.find_element(By.XPATH, "//html/body/div[1]/section/main/div/div"):
        sleep(2)
        driver.find_element(By.XPATH, info_notnow_btn_path).send_keys(Keys.RETURN)
        driver.implicitly_wait(50)

    if driver.find_element(By.XPATH, "//html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div"):
        sleep(2)
        driver.find_element(By.XPATH, notif_notnow_btn_path).send_keys(Keys.RETURN)
        driver.implicitly_wait(30)




    if user_choice == 1:
        like_and_comment(*args)


    if user_choice == 2:
        follow_with_hashtag(*args)

    if user_choice == 3:
        find_following(*args)

    if user_choice == 4:
        view_story(*args)

# ----------------------------------------------#
# Auto like and Auto comment
def like_and_comment(number=5):
    counter = 1
    while counter <= number + 1:
        try:
            driver.implicitly_wait(100)
            like_btn = driver.find_element(By.XPATH, f"//html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/section/div[1]/div[3]/div[1]/div/article[{counter}]/div/div[3]/div/div/section[1]/span[1]/button")
            print(like_btn)
            like_btn.click()
            sleep(2)

            commnet_input = driver.find_element(By.XPATH, f"//html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/section/div[1]/div[3]/div[1]/div/article[{counter}]/div/div[3]/div/div/section[3]/div/form/textarea")
            commnet_input.clear()
            commnet_input.send_keys(choice(COMMENTS))
            sleep(2)
            post_btn = driver.find_element(By.XPATH, f"//html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/section/div[1]/div[3]/div[1]/div/article[{counter}]/div/div[3]/div/div/section[3]/div/form/button")
            post_btn.click()
            driver.implicitly_wait(30)
            sleep(5)

        except:
            print("Error Counter...")
        
        
        counter += 1
        if counter > number:
            break


# Auto Follow with Hashtag
def follow_with_hashtag(hashtag):
    search_input = driver.find_element(By.XPATH, search_input_path)
    search_input.clear()
    search_input.send_keys('#' + hashtag)
    driver.find_element(By.XPATH, search_first_item_path).click()
    sleep(5)
    driver.implicitly_wait(30)
    try:
        follow_btn_txt = driver.find_element(By.XPATH, hashtag_follow_btn_path).text
        if follow_btn_txt == "Follow":
            driver.find_element(By.XPATH, hashtag_follow_btn_path).click()
        else:
            print("Follow this # ego...")
    except:
        print("following...")
    

# Auto find following with hashtag
def find_following(hashtag, number=5):
    search_input = driver.find_element(By.XPATH, search_input_path)
    search_input.clear()
    search_input.send_keys('#' + hashtag)
    driver.find_element(By.XPATH, search_first_item_path).click()
    sleep(5)
    driver.implicitly_wait(30)

    counter = 1
    while counter <= number + 1:
        try:
            follow_modal = driver.find_element(By.XPATH, f"//html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/article/div[1]/div/div/div[1]/div[{counter}]")
            follow_modal.click()
            driver.implicitly_wait(50)
            sleep(5)
            counter += 1

            follow_modal_btn_txt = driver.find_element(By.XPATH, follow_modal_btn_path).text
            if follow_modal_btn_txt == "Follow":
                follow_modal_btn = driver.find_element(By.XPATH, follow_modal_btn_path)
                follow_modal_btn.click()
                sleep(3)
                driver.find_element(By.XPATH, exit_btn_path).click()
                sleep(2)
                driver.implicitly_wait(20)

            else:
                print("this page following ego...")

        except:
            pass


# Auto View Story
def view_story(user_number=3):
    counter = 3
    while counter < user_number + 3:
        try:
            driver.find_element(By.XPATH, f"//html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/section/div[1]/div[2]/div/div/div/div/ul/li[{counter}]/div/button").click()
            driver.implicitly_wait(50)
            sleep(3)
            driver.find_element(By.XPATH , story_forward_btn).click()
            driver.implicitly_wait(30)
            sleep(3)
            driver.find_element(By.XPATH, "//html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/div[3]/button").click()
            sleep(3)
            counter += 1
        except:
            print("this seen...")




if __name__ == "__main__":
    print("*****Choice what do you want......******")
    print('*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*')
    print('''
    **1.Auto Like and Auto Comment
    **2.Auto Follow with Hashtag
    **3.Auto Following with Hashtag
    **4.Auto View story
    **0.Exit form app (END...)
    ''')
    print('*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*')


    user_choice = int(input('Enter your choice: '))


    # Login and Auto like and Auto Comment
    if user_choice == 1:
        username = USERNAME
        password = PASSWORD
        

        driver = webdriver.Firefox(executable_path=PATH)
        driver.get("https://www.instagram.com")
        login(driver,username, password, user_choice)

        sleep(20)
        driver.close()
        

    # follow one with hashtag
    elif user_choice == 2:
        username = USERNAME
        password = PASSWORD
        hashtag = input("Enter HASHTAG: ")

        driver = webdriver.Firefox(executable_path=PATH)
        driver.get("https://www.instagram.com")
        login(driver,username, password, user_choice, hashtag)

        sleep(20)
        driver.close()
        
    #find following with Hashtag
    elif user_choice == 3:
        username = USERNAME
        password = PASSWORD
        hashtag = input("Enter HASHTAG: ")
        number = int(input('Enter number for follow: '))

        driver = webdriver.Firefox(executable_path=PATH)
        driver.get("https://www.instagram.com")
        login(driver,username, password, user_choice, hashtag, number)

        sleep(20)
        driver.close()

   
   # View story
    elif user_choice == 4:
        username = USERNAME
        password = PASSWORD
        user_number = int(input('Enter User number for view: '))

        driver = webdriver.Firefox(executable_path=PATH)
        driver.get("https://www.instagram.com")
        login(driver,username, password, user_choice,user_number)

        sleep(20)
        driver.close()


    else:
        exit()









