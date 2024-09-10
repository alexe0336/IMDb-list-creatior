from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time
unadded_titles = [] # List made to store titles that weren't added

# Configuration
IMDB_EMAIL = 'email' # Enter your IMDb account email
IMDB_PASSWORD = 'password' # Enter your IMDb account password
List_Name = 'Temporary Name' # Enter the name you want your IMDb list to have

# Enter movies or tv show titles below in a format like below for best results. 
    # Make sure movie names are separated by a comma. And try to include year.
List_of_titles = [  # Example titles, change to what you want.
    "Maharaja (2024)",
    "Dune: Part Two (2024)",
    "Fargo (1996)",
    "Trainspotting (1996)",
    "Heat (1995)",
    "Toy Story (1995)"
]

def main():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--incognito")  # Open in incognito mode

    driver = webdriver.Chrome()  # Or use Firefox(), Edge(), etc.
    driver.get("https://www.imdb.com")

    # Log in
    xpath = '//*[@id="imdbHeader"]/div[2]/div[5]/a/span'
    element = driver.find_element(By.XPATH, xpath)
    element.click()

    driver.find_element(By.LINK_TEXT, 'Sign in with IMDb').click()

    driver.find_element(By.ID, 'ap_email').send_keys(IMDB_EMAIL)
    driver.find_element(By.ID, 'ap_password').send_keys(IMDB_PASSWORD)
    driver.find_element(By.ID, 'ap_password').send_keys(Keys.RETURN)
    time.sleep(20)

    # Go to your lists
    # Locate the label element using XPath
    user_menu = driver.find_element(By.XPATH, '//*[@id="imdbHeader"]/div[2]/div[5]/div/label[2]/span/span')
    user_menu.click()   # Click on the label element

    your_lists = driver.find_element(By.XPATH, '//*[@id=\"navUserMenu-contents\"]/ul/a[4]/span')
    your_lists.click()

    # Create a new list
    xpath = '//a[@data-testid="list-page-atf-add-to-list-btn"]'
    button = driver.find_element(By.XPATH, xpath)
    button.click()

    input_field = driver.find_element(By.XPATH, '//input[@placeholder="Enter the name of your list"]')
    input_field.send_keys(List_Name)
    print("Title of movie list was entered")

    button = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/section/div/section/div/div[1]/section/button')
    button.click()  # Click the button
    print("Create button was pressed")

    # If it asks for user to login again after creating a list. It was sometimes making user do this in testing.
    try:
        driver.find_element(By.LINK_TEXT, 'Sign in with IMDb')
        print("Re-login required, logging in again...")
        
        xpath = '//*[@id="imdbHeader"]/div[2]/div[5]/a/span'
        element = driver.find_element(By.XPATH, xpath)
        element.click()

        driver.find_element(By.LINK_TEXT, 'Sign in with IMDb').click()

        driver.find_element(By.ID, 'ap_email').send_keys(IMDB_EMAIL)
        driver.find_element(By.ID, 'ap_password').send_keys(IMDB_PASSWORD)
        driver.find_element(By.ID, 'ap_password').send_keys(Keys.RETURN)

    except NoSuchElementException:
        print("No re-login needed.")

    # Loop to Add movies or tv show titles to your IMDb list.
    for title in List_of_titles:
        try:
            driver.execute_script("window.scrollTo(0, 0);") # Scroll to the top of the page
            search_box = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="text-input__1"]'))
            )
            # Click the search box
            search_box.click()
        except TimeoutException as e:
            print(f"TimeoutException: {e} - The search box was not clickable.")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        # Send keys to the search box
        search_box.send_keys(title)

        try:
            # Wait for the dropdown list to appear
            dropdown_list = WebDriverWait(driver,10).until(
                EC.visibility_of_element_located((By.ID, 'react-autowhatever-1'))
            )

            # Locate the first item in the dropdown list
            first_item = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#react-autowhatever-1--item-0'))
            )
            
            # Click the first item
            first_item.click()
            print(f"{title} has been added")
        except Exception as e:
            # If dropdown item click fails, handle the exception
            print(f"{title} was not able to be added to list: {e}")
            unadded_titles.append(title)

            try:
                input_field = driver.find_element(By.XPATH, "//input[@placeholder='Search title to add']")

                #Clear the input field
                input_field.clear()
                input_field.send_keys(Keys.CONTROL + "a")
                input_field.send_keys(Keys.DELETE)

            except Exception as e:
                print(f"An error occurred: {e}")
            


    print("Finished adding titles to IMDb list.")
    if len(unadded_titles) != 0:
        print("The following titles could not be added automatically and will need to be added to your list manually.")
        for title in unadded_titles:
            print(title)
    driver.quit()



if __name__ == "__main__":
    main()
