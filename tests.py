from colorama import Fore, Back, Style
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
from dotenv import load_dotenv
load_dotenv()

BASEURL = "http://localhost:5173"

def first_test(driver):
    '''
    Verify that a web page title matches an expected value.
    '''
    driver.get(BASEURL)
    title = driver.title
    if title == "MMCOE: Budget Management Application":
        print(Fore.GREEN + "Test passed" + Style.RESET_ALL)
        return True
    else:
        print(Fore.RED + "Test failed" + Style.RESET_ALL)
        return False
    

def second_test(driver):
    '''
    Verify that a web element is present on a web page.
    '''
    driver.get(BASEURL)
    try:
        element = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[2]/button")
        if element:
            print(Fore.GREEN + "Test passed" + Style.RESET_ALL)
            return True
        else:
            print(Fore.RED + "Test failed" + Style.RESET_ALL)
            return False
    except Exception as e:
        print(Fore.RED + f"Test failed with exception: {e.msg}" + Style.RESET_ALL)
        return False
    

def third_test(driver):
    '''
    Verify that no login is possible with empty credentials.
    '''
    driver.get(f"{BASEURL}/login")
    email_field = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[1]/form/div[1]/input")
    password_field = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[1]/form/div[2]/input")
    email_field.send_keys("")
    password_field.send_keys("")

    login_button = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[1]/form/button")
    login_button.click()
    expected_url = f"{BASEURL}/transactions"
    try:
        WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print(Fore.RED + "Test failed" + Style.RESET_ALL)
            return False
        else:
            print(Fore.GREEN + "Test passed" + Style.RESET_ALL)
            return True
    except Exception as e:
        print(Fore.GREEN + f"Test passed" + Style.RESET_ALL)
        return True
    

def fourth_test(driver):
    '''
    Verify that login is possible with correct credentials.
    '''
    driver.get(f"{BASEURL}/login")
    email_field = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[1]/form/div[1]/input")
    password_field = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[1]/form/div[2]/input")
    email_field.send_keys(os.getenv("BUDGET_PROJECT_USERNAME"))
    password_field.send_keys(os.getenv("BUDGET_PROJECT_PASSWORD"))

    login_button = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[1]/form/button")
    login_button.click()
    expected_url = f"{BASEURL}/transactions"
    try:
        WebDriverWait(driver, 20).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print(Fore.GREEN + "Test passed" + Style.RESET_ALL)
            return True
        else:
            print(Fore.RED + "Test failed" + Style.RESET_ALL)
            return False
    except Exception as e:
        print(Fore.RED + f"Test failed because of unexpected result" + Style.RESET_ALL)
        return False
    

def fifth_test(driver):
    '''
    Verify that login is not possible with empty username.
    '''
    driver.get(f"{BASEURL}/login")
    email_field = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[1]/form/div[1]/input")
    password_field = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[1]/form/div[2]/input")
    email_field.send_keys("")
    password_field.send_keys(os.getenv("BUDGET_PROJECT_PASSWORD"))

    login_button = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[1]/form/button")
    login_button.click()
    expected_url = f"{BASEURL}/account"
    try:
        WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print(Fore.RED + "Test failed" + Style.RESET_ALL)
            return False
        else:
            print(Fore.GREEN + "Test passed" + Style.RESET_ALL)
            return True
    except Exception as e:
        print(Fore.GREEN + f"Test passed" + Style.RESET_ALL)
        return True


def sixth_test(driver):
    '''
    Verify that login is not possible with empty password.
    '''
    driver.get(f"{BASEURL}/login")
    email_field = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[1]/form/div[1]/input")
    password_field = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[1]/form/div[2]/input")
    email_field.send_keys(os.getenv("BUDGET_PROJECT_USERNAME"))
    password_field.send_keys("")

    login_button = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[1]/form/button")
    login_button.click()
    expected_url = f"{BASEURL}/account"
    try:
        WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print(Fore.RED + "Test failed" + Style.RESET_ALL)
            return False
        else:
            print(Fore.GREEN + "Test passed" + Style.RESET_ALL)
            return True
    except Exception as e:
        print(Fore.GREEN + f"Test passed" + Style.RESET_ALL)
        return True


def seventh_test(driver):
    '''
    Verify that website goes to login/register page after clicking on "Get Started" button.
    '''
    driver.get(BASEURL)
    get_started_button = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[2]/button")
    get_started_button.click()
    expected_url = f"{BASEURL}/login"
    try:
        WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print(Fore.GREEN + "Test passed" + Style.RESET_ALL)
            return True
        else:
            print(Fore.RED + "Test failed" + Style.RESET_ALL)   
            return False
    except Exception as e:
        print(Fore.RED + f"Test failed because of unexpected result" + Style.RESET_ALL)
        return False


