from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import TestData, Urls
from generators import generate_email, generate_password
from locators import Locators


class TestRegistration:
    def test_successful_registration(self, driver):
        email = generate_email()
        password = generate_password()

        driver.get(Urls.REGISTRATION_URL)
        driver.find_element(*Locators.REGISTRATION_NAME_INPUT).send_keys(
            TestData.USER_NAME
        )
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.url_to_be(Urls.LOGIN_URL)
        )

        assert driver.current_url == Urls.LOGIN_URL
        driver.quit()

    def test_registration_with_incorrect_password(self, driver):
        email = generate_email()

        driver.get(Urls.REGISTRATION_URL)
        driver.find_element(*Locators.REGISTRATION_NAME_INPUT).send_keys(
            TestData.USER_NAME
        )
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(
            TestData.INCORRECT_PASSWORD
        )
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        error = WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                Locators.INCORRECT_PASSWORD_ERROR
            )
        )

        assert error.text == TestData.INCORRECT_PASSWORD_ERROR
        driver.quit()
