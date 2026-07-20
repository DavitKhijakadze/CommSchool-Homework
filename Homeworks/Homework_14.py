from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time


# #task1

# driver = webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")


# username = driver.find_element(By.ID, "user-name")
# password = driver.find_element(By.ID, "password")
# login_button = driver.find_element(By.ID, "login-button")

# username.send_keys("locked_out_user")
# password.send_keys("secret_sauce")

# login_button.click()

# time.sleep(2)

# try:
#     error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
#     print("ავტორიზაცია ვერ გაიარა. შეცდომის შეტყობინება:")
#     print(error.text)
# except:
#     print("ავტორიზაციამ წარმატებით გაიარა ან ერორის ბლოკი ვერ მოიძებნა.")

# driver.quit()


# #task2

# options = Options()
# options.add_experimental_option("prefs", {"profile.password_manager_leak_detection": False})

# driver = webdriver.Chrome(options=options)
# driver.get("https://www.saucedemo.com/")


# username = driver.find_element(By.ID, "user-name")
# password = driver.find_element(By.ID, "password")
# login_button = driver.find_element(By.ID, "login-button")

# username.send_keys("performance_glitch_user")
# password.send_keys("secret_sauce")

# login_button.click()

# time.sleep(2)

# burger_menu = driver.find_element(By.ID, "react-burger-menu-btn")
# burger_menu.click()

# time.sleep(2)

# logout_btn = driver.find_element(By.ID, "logout_sidebar_link")
# logout_btn.click()

# time.sleep(2)

# driver.quit()


# #task3

# options = Options()
# options.add_experimental_option("prefs", {"profile.password_manager_leak_detection": False})

# driver = webdriver.Chrome(options=options)
# driver.get("https://www.saucedemo.com/")


# username = driver.find_element(By.ID, "user-name")
# password = driver.find_element(By.ID, "password")
# login_button = driver.find_element(By.ID, "login-button")

# username.send_keys("problem_user")
# password.send_keys("secret_sauce")

# login_button.click()

# time.sleep(2)

# item1 = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
# item2 = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")

# item1.click()
# item2.click()

# time.sleep(2)

# cart_btn = driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
# cart_btn.click()

# time.sleep(2)

# remove_item1 = driver.find_element(By.ID, "remove-sauce-labs-backpack")
# remove_item2 = driver.find_element(By.ID, "remove-sauce-labs-bike-light")

# time.sleep(2)

# remove_item1.click()
# remove_item2.click()

# time.sleep(2)

# burger_menu = driver.find_element(By.ID, "react-burger-menu-btn")
# burger_menu.click()

# time.sleep(2)

# logout_btn = driver.find_element(By.ID, "logout_sidebar_link")
# logout_btn.click()

# time.sleep(2)

# driver.quit()


#task4

options = Options()
options.add_experimental_option("prefs", {"profile.password_manager_leak_detection": False})

driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com/")


username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username.send_keys("standard_user")
password.send_keys("secret_sauce")

login_button.click()

time.sleep(2)

item1 = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
item2 = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")

item1.click()
item2.click()

time.sleep(2)

cart_btn = driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
cart_btn.click()

time.sleep(5)

remove_item1 = driver.find_element(By.ID, "remove-sauce-labs-backpack")
remove_item1.click()

time.sleep(2)

back_btn = driver.find_element(By.ID, "continue-shopping")
back_btn.click()

time.sleep(2)

find_item = driver.find_element(By.ID, "item_1_title_link")
find_item.click()

time.sleep(5)

back_btn1 = driver.find_element(By.ID, "back-to-products")
back_btn1.click()

time.sleep(2)

sort_element = driver.find_element(By.CSS_SELECTOR, "[data-test='product-sort-container']")
select = Select(sort_element)
select.select_by_value("hilo")

time.sleep(2)

main_window = driver.current_window_handle

facebook_icon = driver.find_element(By.CSS_SELECTOR, "[data-test='social-facebook']")
facebook_icon.click()
time.sleep(2)

for window_handle in driver.window_handles:
    if window_handle != main_window:
        driver.switch_to.window(window_handle)
        driver.close()
        break

driver.switch_to.window(main_window)

linkedin_icon = driver.find_element(By.CSS_SELECTOR, "[data-test='social-linkedin']")
linkedin_icon.click()
time.sleep(2)

for window_handle in driver.window_handles:
    if window_handle != main_window:
        driver.switch_to.window(window_handle)
        driver.close()
        break

driver.switch_to.window(main_window)

burger_menu = driver.find_element(By.ID, "react-burger-menu-btn")
burger_menu.click()
time.sleep(1)

logout_btn = driver.find_element(By.CSS_SELECTOR, "[data-test='logout-sidebar-link']")
logout_btn.click()
time.sleep(2)

driver.quit()
