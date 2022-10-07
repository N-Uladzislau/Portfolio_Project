from pywinauto.keyboard import SendKeys
from select import select
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchWindowException, \
    ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Helpers_final as H
import time
import unittest

class Chrome_CA_Marketing(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def test_1_Chrome_Log_In(self):
        driver = self.driver
        # Open Browser and go to Website
        driver.get(H.QASV_url)
        print("______________________Positive_Test___________________________")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
              "Test 1 Verify that User able to 'Log In'\n"
              "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        H.delay1_3()
        # Check API Response Code
        H.check_API(driver)
        # Check Title is correct
        H.assert_title(driver, "Home | California Marcketing")
        # Check that the LOGO is present
        H.page_logo(driver)
        wait = WebDriverWait(driver, 10)
        # Log in with Helpers - Function
        H.log_In(driver)
        H.delay1_3()
        # Not Equal Assert
        self.assertIn('Hello vladislavnovik007', driver.page_source)
        # Verify that use get into Account, print text
        print('User get into Account:', driver.find_element(By.XPATH, H.ver_log_in).text)
        # Verify Main Page Logo is present
        print(driver.find_element(By.XPATH, H.main_logo).get_attribute("src"))
        print("______________________Test is Passed!_____________________")

    def test_2_Chrome_Create_new_address(self):
        driver = self.driver
        actions = ActionChains(self.driver)
        wait = WebDriverWait(driver, 10)
        # Set window 1280x800
        driver.set_window_size(1280, 960)
        # Set wait time
        driver.implicitly_wait(10)
        print("______________________Positive_Test___________________________")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
              "Test 2 Create New Address \n"
              "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # get CA-Marketing Website
        driver.get(H.QASV_url)
        # Check API Main Page
        H.check_API(driver)
        H.delay1_3()
        # Get Title
        H.assert_title(driver, "Home | California Marcketing")
        # Log in with Helpers - Function
        H.log_In(driver)
        time.sleep(3)
        # Not Equal Assert
        self.assertIn('Hello', driver.page_source)
        # Verify that use get into Account, print text
        print('User get into Account:', driver.find_element(By.XPATH, H.ver_log_in).text)
        # Verify Main Page Logo is present
        print(driver.find_element(By.XPATH, H.main_logo).get_attribute("src"))
        time.sleep(2)
        # Open Drop Down Menu
        try:  # verify that menu is visible and clickable
            wait.until(EC.visibility_of_element_located((By.XPATH, H.DDM)))
            wait.until(EC.element_to_be_clickable((By.XPATH, H.DDM)))
            # Click on DDM
            driver.find_element(By.XPATH, H.DDM).click()
            time.sleep(1)
            print("DDM is OK !")
        except TimeoutException:
            print("DDM is NOT OK ")
        time.sleep(3)
        # Verify that Option (My Addresses)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.my_addresses)))
        wait.until(EC.element_to_be_clickable((By.XPATH, H.my_addresses)))
        driver.find_element(By.XPATH, H.my_addresses).click()
        time.sleep(5)
        # Assert Title
        H.assert_title(driver, 'My Addresses')
        # assert My addresses to be sure we on right place
        assert 'My Addresses' in driver.page_source
        time.sleep(2)
        # Switch to Address Iframe
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@title='My Addresses']"))
        H.delay1_3()
        # Verify Button "Add New Address"
        wait.until(EC.visibility_of_element_located((By.XPATH, H.button_Add_Address)))
        wait.until(EC.element_to_be_clickable((By.XPATH, H.my_addresses)))
        # Click on Button "Add New Address"
        driver.find_element(By.XPATH, H.button_Add_Address).click()
        # switch back to default
        driver.switch_to.default_content()
        # switch on "Add New Address" frame
        driver.switch_to.frame(3)
        time.sleep(2)
        # Create "New Address" With Helper, Faker
        H.add_new_address_positive(driver)
        time.sleep(3)
        print("______________________Test is Passed, User able to Create New Address_____________________")




    def test_3_Chrome_Add_Product_1_1280x800(self):

        driver = self.driver
        wait = WebDriverWait(driver, 10)
        # Set window 1280x800
        driver.set_window_size(1280, 960)
        # Set wait time
        driver.implicitly_wait(10)
        print("______________________Positive_Test___________________________")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
              "Test 3 Verify that user able to add 'Product 1' to Cart\n"
              "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # get CA-Marketing Website
        driver.get(H.QASV_url)
        # Check API Main Page
        H.check_API(driver)
        H.delay1_3()
        # Get Title
        H.assert_title(driver, "Home | California Marcketing")
        # Get function Scroll to Shop menu and click on Product 1
        H.product1_scroll_to_menu_and_click(driver)
        H.assert_title(driver, 'Product 1 | California Marketing')
        # Get source of Product 1
        H.delay1_3()
        # function for Product 1 El is present and move to El "Add to Cart"
        H.product1_scroll_to_cart(driver)
        H.delay1_3()
        # get scr of main photo "Product 1"
        print(driver.find_element(By.XPATH, H.product1_main_photo).get_attribute("src"))
        # Check if Color "Black" is clickable
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, H.color_brown)))
        # Check if Color "Brown" is Clickable
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, H.color_brown)))
        time.sleep(3)
        # Click on button Color "Black"
        # driver.find_element(By.CSS_SELECTOR,
         #                    ".RadioButton330525410__root:nth-child(1) .ColorPickerItem2577026692__radioInner").click()
        driver.find_element(By.CSS_SELECTOR, H.color_brown).click()
        time.sleep(3)
        # CLick on color "Black"
        # Verify Quantity, by default is 1
        wait.until(EC.visibility_of_element_located((By.XPATH, H.quantity)))
        # Verify if value 1
        wait.until(EC.visibility_of_element_located((By.XPATH, H.value1)))
        # Verify that El "Add to Cart" is visible
        wait.until(EC.visibility_of_element_located((By.XPATH, H.add_to_cart)))
        # button "Add to Cart"  is Clickable
        wait.until(EC.element_to_be_clickable((By.XPATH, H.add_to_cart)))
        time.sleep(3)
        # Click on button "Add to Cart"
        driver.find_element(By.XPATH, H.add_to_cart).click()
        time.sleep(5)
        # Switch on Frame "View Cart"
        H.switch_frame_cart(driver)
        time.sleep(5)
        # Wait till El "View Cart" is Clickable then Click on it
        wait.until(EC.element_to_be_clickable((By.ID, H.view_cart))).click()
        # Asser Dr Title
        H.assert_title(driver, 'Cart | California Marketing')
        time.sleep(5)
        # Print "src" of main logo on the Page
        print(driver.find_element(By.XPATH, H.main_logo).get_attribute('src'))
        # Function for Checkout
        H.checkout_product1(driver)
        # Switch to Frame Checkout
        H.switch_frame_checkout(driver)
        time.sleep(3)
        # Assert that User Cannot place an order and has a Message:
        error = driver.find_element(By.CLASS_NAME, "_33L4Q").text
        print(error)
        assert "We can't accept online orders right now" in error

        print("______________________Test is 'FAIL' cause user Can't place an order!_____________________")


    def test_4_Chrome_meatball_menu1600x1024(self):
        driver = self.driver
        actions = ActionChains(driver)
        wait = WebDriverWait(driver, 10)
        driver.implicitly_wait(10)
        driver.set_window_size(1600, 1024)
        print("______________________Positive_Test___________________________")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
              "TEST 4 'Functional of Meatball Menu'\n"
              "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # get CA-Marketing Website
        driver.get(H.QASV_url)
        # Check API Main Page
        H.check_API(driver)
        H.delay1_3()
        # assert Dr Title of the "Main Page"
        H.assert_title(driver, "Home | California Marcketing")
        # Verify Main Page Logo is present
        print(driver.find_element(By.XPATH, H.main_logo).get_attribute("src"))
        # Scroll down through "Actions function"
        H.scroll_meatball_menu(driver)
        time.sleep(2)
        assert "All Videos" in driver.page_source
        # Verification Menu
        try:
            # Wait till el is Present (Main Menu)
            wait.until(EC.visibility_of_element_located((By.XPATH, H.meatball_main_video)))
            # Verify that Search video field is clickable
            wait.until(EC.element_to_be_clickable((By.XPATH, H.search_video)))
            # Verify that Play Video button is clickable
            wait.until(EC.element_to_be_clickable((By.XPATH, H.play_videos)))
            print("Video Elements is present and clickable")
        except NoSuchElementException:
            print("One of Element is missing")

        # Verify Right Arrow is visible and clickable
        wait.until(EC.visibility_of_element_located((By.XPATH, H.right_arrow)))
        wait.until(EC.element_to_be_clickable((By.XPATH, H.right_arrow)))
        # Click on "Right arrow"
        driver.find_element(By.XPATH, H.right_arrow).click()
        time.sleep(2)
        click_right = driver.find_element(By.XPATH, H.right_arrow).click()
        # Verify Rigth arrow is clickable and click on it "2nd"
        try:
            assert "Dusty Trails: Baja Road Trip" in driver.page_source
            wait.until(EC.element_to_be_clickable((By.XPATH, H.right_arrow)))
            # Click on right arrow with declared variable
            click_right
        except NoSuchElementException:
            print("Text or '2nd' Arrow is missing")
        time.sleep(3)
        # Go Forward and assert "Text" but not equal ! "3rd"
        try:
            self.assertIn("North to South ••", driver.page_source)
            wait.until(EC.element_to_be_clickable((By.XPATH, H.right_arrow)))
            driver.find_element(By.XPATH, H.right_arrow).click()
        except NoSuchElementException:
            print("Text or '3rd' Arrow is missing")
        time.sleep(3)
        # Go Forward, But now use Raise Exception if smth wrong "4th"
        try:
            self.assertIn("New York City", driver.page_source)
            wait.until(EC.element_to_be_clickable((By.XPATH, H.right_arrow)))
            driver.find_element(By.XPATH, H.right_arrow).click()
        except NoSuchElementException:
            raise Exception("Unable to Click on '4th' Arrow")
        time.sleep(3)
        # Go on next video "5th"
        try:
            self.assertIn("San Francisco", driver.page_source)
            wait.until(EC.element_to_be_clickable((By.XPATH, H.right_arrow)))
            driver.find_element(By.XPATH, H.right_arrow).click()
        except NoSuchElementException:
            raise Exception("Unable to Click on 5th Arrow")
        time.sleep(3)
        # Verify that everything is OK on "6th"
        try:
            assert "No Result Found" not in driver.page_source
            self.assertIn("AVENGERS 5", driver.page_source)
            wait.until(EC.element_to_be_clickable((By.XPATH, H.right_arrow)))
            driver.find_element(By.XPATH, H.right_arrow).click()
        except NoSuchElementException:
            print("Unable to Click on '6th' Arrow")
        time.sleep(3)
        # Verify That on last video "Arrow Right" is missing and print it !
        try:
            wait = WebDriverWait(driver, 3)
            wait.until(EC.visibility_of_element_located((By.XPATH, H.right_arrow)))
        except TimeoutException:
            print("No Right Arrow Element on the page")
        # Verify last Video and go "Back" on Previous Video "AVENGERS 5"
        try:
            self.assertIn("Big Sur California:", driver.page_source)
            wait.until(EC.visibility_of_element_located((By.XPATH, H.left_arrow)))
            driver.find_element(By.XPATH, H.left_arrow).click()
        except TimeoutException:
            print("Left Arrow is Missing")
        time.sleep(1)
        # Go to Previous Video "San Francisco"
        wait.until(EC.visibility_of_element_located((By.XPATH, H.left_arrow)))
        driver.find_element(By.XPATH, H.left_arrow).click()
        time.sleep(1)
        # Go to Previous Video "New York City"
        wait.until(EC.visibility_of_element_located((By.XPATH, H.left_arrow)))
        driver.find_element(By.XPATH, H.left_arrow).click()
        time.sleep(1)
        # Go to Previous Video "North to South"
        wait.until(EC.visibility_of_element_located((By.XPATH, H.left_arrow)))
        driver.find_element(By.XPATH, H.left_arrow).click()
        time.sleep(1)
        # Go to Previous Video "Dusty Trails"
        wait.until(EC.visibility_of_element_located((By.XPATH, H.left_arrow)))
        driver.find_element(By.XPATH, H.left_arrow).click()
        time.sleep(1)
        # Go to Main Video
        wait.until(EC.visibility_of_element_located((By.XPATH, H.left_arrow)))
        driver.find_element(By.XPATH, H.left_arrow).click()
        time.sleep(1)
        # Verify Main Video Page
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, H.play_videos)))
            wait.until(EC.visibility_of_element_located((By.XPATH, H.meatball_main_video)))
        except TimeoutException:
            print("Main Video Page is NOT OKAY")
        # Verify That Left Arrow Is Mission on The Main Page
        try:
            wait = WebDriverWait(driver, 2)
            wait.until(EC.visibility_of_element_located((By.XPATH, H.left_arrow)))
        except TimeoutException:
            print("No Left Arrow on the 'Main Video'")
        # Scroll Up on main Page
        actions.move_to_element(driver.find_element(By.XPATH, H.main_logo)).perform()
        time.sleep(2)
        # Assert Text on the Main Page
        assert "CALIFORNIA MARCKETING" in driver.page_source
        print("______________________Test is Passed______________________")


    def test_5_Chrome_Reg_Event_3_1600x1024(self):

        driver = self.driver
        actions = ActionChains(driver)
        wait = WebDriverWait(driver, 10)
        driver.implicitly_wait(10)
        driver.set_window_size(1600, 1024)
        print("______________________Positive_Test___________________________")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
              "TEST 5 'Registration for Event 3'\n"
              "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # get CA-Marketing Website
        driver.get(H.QASV_url)
        # Check API Main Page
        H.check_API(driver)
        H.delay1_3()
        # assert Dr Title of the "Main Page"
        H.assert_title(driver, "Home | California Marcketing")
        # Verify Main Page Logo is present
        print(driver.find_element(By.XPATH, H.main_logo).get_attribute("src"))
        time.sleep(2)
        # Scroll till Upcoming Events
        H.scroll_upcoming_events(driver)
        time.sleep(3)
        # assert that" Upcoming Events" present on the page
        assert "Upcoming Events" in driver.page_source
        # Verify that "Event 3" is present
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, H.event_3_text)))
        # Verify that "RSVP" button for Event 3 is clickable
        wait.until(EC.element_to_be_clickable((By.XPATH, H.button_event_3)))
        H.delay1_3()
        # Click on button "Event 3"
        try:
            driver.find_element(By.XPATH, H.button_event_3).click()
            print("Button 'Event 3' OK")
        except NoSuchElementException:
            print("Button 'Event 3' Doesn't work")
        time.sleep(3)
        # Verify that Title is correct !
        H.assert_title(driver, 'Event 3 | California Marketing')
        time.sleep(2)
        # Verify text "Event 3" is present
        assert "Event 3" in driver.page_source
        # Get src of photo for Event 3
        print(driver.find_element(By.XPATH, H.photo_event_3).get_attribute('src'))
        # Verify Time and Location
        print('Time and Location is present: ', driver.find_element(By.XPATH, H.time_location).text)
        # Verify Full DATE and print it
        print(driver.find_element(By.XPATH, H.full_date).text)

        try:
            assert "Desctiption is missing, report this bug." in driver.page_source
            print("Report Bug, That Description is missing!")
        except:
            print("Bug was Fixed")

        # Verify that Button "RSVP" is Visible and Clickable nad Click on it !
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, H.inner_button_event_3)))
            wait.until(EC.element_to_be_clickable((By.XPATH, H.inner_button_event_3)))
            driver.find_element(By.XPATH, H.inner_button_event_3).click()
            print("User get into RVSP")
        except TimeoutException:
            print("Button for Inner 'Event 3' Doesn't work")
        time.sleep(3)
        # Verify Main Logo
        driver.find_element(By.XPATH, H.main_logo)
        H.delay1_3()
        # Assert Text on the Page
        assert "CALIFORNIA MARCKETING" in driver.page_source
        H.delay1_3()
        assert "Event 3" in driver.page_source
        # Function for FN, LN, Email and button Submit
        H.regist_field_verification(driver)
        time.sleep(3)
        # Function Fake for Date FN, LN, Email. And click on Submit!
        H.create_faker_data_for_event_3(driver)
        time.sleep(3)
        # Verify that Registration was Successful
        assert 'Thank you! See you soon' in driver.page_source
        try:
            assert "An email with the event's details was sent to you" in driver.page_source
            print("Registration was Successful")
        except NoSuchElementException:
            print("Registration Failed, Smth went Wrong!")

        print("______________________Test is Passed______________________")


    def test_6_Chrome_Sign_up(self):

        driver = self.driver
        actions = ActionChains(driver)
        wait = WebDriverWait(driver, 10)
        driver.implicitly_wait(10)
        print("______________________Negative Test___________________________")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
              "TEST 6 'Sign Up with Existing Email and valid Password'\n"
              "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # get CA-Marketing Website
        driver.get(H.QASV_url)
        # Check API Main Page
        H.check_API(driver)
        H.delay1_3()
        # assert Dr Title of the "Main Page"
        H.assert_title(driver, "Home | California Marcketing")
        # Verify Main Page Logo is present
        print(driver.find_element(By.XPATH, H.main_logo).get_attribute("src"))
        time.sleep(2)
        # H.sign_up_to_account(driver)
        time.sleep(3)
        # Verify that button 'Log in' is present and clickable then click on it
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, H.log_in)))
            wait.until(EC.element_to_be_clickable((By.XPATH, H.log_in)))
            driver.find_element(By.XPATH, H.log_in).click()
            print("Log in button is OK")
        except TimeoutException:
            print("Log In button is NOT OK")
        time.sleep(2)
        # assert 'Sign Up' Text on the page
        assert 'Sign Up' in driver.page_source
        time.sleep(1)
        # Verify that button 'Sign Up' is present and clickable then click on it
        try:
            wait.until(EC.visibility_of_element_located((By.ID, H.sign_up_button_with_email)))
            wait.until(EC.element_to_be_clickable((By.ID, H.sign_up_button_with_email)))
            driver.find_element(By.ID, H.sign_up_button_with_email).click()
            print("Sing up button is OK")
        except TimeoutException:
            print("Sing up button NOT OK")
        time.sleep(3)
        # assert Title
        H.assert_title(driver, 'Home | California Marcketing')
        # Assert not equal Text on the page
        self.assertIn("Sign Up", driver.page_source)

        time.sleep(1)
        # Verify Email field present and clickable
        wait.until(EC.visibility_of_element_located((By.ID, H.email_sign_up)))
        wait.until(EC.element_to_be_clickable((By.ID, H.email_sign_up)))
        # Cleat The field
        driver.find_element(By.ID, H.email_sign_up).clear()
        # Enter Existing Email
        driver.find_element(By.ID, H.email_sign_up).send_keys(H.user_email)
        time.sleep(1)
        # Verify Password field present and clickable
        wait.until(EC.visibility_of_element_located((By.ID, H.password_sign_up)))
        wait.until(EC.element_to_be_clickable((By.ID, H.password_sign_up)))
        # Cleat The field
        driver.find_element(By.ID, H.password_sign_up).clear()
        # Enter Valid password
        driver.find_element(By.ID, H.password_sign_up).send_keys(H.user_pass)
        time.sleep(2)
        # Verify That button Sign up is visible and clickable
        wait.until(EC.visibility_of_element_located((By.ID, H.sign_up_button)))
        wait.until(EC.element_to_be_clickable((By.ID, H.sign_up_button)))

        # Try to "Sign Up" With Existing Email !!! it has to be Error !
        # Error Captcha is required to verify that you're a human
        try:
            driver.find_element(By.ID, H.sign_up_button).click()
            print("At The moment We CANNOT 'Sign Up' cause of 'Captcha'")
        except NoSuchElementException:
            print("Button 'Sign Up' Doesn't work")
        # Text "Captcha" Doesn't Allow to Sign Up
        print(driver.find_element(By.ID, 'siteMembersInputErrorMessage_emailInput_SM_ROOT_COMP15').text)
        time.sleep(5)
        print("_________Test Passed When I did Manual Testing______")

    def test_7_Chrome_Invalid_Email_Log_In(self):

        driver = self.driver
        actions = ActionChains(driver)
        wait = WebDriverWait(driver, 10)
        driver.implicitly_wait(10)
        print("______________________Negative Test___________________________")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
              "TEST 7 'Enter Invalid Email and valid Password for Log In'\n"
              "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # get CA-Marketing Website
        driver.get(H.QASV_url)
        # Check API Main Page
        H.check_API(driver)
        H.delay1_3()
        # assert Dr Title of the "Main Page"
        H.assert_title(driver, "Home | California Marcketing")
        # Verify Main Page Logo is present
        print(driver.find_element(By.XPATH, H.main_logo).get_attribute("src"))
        # Verify that button 'Log in' is present and clickable then click on it
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, H.log_in)))
            wait.until(EC.element_to_be_clickable((By.XPATH, H.log_in)))
            driver.find_element(By.XPATH, H.log_in).click()
            print("Log in button is OK")
        except TimeoutException:
            print("Log In button is NOT OK")
        time.sleep(3)
        # assert "Sign on" Present on the page
        assert "Sign Up" in driver.page_source
        # print that Button is present on the page
        print(driver.find_element(By.XPATH, H.log_in).text, "Button is Present on the Page")
        time.sleep(3)
        # Verify Button inner Log in and click on it
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, H.inner_log_in)))
            wait.until(EC.element_to_be_clickable((By.XPATH, H.inner_log_in)))
            driver.find_element(By.XPATH, H.inner_log_in).click()
            print("Inner button Login In is OK")
        except TimeoutException:
            print("Inner button Login In is NOT OK")
        time.sleep(3)
        # Verify button Log in with Email and click on it !
        wait.until(EC.visibility_of_element_located((By.XPATH, H.log_in_with_email)))
        wait.until(EC.element_to_be_clickable((By.XPATH, H.log_in_with_email)))
        driver.find_element(By.XPATH, H.log_in_with_email).click()
        time.sleep(2)
        # Assert "Email" text is present on the page
        assert 'Email' in driver.page_source
        # Assert Password text os present on the page
        assert "Password" in driver.page_source
        # Verify Email field and enter Data
        try: # Visible
            wait.until(EC.visibility_of_element_located((By.ID, H.email_log_in)))
            # Clickable
            wait.until(EC.element_to_be_clickable((By.ID, H.email_log_in)))
            # Clear
            driver.find_element(By.ID, H.email_log_in).clear()
            # input Valid Email
            driver.find_element(By.ID, H.email_log_in).send_keys(H.invalid_email_name)
            print("Email is OK")
        except TimeoutException:
            print("Email is NOT OK")
        time.sleep(2)
        # Verify Password and enter Data
        try:
            wait.until(EC.visibility_of_element_located((By.ID, H.password_log_in)))
            # Clickable
            wait.until(EC.element_to_be_clickable((By.ID, H.password_log_in)))
            # Clear
            driver.find_element(By.ID, H.password_log_in).clear()
            # input Valid Email
            driver.find_element(By.ID, H.password_log_in).send_keys(H.user_pass)
            print("Password is OK")
        except TimeoutException:
            print("Password is NOT OK")
        time.sleep(2)
        # Click on Button Log in and Enter in Account!
        driver.find_element(By.ID, H.final_Button_log_in).click()
        time.sleep(3)
        print(driver.find_element(By.ID, 'siteMembersInputErrorMessage_passwordInput_SM_ROOT_COMP16').text)
        print("Error Has to show us, Invalid email address 'Contains only Numbers! '")
        driver.save_screenshot("Wrong Error Message.png")
        print("_______________________________Test Failed_______________________")

    def test_8_Chrome_Subscribe_Form(self):

        driver = self.driver
        wait = WebDriverWait(driver, 10)
        driver.implicitly_wait(10)
        print("______________________Negative Test___________________________")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
              "TEST 8 'Verify “Subscribe form” on invalid Email'\n"
              "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # get CA-Marketing Website
        driver.get(H.QASV_url)
        # Check API Main Page
        H.check_API(driver)
        H.delay1_3()
        # assert Dr Title of the "Main Page"
        H.assert_title(driver, "Home | California Marcketing")
        # Verify Main Page Logo is present
        print(driver.find_element(By.XPATH, H.main_logo).get_attribute("src"))
        time.sleep(2)
        # Scroll down till Subscribe form
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.XPATH, H.subscribe_form))
        time.sleep(2)
        # Verify that Subscribe form is present
        assert 'Subscribe Form' in driver.page_source
        # driver.find_element(By.XPATH, '')
        print(driver.find_element(By.XPATH, '//*[text()="California Marcketing"]').get_attribute("href"))
        time.sleep(2)
        # Verify Subscribe Text on the page
        wait.until(EC.visibility_of_element_located((By.XPATH, H.subscribe_form)))
        # Verify "Email Address" placeholder
        wait.until(EC.visibility_of_element_located((By.XPATH, H.email_address_placeholder)))
        # Placeholder is Clickable
        wait.until(EC.element_to_be_clickable((By.XPATH, H.subscribe_form)))
        time.sleep(2)
        # Verify Submit button
        wait.until(EC.visibility_of_element_located((By.XPATH, H.submit_button)))
        # Submit button is clickable
        wait.until(EC.element_to_be_clickable((By.XPATH, H.submit_button)))
        # Enter invalid Email Contains only numbers
        driver.find_element(By.XPATH, H.email_address_placeholder).clear()
        driver.find_element(By.XPATH, H.email_address_placeholder).send_keys(H.invalid_email_name)
        time.sleep(2)
        # Click on button Submit
        driver.find_element(By.XPATH, H.submit_button).click()
        time.sleep(3)
        print("We've got 'Thanks for submitting!' Instead Invalid Email Address")
        print("___________________Test is Failed____________________")

    def test_9_Chrome_Product_1_Quantity_1888888(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        driver.implicitly_wait(10)
        print("______________________Negative Test___________________________")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
              "TEST 9 'Verify that User CANNOT enter 0 value for product 1'\n"
              "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # get CA-Marketing Website
        driver.get(H.QASV_url)
        # Check API Main Page
        H.check_API(driver)
        H.delay1_3()
        # assert Dr Title of the "Main Page"
        H.assert_title(driver, "Home | California Marcketing")
        # Verify Main Page Logo is present
        print(driver.find_element(By.XPATH, H.main_logo).get_attribute("src"))
        time.sleep(2)
        # Go to Shop menu use fucntion for it
        H.product_1_shop(driver)
        time.sleep(3)
        # Assert title "Shop"
        H.assert_title(driver, 'Shop | California Marcketing')
        # Check if Logo is present
        H.page_logo(driver)
        print(driver.find_element(By.XPATH, H.src_product1).get_attribute('src'))
        time.sleep(2)
        # Verify that Button for Product 1 is OK
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, H.product_1_button)))
            wait.until(EC.element_to_be_clickable((By.XPATH, H.product_1_button)))
            driver.find_element(By.XPATH, H.product_1_button).click()
        except TimeoutException:
            print("Button for 'Product 1' Is NOT OK")
        time.sleep(2)
        # get src of Main Photo
        print(driver.find_element(By.XPATH, H.product1_main_photo).get_attribute('src'))
        # Scroll down till description
        driver.execute_script("window.scrollTo(0, window.scrollY + 1000)")
        time.sleep(2)
        # Verify Color of Product and choose black one
        try:
            # Verify Color of Product
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, H.color_black)))
            # Color is Clickable
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, H.color_black)))
            time.sleep(1)
            # Choose Black one
            driver.find_element(By.CSS_SELECTOR, H.color_black).click()
            time.sleep(2)
            print("Black Color was selected")
        except TimeoutException:
            print("Black color wasn't found")
        # Verify Quantity field and Choose '0' value
        value1 = driver.find_element(By.XPATH, H.quantity).send_keys(9 + 9)
        try:
            # Verify Quantity field
            wait.until(EC.visibility_of_element_located((By.XPATH, H.quantity)))
            wait.until(EC.element_to_be_clickable((By.XPATH, H.quantity)))
            # Enter Value: "1888888"
            driver.find_element(By.XPATH, H.quantity).send_keys(1999 + 1999)
            driver.find_element(By.XPATH, H.quantity).send_keys(1999 + 1999)
            driver.find_element(By.XPATH, H.quantity).send_keys(1999 + 1999)
            driver.find_element(By.XPATH, H.quantity).send_keys(1999 + 1999)
            driver.find_element(By.XPATH, H.quantity).send_keys(1999 + 1999)
            time.sleep(1)
        except ElementNotInteractableException:
            raise Exception("Field Quantity Doesn't Work")
        # click on Button "Add To Cart"
        driver.find_element(By.XPATH, H.add_to_cart).click()
        time.sleep(3)
        # Assert that User Can't "Add to Card" More than "99999"
        assert 'Only 99999 left in stock' in driver.page_source
        time.sleep(2)
        print("~~~~~~~~~~~~~~~~~User Can't 'Add to Cart' more than '99999'~~~~~~~~~~~~~~~~~~~~~~~~ ")
        print("________________________________Test is Passed____________________________________")


    def test__10_Chrome_Create_Address_Invalid_FN(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        driver.implicitly_wait(10)
        print("______________________Negative Test___________________________")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
              "TEST 10 'Verify that User CANNOT enter 0 value for product 1'\n"
              "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # get CA-Marketing Website
        driver.get(H.QASV_url)
        # Check API Main Page
        H.check_API(driver)
        H.delay1_3()
        # assert Dr Title of the "Main Page"
        H.assert_title(driver, "Home | California Marcketing")
        # Verify Main Page Logo is present
        print(driver.find_element(By.XPATH, H.main_logo).get_attribute("src"))
        time.sleep(2)
        # Function 'Log in'
        H.log_In(driver)
        time.sleep(4)
        # Verify that user get into account
        print(driver.find_element(By.XPATH, H.ver_log_in).text)
        time.sleep(2)
        # Open Drop Down Menu
        try: # verify that menu is visisble and clickable
            wait.until(EC.visibility_of_element_located((By.XPATH, H.DDM)))
            wait.until(EC.element_to_be_clickable((By.XPATH, H.DDM)))
            # Click on DDM
            driver.find_element(By.XPATH, H.DDM).click()
            time.sleep(1)
            print("DDM is OK !")
        except TimeoutException:
            print("DDM is NOT OK ")
        time.sleep(3)
        # Verify that Option (My Addresses)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.my_addresses)))
        wait.until(EC.element_to_be_clickable((By.XPATH, H.my_addresses)))
        driver.find_element(By.XPATH, H.my_addresses).click()
        time.sleep(4)
        # Assert Title
        H.assert_title(driver, 'My Addresses')
        # assert My addresses to be sure we on right place
        assert 'My Addresses' in driver.page_source
        # Switch Frame # 1
        # driver.switch_to.frame(0)
        # Switch Frame # 2 with 'SelectorsHub'
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@title='My Addresses']"))
        time.sleep(1)
        driver.find_element(By.XPATH, H.button_Add_Address).click()
        time.sleep(2)
        # We can use this
        driver.switch_to.default_content()
        driver.switch_to.frame(3)
        time.sleep(3)
        H.add_new_addres_negative(driver)
        time.sleep(3)
        print("____________________Test Is Failed____________________")
        print("______User able to Create Address with Invalid First Name, contains only Numbers_______")

    def tearDown(self):
        self.driver.quit()





