from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import TestData, Urls
from locators import Locators


class TestPersonalAccount:
    def test_go_to_personal_account(self, driver):
        driver.get(Urls.LOGIN_URL)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(TestData.EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(
            TestData.CORRECT_PASSWORD
        )
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                Locators.ORDER_BUTTON
            )
        )
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.url_to_be(Urls.PROFILE_URL)
        )

        assert driver.current_url == Urls.PROFILE_URL
        driver.quit()

    def test_go_to_constructor_from_personal_account(self, driver):
        driver.get(Urls.LOGIN_URL)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(TestData.EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(
            TestData.CORRECT_PASSWORD
        )
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                Locators.ORDER_BUTTON
            )
        )
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.url_to_be(Urls.PROFILE_URL)
        )
        driver.find_element(*Locators.CONSTRUCTOR_LINK).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.url_to_be(Urls.MAIN_URL)
        )

        assert driver.current_url == Urls.MAIN_URL
        driver.quit()

    def test_go_to_constructor_by_logo(self, driver):
        driver.get(Urls.LOGIN_URL)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(TestData.EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(
            TestData.CORRECT_PASSWORD
        )
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                Locators.ORDER_BUTTON
            )
        )
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.url_to_be(Urls.PROFILE_URL)
        )
        driver.find_element(*Locators.LOGO_LINK).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.url_to_be(Urls.MAIN_URL)
        )

        assert driver.current_url == Urls.MAIN_URL
        driver.quit()

    def test_logout_from_personal_account(self, driver):
        driver.get(Urls.LOGIN_URL)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(TestData.EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(
            TestData.CORRECT_PASSWORD
        )
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                Locators.ORDER_BUTTON
            )
        )
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()

        logout_button = WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                Locators.LOGOUT_BUTTON
            )
        )
        logout_button.click()

        WebDriverWait(driver, 10).until(
            expected_conditions.url_to_be(Urls.LOGIN_URL)
        )

        assert driver.current_url == Urls.LOGIN_URL
        driver.quit()
