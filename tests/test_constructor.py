from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import Urls
from locators import Locators


class TestConstructor:
    def test_go_to_buns_tab(self, driver):
        driver.get(Urls.MAIN_URL)
        sauces_tab = WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(Locators.SAUCES_TAB)
        )
        sauces_tab.click()

        WebDriverWait(driver, 10).until(
            expected_conditions.text_to_be_present_in_element(
                Locators.ACTIVE_CONSTRUCTOR_TAB, "Соусы"
            )
        )
        driver.find_element(*Locators.BUNS_TAB).click()

        active_tab = WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                Locators.ACTIVE_CONSTRUCTOR_TAB
            )
        )

        assert active_tab.text == "Булки"
        driver.quit()

    def test_go_to_sauces_tab(self, driver):
        driver.get(Urls.MAIN_URL)
        sauces_tab = WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(Locators.SAUCES_TAB)
        )
        sauces_tab.click()

        WebDriverWait(driver, 10).until(
            expected_conditions.text_to_be_present_in_element(
                Locators.ACTIVE_CONSTRUCTOR_TAB, "Соусы"
            )
        )
        active_tab = WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                Locators.ACTIVE_CONSTRUCTOR_TAB
            )
        )

        assert active_tab.text == "Соусы"
        driver.quit()

    def test_go_to_fillings_tab(self, driver):
        driver.get(Urls.MAIN_URL)
        fillings_tab = WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(Locators.FILLINGS_TAB)
        )
        fillings_tab.click()

        WebDriverWait(driver, 10).until(
            expected_conditions.text_to_be_present_in_element(
                Locators.ACTIVE_CONSTRUCTOR_TAB, "Начинки"
            )
        )
        active_tab = WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                Locators.ACTIVE_CONSTRUCTOR_TAB
            )
        )

        assert active_tab.text == "Начинки"
        driver.quit()
