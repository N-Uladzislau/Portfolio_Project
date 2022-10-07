import time
import random
import driver
import requests
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchWindowException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
from selenium.webdriver import ActionChains
actions = ActionChains(driver)
faker_class = Faker()
F = Faker()
F.Number = Faker(["en_CA"])





# Email for User
user_email = "vladislavnovik007@gmail.com"
# Invalid Email for user
invalid_email_name = "11111@gmail.com"
# Password for User
user_pass = "12345678"
# Verify Log In
ver_log_in = '//*[@class="_1i-z_"]'
# Url for Website
QASV_url = "https://qasvus.wixsite.com/ca-marketing"


# Main logo
main_logo = '//img[@alt="iot_sq.png"]'

# Log In button
log_in = "//*[text()='Log In']"
# final login button for Log in w
final_Button_log_in = "okButton_SM_ROOT_COMP16"
# Inner Log In button
inner_log_in = '//*[@class="_3VCEv focus-within"]'
# Log In with Email
log_in_with_email = '//*[@data-testid="switchToEmailLink"][@aria-disabled="false"]'


# input email For Log In: Log in and Sign up have different locators
email_log_in = 'input_input_emailInput_SM_ROOT_COMP16'
# input password For log in:  Log in and Sign up have different locators
password_log_in = 'input_input_passwordInput_SM_ROOT_COMP16'


# By ID
sign_up_button_with_email = 'switchToEmailLink_SM_ROOT_COMP15'
# Email for Sign Up By ID
email_sign_up = 'input_input_emailInput_SM_ROOT_COMP15'
# Password for Sign Up By
password_sign_up = 'input_input_passwordInput_SM_ROOT_COMP15'
# Sign Up button for submit ! it's different between Switch to
sign_up_button = 'okButton_SM_ROOT_COMP15'

# By ID field for Add New Address ( First Name )
first_name_field = "firstName-field"

# By ID field for Add New Address ( Last Name )
last_name_field = 'lastName-field'

# Locators for Product 1

# Button for Product 1
product_1_button = '//*[text()="Product 1"]'

# Locator for main photo "Product 1"
product1_main_photo = '//img[@class="_2NNgJ _24O7B er7Ub"]'

# Locator for "Product 1" text description
product_1_description = '//*[contains(text(),"I\'m a product 1")]'

# Locator for Color "Black"
color_black = '.RadioButton330525410__root:nth-child(1) .ColorPickerItem2577026692__radioInner'
# One more locator for Black ".RadioButton330525410__root:nth-child(1) .ColorPickerItem2577026692__radioInner"

# Color Brown
color_brown = ".RadioButton330525410__root:nth-child(2) .ColorPickerItem2577026692__radioInner"


# Quantity is present
quantity1 = '//*[text()="Quantity"]'
quantity = '//*[@type="number"]'

# Value for "Produc 1"
value1 = '//*[@value="1"]'

# Add to Cart
add_to_cart = '//*[@class="buttonnext1749291004__content"]'    # '//*[contains(text(),"Add to Card")]'

# View cart
view_cart = "widget-view-cart-button"

# Subscribe form locator
subscribe_form = '//*[text()="Subscribe Form"]'
# Email input for subscribe
email_address_placeholder = '//*[@id="input_comp-ksocylga1"]'
# Submit button for Subscribe form
submit_button = '//*[text()="Submit"]'

# src for Product 1 on Shop Menu
src_product1 = '//img[@src="https://static.wixstatic.com/media/3c76e2_f2d88894bda246979ba21e699878a3fa~mv2.jpg/v1/' \
               'fill/w_225,h_225,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/3c76e2_f2d88894bda246979ba21e699878a3fa~mv2.jpg"]'




DDM = '//*[@class="_1i-z_"]'
# Open dropdown menu
# Open dropdown menu
DDM1 = ".\\_1hHt1 > svg"
# Open My Addresses
my_addresses = '//*[text()="My Addresses"]'

button_Add_Address = '//div[@class="_10o0_ _26mkp hidden-mobile"]//button[@class="_172js"][contains(text(),"Add New Address")]'


