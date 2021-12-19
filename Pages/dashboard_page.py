from selenium.webdriver.common.by import By

from Pages.base_page import BaseClass
from Utils.logger_utliity import GenerateLog

class DasboardPage(BaseClass):
    bookings_btn = (By.XPATH, "//button[@type='submit']//*[contains(text(), 'Bookings')]")
    add_bookings_btn = (By.XPATH, "//*[contains(text(), 'Add Booking')]")
    quick_booking_text = (By.XPATH, "//*[text()='Quick Booking']")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def bookings(self):
        self.click_element(DasboardPage.bookings_btn)

    def bookings_page(self):
        return self.get_element_text(DasboardPage.add_bookings_btn)

    def click_add_bookings_btn(self):
        self.click_element(DasboardPage.add_bookings_btn)

    def quick_bookings_page(self):
        return self.get_element_text(DasboardPage.quick_booking_text)