def eighth_test(driver):
    '''
    Verify that add transaction page is not accessible.
    '''
    try:
        driver.get(f"{BASEURL}/transactions/add")
        redirected_url = WebDriverWait(driver, 5).until(
            EC.url_matches(BASEURL+"/login")
        )

        if redirected_url:
            print(Fore.GREEN + "Test passed: Redirects to login page." + Style.RESET_ALL)
            return True
        else:
            print(Fore.RED + f"Test failed - Redirected to: {BASEURL}/transactions/add" + Style.RESET_ALL)
            return False
    except Exception as e:
        print(Fore.RED + f"Test failed because of unexpected error: {e}" + Style.RESET_ALL)
        return False


def ninth_test(driver):
    '''
    Verify that transactions page is not accessible without login.
    '''
    try:
        driver.get(f"{BASEURL}/transactions/")
        redirected_url = WebDriverWait(driver, 5).until(
            EC.url_matches(BASEURL+"/login")
        )

        if redirected_url:
            print(Fore.GREEN + "Test passed" + Style.RESET_ALL)
            return True
        else:
            print(Fore.RED + f"Test failed - Redirected to: {BASEURL}/transactions/add" + Style.RESET_ALL)
            return False
    except Exception as e:
        print(Fore.RED + f"Test failed because of unexpected error: {e}" + Style.RESET_ALL)
        return False

def tenth_test(driver):
    '''
    Verify that logged in user can logout.
    '''
    if fourth_test(driver):
        time.sleep(2)
        sign_out_button = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[1]/div/div[2]/div")
        sign_out_button.click()
        yes_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[6]/button[1]")
        yes_button.click()
        expected_url = f"{BASEURL}/login"
        try:
            WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))
            if driver.current_url == expected_url:
                print(Fore.GREEN + "Test passed" + Style.RESET_ALL)
                return True
            else:
                print(Fore.RED + "Test failed" + Style.RESET_ALL)
                return False
        except Exception as e:
            print(Fore.RED + f"Test failed because of unexpected result" + Style.RESET_ALL)
            return False
    else:
        print(Fore.RED + f"Test failed because of wrong login credentials" + Style.RESET_ALL)
        return False

def eleventh_test(driver):
    '''
    Verify that only logged in user can add transaction.
    '''
    if fourth_test(driver):
        add_button = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]")
        add_button.click()
        expected_url = f"{BASEURL}/transactions/add"
        try:
            WebDriverWait(driver, 20).until(EC.url_to_be(expected_url))
            if driver.current_url == expected_url:
                print(Fore.GREEN + "Test passed" + Style.RESET_ALL)
                return True
            else:
                print(Fore.RED + "Test failed" + Style.RESET_ALL)
                return False
        except Exception as e:
            print(Fore.RED + f"Test failed because of unexpected result" + Style.RESET_ALL)
            return False
    else:
        print(Fore.RED + f"Test failed because of wrong login credentials" + Style.RESET_ALL)
        return False

def twelveth_test(driver):
    '''
    Verify that transaction title is correctly displayed.
    '''
    if fourth_test(driver):
        datagrid_title_element = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[2]/div[2]/div/div[1]/div[3]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div")
        datagrid_title = datagrid_title_element.text
        datagrid_row = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[2]/div[2]/div/div[1]/div[3]/div/div/div[1]/div[2]/div/div/div[1]")
        actionChains = ActionChains(driver)
        actionChains.double_click(datagrid_row).perform()
        transaction_title_element = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[1]/div[1]")
        transaction_title = transaction_title_element.text
        try:
            if datagrid_title == transaction_title:
                print(Fore.GREEN + "Test passed" + Style.RESET_ALL)
                return True
            else:
                print(Fore.RED + "Test failed" + Style.RESET_ALL)
                return False
        except Exception as e:
            print(Fore.RED + f"Test failed because of unexpected result" + Style.RESET_ALL)
            return False
    else:
        print(Fore.RED + f"Test failed because of wrong login credentials" + Style.RESET_ALL)
        return False

if __name__ == "__main__":
    driver = webdriver.Chrome()
    first_test(driver)
    second_test(driver)
    third_test(driver)
    fourth_test(driver)
    fifth_test(driver)
    sixth_test(driver)
    seventh_test(driver)
    eighth_test(driver)
    ninth_test(driver)
    tenth_test(driver)
    eleventh_test(driver)
    twelveth_test(driver)
    driver.quit()