def add_new_address_positive(driver):
    wait = WebDriverWait(driver, 10)
    try:
        # Enter Valid First Name: Use Faker for it
        wait.until(EC.visibility_of_element_located((By.ID, first_name_field)))
        wait.until(EC.element_to_be_clickable((By.ID, first_name_field)))
        driver.find_element(By.ID, first_name_field).clear()
        driver.find_element(By.ID, first_name_field).send_keys(F.first_name())
    except TimeoutException:
        print("FN field NOT OK")
    time.sleep(2)
    try:
        # Enter Valid Last Name: Use Faker for it
        wait.until(EC.visibility_of_element_located((By.ID, last_name_field)))
        wait.until(EC.element_to_be_clickable((By.ID, last_name_field)))
        driver.find_element(By.ID, last_name_field).clear()
        driver.find_element(By.ID, last_name_field).send_keys(F.last_name())
    except TimeoutException:
        print("LN field NOT OK")
    time.sleep(2)
    # Faker for Company
    wait.until(EC.visibility_of_element_located((By.ID, 'company-field')))
    wait.until(EC.element_to_be_clickable((By.ID, 'company-field')))
    driver.find_element(By.ID, 'company-field').clear()
    driver.find_element(By.ID, 'company-field').send_keys(F.company())
    time.sleep(2)
    # Faker for Address line  Only CA
    wait.until(EC.visibility_of_element_located((By.ID, 'addressLine1-field')))
    wait.until(EC.element_to_be_clickable((By.ID, 'addressLine1-field')))
    driver.find_element(By.ID, 'addressLine1-field').clear()
    driver.find_element(By.ID, 'addressLine1-field').send_keys(F.street_address())
    time.sleep(2)
    # Faker for Address line 2 , APT, Suite, floor
    wait.until(EC.visibility_of_element_located((By.ID, 'addressLine2-field')))
    wait.until(EC.element_to_be_clickable((By.ID, 'addressLine2-field')))
    driver.find_element(By.ID, 'addressLine2-field').clear()
    driver.find_element(By.ID, 'addressLine2-field').send_keys(F.secondary_address())
    time.sleep(2)
    # Faker for city
    wait.until(EC.visibility_of_element_located((By.ID, 'city-field')))
    wait.until(EC.element_to_be_clickable((By.ID, 'city-field')))
    driver.find_element(By.ID, 'city-field').clear()
    driver.find_element(By.ID, 'city-field').send_keys(F.city())
    time.sleep(1)
    # Faker for State
    wait.until(EC.visibility_of_element_located((By.ID, 'subdivision-field')))
    wait.until(EC.element_to_be_clickable((By.ID, 'subdivision-field')))
    driver.find_element(By.ID, 'subdivision-field').clear()
    driver.find_element(By.ID, 'subdivision-field').send_keys(F.state_abbr())
    time.sleep(2)
    # Faker for ZipCode
    wait.until(EC.visibility_of_element_located((By.ID, 'zipCode-field')))
    wait.until(EC.element_to_be_clickable((By.ID, 'zipCode-field')))
    driver.find_element(By.ID, 'zipCode-field').clear()
    driver.find_element(By.ID, 'zipCode-field').send_keys(F.zipcode())
    time.sleep(2)
    # Faker for Phone number Only CA
    wait.until(EC.visibility_of_element_located((By.ID, 'phone-field')))
    wait.until(EC.element_to_be_clickable((By.ID, 'phone-field')))
    driver.find_element(By.ID, 'phone-field').clear()
    driver.find_element(By.ID, 'phone-field').send_keys(F.Number.phone_number())
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@aria-label="Add Address and close dialog, button"]').click()



# Add new Address For Negative Testing with Invalid FN
def add_new_addres_negative(driver):
    try:
        # Enter Invalid Fist Name "12345" only Num
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, first_name_field)))
        wait.until(EC.element_to_be_clickable((By.ID, first_name_field)))
        driver.find_element(By.ID, first_name_field).clear()
        driver.find_element(By.ID, first_name_field).send_keys('12345')
        print("Invalid FN Entered")
    except TimeoutException:
        print("FN field NOT OK")
        time.sleep(1)
    try:
        # Enter Valid Last Name: Use Faker for it
        wait.until(EC.visibility_of_element_located((By.ID, last_name_field)))
        wait.until(EC.element_to_be_clickable((By.ID, last_name_field)))
        driver.find_element(By.ID, last_name_field).clear()
        driver.find_element(By.ID, last_name_field).send_keys(F.last_name())
    except TimeoutException:
        print("LN field NOT OK")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@aria-label="Add Address and close dialog, button"]').click()
    time.sleep(1)






# Delay
def delay1_3():
    time.sleep(random.randint(1, 3))


# Wait time
wait = WebDriverWait(driver, 5)


# Check API
def check_API(driver):
    code = requests.get(driver.current_url).status_code
    if code == 200:
        print("Url has ", requests.get(driver.current_url).status_code, " as Status Code")
    else:
        print("API response code is not 200")

