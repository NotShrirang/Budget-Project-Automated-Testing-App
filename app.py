import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from tests import *

TEST_DESCRIPTIONS = {
    "Check web page title": ["Verify that a web page title matches an expected value.", first_test],
    "Check presence of Get Started button": ["Verify that a web element is present on a web page.", second_test],
    "Check login without credentials": ["Verify that no login is possible with empty credentials.", third_test],
    "Check login with correct credentials": ["Verify that login is possible with correct credentials.", fourth_test],
    "Check login without username": ["Verify that login is not possible with empty username.", fifth_test],
    "Check login without password": ["Verify that login is not possible with empty password.", sixth_test],
    "Check functionality of Get Started button": ["Verify that website goes to login/register page after clicking on 'Get Started' button.", seventh_test],
    "Check add transaction page": ["Verify that add transaction page is not accessible without login.", eighth_test],
    "Check transaction view page": ["Verify that transaction view page is not accessible without login.", ninth_test],
    "Check that logged in user can logout": ["Verify that logged in user can logout.", tenth_test],
    "Check transaction add page": ["Verify that transaction add page can be accessed by logged in users.", eleventh_test],
    "Check if transaction title is correctly displayed.": ["Verify that transaction title is correctly displayed.", twelveth_test],
    "Check if transaction can be added.": ["Verify that transaction can be added.", thirteenth_test],
    "Check if transaction can be added with empty activity field.": ["Verify that transaction can be added with empty activity field.", fourteenth_test],
    "Check if transaction can be added with empty title field.": ["Verify that transaction can be added with empty title field.", fifteenth_test],
    "Check if transaction can be added with empty amount field.": ["Verify that transaction can be added with empty amount field.", sixteenth_test],
    "Check if HoD can login.": ["Verify that HoD can login.", seventeenth_test],
    "Check if HoD can navigate to transactions page.": ["Verify that HoD can navigate to transactions page.", eighteenth_test],
    "Check if HoD can navigate to activities page.": ["Verify that HoD can navigate to activities page.", nineteenth_test],
    "Check if HoD has option to accept transactions.": ["Verify that HoD has option to accept transactions.", twentieth_test],
    "Check if HoD has option to reject transactions.": ["Verify that HoD has option to reject transactions.", twenty_first_test],
    "Check if HoD can accept transactions.": ["Verify that HoD can accept transactions.", twenty_second_test],
    "Check if HoD can reject transactions.": ["Verify that HoD can reject transactions.", twenty_third_test],
    "Check if HoD can view dashboard computer card.": ["Verify that HoD can view dashboard computer card.", twenty_fourth_test],
    "Check if HoD can view view available, total, spent amount.": ["Verify that HoD can view available, total, spent amount.", twenty_fifth_test],
    "Check if displayed total_amount = available_amount + spent_amount.": ["Verify that total_amount = available_amount + spent_amount.", twenty_sixth_test],
    "Check if Prinicpal can login.": ["Verify that Prinicpal can login.", twenty_seventh_test],
    "Check if Principal can access transactions page.": ["Verify that Principal can access transactions page.", twenty_eighth_test],
    "Check if Principal can access activities page.": ["Verify that Principal can access activities page.", twenty_eighth_test],
}


@st.cache_resource
def get_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument(f'--disable-logging')

    driver = webdriver.Chrome(options=chrome_options)
    return driver


st.set_page_config(page_title="Budget Project Automated Testing App",
                   page_icon=":moneybag:", layout="wide")

st.title("Budget Project Automated Testing App")

selected_test = st.sidebar.selectbox(
    "Select a Test", list(TEST_DESCRIPTIONS.keys()))

all_tests = st.sidebar.button("Run All Tests")

st.write(f"**Test Description:** {TEST_DESCRIPTIONS[selected_test][0]}")

