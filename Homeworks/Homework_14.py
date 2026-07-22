from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
import unittest



#task1

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")


username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username.send_keys("locked_out_user")
password.send_keys("secret_sauce")

login_button.click()

time.sleep(2)

try:
    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    print("ავტორიზაცია ვერ გაიარა. შეცდომის შეტყობინება:")
    print(error.text)
except:
    print("ავტორიზაციამ წარმატებით გაიარა ან ერორის ბლოკი ვერ მოიძებნა.")

driver.quit()


#task2

options = Options()
options.add_experimental_option("prefs", {"profile.password_manager_leak_detection": False})

driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com/")


username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username.send_keys("performance_glitch_user")
password.send_keys("secret_sauce")

login_button.click()

time.sleep(2)

burger_menu = driver.find_element(By.ID, "react-burger-menu-btn")
burger_menu.click()

time.sleep(2)

logout_btn = driver.find_element(By.ID, "logout_sidebar_link")
logout_btn.click()

time.sleep(2)

driver.quit()


#task3

options = Options()
options.add_experimental_option("prefs", {"profile.password_manager_leak_detection": False})

driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com/")


username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username.send_keys("problem_user")
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

time.sleep(2)

remove_item1 = driver.find_element(By.ID, "remove-sauce-labs-backpack")
remove_item2 = driver.find_element(By.ID, "remove-sauce-labs-bike-light")

time.sleep(2)

remove_item1.click()
remove_item2.click()

time.sleep(2)

burger_menu = driver.find_element(By.ID, "react-burger-menu-btn")
burger_menu.click()

time.sleep(2)

logout_btn = driver.find_element(By.ID, "logout_sidebar_link")
logout_btn.click()

time.sleep(2)

driver.quit()


#task4

class SauceTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_experimental_option("prefs", {"profile.password_manager_leak_detection": False})

        cls.driver = webdriver.Chrome(options=options)
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://www.saucedemo.com/")
        cls.main_window = cls.driver.current_window_handle


    def test_1_login(self):
        try:
            username = self.driver.find_element(By.ID, "user-name")
            password = self.driver.find_element(By.ID, "password")
            login_button = self.driver.find_element(By.ID, "login-button")

            username.send_keys("standard_user")
            password.send_keys("secret_sauce")

            login_button.click()

            time.sleep(2)

            self.assertIn("inventory.html", self.driver.current_url)
            print("ავტორიზაციამ წარმატებით გაიარა!")

        except Exception as e:
            self.fail(f"ავტორიზაციის დროს დაფიქსირდა შეცდომა: {e}")


    def test_2_cart_and_navigation(self):
        item1 = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        item2 = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
        item1.click()
        item2.click()
        time.sleep(2)

        cart_btn = self.driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
        cart_btn.click()
        time.sleep(5)

        remove_item1 = self.driver.find_element(By.ID, "remove-sauce-labs-backpack")
        remove_item1.click()
        time.sleep(2)

        back_btn = self.driver.find_element(By.ID, "continue-shopping")
        back_btn.click()
        time.sleep(2)

        find_item = self.driver.find_element(By.ID, "item_1_title_link")
        find_item.click()
        time.sleep(5)

        back_btn1 = self.driver.find_element(By.ID, "back-to-products")
        back_btn1.click()
        time.sleep(2)


    def test_3_sort_products(self):
        sort_element = self.driver.find_element(By.CSS_SELECTOR, "[data-test='product-sort-container']")
        select = Select(sort_element)
        select.select_by_value("hilo")
        time.sleep(2)


    def test_4_footer_and_logout(self):
        facebook_icon = self.driver.find_element(By.CSS_SELECTOR, "[data-test='social-facebook']")
        facebook_icon.click()
        time.sleep(2)
        self._close_new_tab_and_return()

        linkedin_icon = self.driver.find_element(
            By.CSS_SELECTOR, "[data-test='social-linkedin']"
        )
        linkedin_icon.click()
        time.sleep(2)
        self._close_new_tab_and_return()

        burger_menu = self.driver.find_element(By.ID, "react-burger-menu-btn")
        burger_menu.click()
        time.sleep(1)

        logout_btn = self.driver.find_element(By.CSS_SELECTOR, "[data-test='logout-sidebar-link']")
        logout_btn.click()
        time.sleep(2)


    def _close_new_tab_and_return(self):
        for window_handle in self.driver.window_handles:
            if window_handle != self.main_window:
                self.driver.switch_to.window(window_handle)
                self.driver.close()
                break
        self.driver.switch_to.window(self.main_window)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()