# asser dr title
def assert_title(driver, title):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.title_is(title))
    assert title in driver.title
    print(f"Page has, {driver.title} as Page title")
    # Scr of page if pas has different title
    driver.get_screenshot_as_file(f"Page has different {title}.png")
    if not title in driver.title:
        raise Exception(f"Page {title} has wrong Title!")


# Check that "Main Logo" is present and visible
def page_logo(driver):
    try:
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@alt="iot_sq.png"]')))
        print(f"LOGO is present and correct!")
    except NoSuchElementException:
        print("Logo is NOT present on the Main Page")
        driver.get_screenshot_as_file("Page has different LOGO.png")






# Function for Log In
def log_In(driver):
    wait = WebDriverWait(driver, 10)
    # Button Log in on the Main Page
    try:  # Button visible and clickable
        wait.until(EC.visibility_of_element_located((By.XPATH, log_in)))
        wait.until(EC.element_to_be_clickable((By.XPATH, log_in)))
        # Click on Button
        driver.find_element(By.XPATH, log_in).click()
        print("Log In Button is OK")
    except TimeoutException:
        print("Log In Button is NOT OK")
    time.sleep(2)
    try: # Inner Button Log in Is Visible and clickable
        wait.until(EC.visibility_of_element_located((By.XPATH, inner_log_in)))
        wait.until(EC.element_to_be_clickable((By.XPATH, inner_log_in)))
        # click on the inner Button
        driver.find_element(By.XPATH, inner_log_in).click()
        print("Inner Button Log In is OK")
    except TimeoutException:
        print("Inner Button Log In is NOT OK")
    time.sleep(2)
    try: # Verify that Button "Log in With Email" Is visible and clickable
        wait.until(EC.visibility_of_element_located((By.XPATH, log_in_with_email)))
        wait.until(EC.element_to_be_clickable((By.XPATH, log_in_with_email)))
        # Click on it
        driver.find_element(By.XPATH, log_in_with_email).click()
        print("Button 'Log in with Email' is OK")
    except TimeoutException:
        print("Button 'Log in with Email' is NOT OK")
    # Verify that Placeholder for Email is visible and clickable
    wait.until(EC.visibility_of_element_located((By.ID, email_log_in)))
    wait.until(EC.element_to_be_clickable((By.ID, email_log_in)))
    # Clear Field
    driver.find_element(By.ID, email_log_in).clear()
    time.sleep(1)
    # Enter Valid Email
    driver.find_element(By.ID, email_log_in).send_keys(user_email)
    time.sleep(1)
    # Verify that Placeholder for Password is visible and clickable
    wait.until(EC.visibility_of_element_located((By.ID, password_log_in)))
    wait.until(EC.element_to_be_clickable((By.ID, password_log_in)))
    # Clear Field
    driver.find_element(By.ID, password_log_in).clear()
    time.sleep(1)
    # Enter Valid Email
    driver.find_element(By.ID, password_log_in).send_keys(user_pass)
    time.sleep(2)
    # Verify Final Log In Visible and clickable
    wait.until(EC.visibility_of_element_located((By.ID, final_Button_log_in)))
    wait.until(EC.element_to_be_clickable((By.ID, final_Button_log_in)))
    # Click on The button "Log In"
    driver.find_element(By.ID, final_Button_log_in).click()

# function, On main page scroll to menu and click on "Product 1" For Chrome
def product1_scroll_to_menu_and_click(driver):
    shop_menu = driver.find_element(By.XPATH, '//*[@class="s5QqWI FdnK0d"]')
    product_1 = driver.find_element(By.XPATH, '//*[@class="slick-slide slick-active slick-current"]')
    actions = ActionChains(driver)
    actions.move_to_element(shop_menu).click(product_1).perform()

# function, on product 1 scroll to button "Add to Cart" For Chrome
def product1_scroll_to_cart(driver):
    actions = ActionChains(driver)
    wait = WebDriverWait(driver, 10)
    # Wait till el is located
    wait.until(EC.visibility_of_element_located((By.XPATH, product_1_description)))
    # variable for "Add to Cart"
    add_to_cart = driver.find_element(By.XPATH, "//*[contains(text(),'Add to Card')]")
    # Move to El "Add to Cart"
    actions.move_to_element(add_to_cart).perform()

# Switch Frame: Cart
def switch_frame_cart(driver):
    try:
        driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "_2DJg7"))
        print("Frame is switched to 'Cart'")
    except NoSuchElementException:
        print("Frame wasn\'t switched")

# Switch Frame: Checkout
def switch_frame_checkout(driver):
    try:
        driver.switch_to.frame(driver.find_element(By.NAME, 'tpaModal_rtby_x2zdo'))
        print("Frame is switched to 'Checkout'")
    except NoSuchElementException:
        print("Frame wasn\'t switched")