if st.button("Run Test"):
    st.write(f"Running test: {TEST_DESCRIPTIONS[selected_test][0]}")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument(f'--disable-logging')
    driver = webdriver.Chrome(options=chrome_options)
    output = TEST_DESCRIPTIONS[selected_test][1](driver)
    if output:
        st.success("Test passed!")
    else:
        st.error("Test failed!")
    driver.quit()

if all_tests:
    st.write("Running all tests...")
    options = Options()
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = get_driver()
    outputs = []
    for test in TEST_DESCRIPTIONS:
        st.info(f"Running test: {TEST_DESCRIPTIONS[test][0]}")
        output = TEST_DESCRIPTIONS[test][1](driver)
        outputs.append(output)
        if test in ["Check login with correct credentials", "Check transaction add page", "Check if HoD can login."]:
            sign_out_button = driver.find_element(
                By.XPATH, "/html/body/div/div/div[1]/div[1]/div/div[2]/div")
            sign_out_button.click()
            yes_button = driver.find_element(
                By.XPATH, "/html/body/div[2]/div/div[6]/button[1]")
            yes_button.click()
            time.sleep(2)
    driver.quit()

    st.header("Test Plan")
    st.write(
        "The following table shows the test plan for the Budget Management web application.")
    test_results = {
        "Check web page title": "Test Passed" if outputs[0] else "Test Failed",
        "Check presence of Get Started button": "Test Passed" if outputs[1] else "Test Failed",
        "Check login without credentials": "Test Passed" if outputs[2] else "Test Failed",
        "Check login with correct credentials": "Test Passed" if outputs[3] else "Test Failed",
        "Check login without username": "Test Passed" if outputs[4] else "Test Failed",
        "Check login without password": "Test Passed" if outputs[5] else "Test Failed",
        "Check functionality of Get Started button": "Test Passed" if outputs[6] else "Test Failed",
        "Check add transaction page": "Test Passed" if outputs[7] else "Test Failed",
        "Check transaction view page": "Test Passed" if outputs[8] else "Test Failed",
        "Check that logged in user can logout": "Test Passed" if outputs[9] else "Test Failed",
        "Check transaction add page": "Test Passed" if outputs[10] else "Test Failed",
        "Check if transaction title is correctly displayed.": "Test Passed" if outputs[11] else "Test Failed",
        "Check if transaction can be added.": "Test Passed" if outputs[12] else "Test Failed",
        "Check if transaction can be added with empty activity field.": "Test Passed" if outputs[13] else "Test Failed",
        "Check if transaction can be added with empty title field.": "Test Passed" if outputs[14] else "Test Failed",
        "Check if transaction can be added with empty amount field.": "Test Passed" if outputs[15] else "Test Failed",
        "Check if HoD can login.": "Test Passed" if outputs[16] else "Test Failed",
        "Check if HoD can navigate to transactions page.": "Test Passed" if outputs[17] else "Test Failed",
        "Check if HoD can navigate to activities page.": "Test Passed" if outputs[18] else "Test Failed",
        "Check if HoD has option to accept transactions.": "Test Passed" if outputs[19] else "Test Failed",
        "Check if HoD has option to reject transactions.": "Test Passed" if outputs[20] else "Test Failed",
        "Check if HoD can accept transactions.": "Test Passed" if outputs[21] else "Test Failed",
        "Check if HoD can reject transactions.": "Test Passed" if outputs[22] else "Test Failed",
        "Check if HoD can view dashboard computer card.": "Test Passed" if outputs[23] else "Test Failed",
        "Check if HoD can view view available, total, spent amount.": "Test Passed" if outputs[24] else "Test Failed",
        "Check if displayed total_amount = available_amount + spent_amount.": "Test Passed" if outputs[25] else "Test Failed",
        "Check if Prinicpal can login.": "Test Passed" if outputs[26] else "Test Failed",
    }

    df = pd.DataFrame()
    df["Test Name"] = list(test_results.keys())
    df["Test Description"] = [TEST_DESCRIPTIONS[test][0]
                              for test in TEST_DESCRIPTIONS]
    df["Test Result"] = list(test_results.values())
    st.dataframe(df, width=2000)