# verify Checkout
def checkout_product1(driver):
    try:
        wait = WebDriverWait(driver, 10)
        # Verify that El Photo is Visible
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@data-hook="product-thumbnail-media"]')))
        # Verify that Logo is visible
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@alt="iot_sq.png"]')))
        # verify button "Checkout"
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Checkout']")))
        # Checkout button is clickable
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Checkout']")))
        # # Click on Checkout that verify or is placed !
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Checkout']"))).click()
        print("All Elements is present and 'Checkout' button is OK")
    except NoSuchElementException:
        print("One of El is missed and Checkout is impossible!")



# Locators for Meatball Menu

# Right Arrow ->
right_arrow = '//*[@aria-label="Next video"]'

# Left Arrow <-
left_arrow = '//*[@aria-label="Previous video"]'

# Search Video
search_video = '//*[@class="qa-widget-searchbar FTfKa4 mxefLp f0iqyG className"]'

# Play Videos button
play_videos = '//*[@class="uiWC71"]'

# Main video locator
meatball_main_video = '//*[@class="fHBPfh eSRV3y"]'

# function for Meatball Menu

# Scroll down To Meatball Menu
def scroll_meatball_menu(driver):
    element = driver.find_element(By.XPATH, meatball_main_video)
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

# locators for Upcoming Events

# For button "Event 3"
button_event_3 = '//a[@href="https://qasvus.wixsite.com/ca-marketing/event-info/event-3-1"]' \
                 '[@class="DjQEyU m022zm aUkG34 SJoiX4 It9dDb x8Nx8N IsmYNY"]'
# for Inner Button "Event 3"
inner_button_event_3 = '//*[@data-hook="rsvp-button"][@class="cZcLi2 eLL6c3 _zBlUW L1o1uK GzDYiv K2p6cT"]'
# Text "Event 3"
event_3_text = 'Event 3'
# Photo Locator for "Event 3"
photo_event_3 = '//img[@alt="Event 3"]'

# Time & Location for 'Event 3'
time_location = '//*[@data-hook="time-and-location"]'
# Full Date of 'Event 3'
full_date = '//*[@data-hook="event-full-date"]'

# Function for upcoming Events

# Scroll till 'Upcoming Events'
def scroll_upcoming_events(driver):
    element = driver.find_element(By.XPATH, '//*[@class="tfCiE0"]')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

# Verify That FN, LN, and Email is present and clickable
def regist_field_verification(driver):
    wait = WebDriverWait(driver, 7)
    # Check "First Name" if is Visible and Clickable
    wait.until(EC.visibility_of_element_located((By.ID, 'firstName')))
    wait.until(EC.element_to_be_clickable((By.ID, 'firstName')))
    driver.find_element(By.ID, 'firstName').clear()
    # Check "Last Name" if is Visible and Clickable
    wait.until(EC.visibility_of_element_located((By.ID, 'lastName')))
    wait.until(EC.element_to_be_clickable((By.ID, 'lastName')))
    driver.find_element(By.ID, 'lastName').clear()
    # Check Email field
    wait.until(EC.visibility_of_element_located((By.ID, 'email')))
    wait.until(EC.element_to_be_clickable((By.ID, 'email')))
    driver.find_element(By.ID, 'email').clear()
    # Check if Button "Submit" is visible and clickable
    wait.until(EC.visibility_of_element_located((By.XPATH, submit_button)))
    wait.until(EC.element_to_be_clickable((By.XPATH, submit_button)))

# Create Faker Date for event_3
def create_faker_data_for_event_3(driver):
    driver.find_element(By.ID, 'firstName').send_keys(F.first_name())
    driver.find_element(By.ID, "lastName").send_keys(F.last_name())
    driver.find_element(By.ID, 'email').send_keys(F.email())
    time.sleep(2)
    driver.find_element(By.XPATH, submit_button).click()

# function for Sign up
def sign_up_to_account(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, log_in)))
    wait.until(EC.element_to_be_clickable((By.XPATH, log_in)))
    driver.find_element(By.XPATH, log_in).click()
    assert 'Sign Up' in driver.page_source

# Function for 'Product 1' through the Shop button
def product_1_shop(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.ID, 'comp-ksocy9ii2label')))
    wait.until(EC.element_to_be_clickable((By.ID, 'comp-ksocy9ii2label')))
    print(driver.find_element(By.XPATH, '//a[@href="https://qasvus.wixsite.com/ca-marketing/shop"]').get_attribute("href"))
    driver.find_element(By.ID, 'comp-ksocy9ii2label').click()

