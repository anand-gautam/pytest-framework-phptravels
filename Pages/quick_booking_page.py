from selenium.webdriver.common.by import By
from Pages.base_page import BaseClass
from Utils.logger_utliity import GenerateLog
import time

class QuickBooking(BaseClass):

    service_type = (By.ID, "servicetype")
    customer_type = (By.ID, "selusertype")
    customer_email = (By.CLASS_NAME, "select2-chosen")
    from_date_picker = (By.XPATH, "//*[contains(@class, 'checkinlabel')]//*[@id='Hotels']")
    date_picker = (By.XPATH, "//*[@class='datepicker dropdown-menu']")
    date_day = (By.XPATH, "//*[@class='datepicker-days']//*[@class='day ']")
    lbl_checkout = (By.XPATH, "//*[text()='Check-Out ']")
    to_date_picker = (By.XPATH, "//*[@class='form-group']//*[@name='checkout']")
    select_hotel = (By.XPATH, "//*[text()='Hotel Name']/..//select")
    select_room = (By.XPATH, "//*[text()='Room Name']/..//select")
    room_count = (By.XPATH, "//select[@name='roomscount']")
    total_room_price = "totalroomprice"
    per_night_price = "roomtotal"
    price_type = "price_type"
    vat_tax = "taxhotel"
    b2c_markup_pct = "b2c_markup"
    total_adults = (By.ID, "adultscount")
    total_children = (By.ID, "childcount")
    deposit_amt = "totaltopay"
    payment_method = (By.XPATH, "//*[@name='paymethod']")
    btn_book_now = (By.XPATH, "//*[@value='Book Now']")
    bookings_view_page = (By.XPATH, "//div[text()='Bookings View']")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def select_service_type(self, option_text):
        self.select_option_by_text(QuickBooking.service_type, option_text)

    def booking_by_registered_customer(self, customer_type_option):
        self.select_option_by_text(QuickBooking.customer_type, customer_type_option)

    def customer_email_id(self):
        self.wait_for(QuickBooking.customer_email)
        return self.get_element_text(QuickBooking.customer_email)


    # def pick_from_date(self, date_value):
    #     self.wait_for(QuickBooking.from_date_picker)
    #     self.click_element(QuickBooking.from_date_picker)
    #     self.wait_for(QuickBooking.date_picker)
    #     all_dates = self.find_elements(QuickBooking.date_day)
    #     for date in all_dates:
    #         date_txt = date.text
    #         if date_txt == date_value:
    #             date.click()
    #             break

    def pick_from_date(self, date_text):
        self.wait_for(QuickBooking.from_date_picker)
        self.type_text(QuickBooking.from_date_picker, date_text)
        self.click_element(QuickBooking.lbl_checkout)

    def pick_to_date(self, date_text):
        self.wait_for(QuickBooking.from_date_picker)
        self.type_text(QuickBooking.to_date_picker, date_text)
        self.click_element(QuickBooking.lbl_checkout)

    def select_hotel_name(self, hotel_name):
        self.select_option_by_text(QuickBooking.select_hotel, hotel_name)

    def select_room_type(self, room_type):
        time.sleep(1)
        self.select_option_by_text(QuickBooking.select_room, room_type)

    def select_required_rooms(self, req_rooms):
        time.sleep(1)
        self.select_option_by_text(QuickBooking.room_count, req_rooms)

    def price_for_rooms(self):
        return self.driver.execute_script(f"return document.getElementById('{QuickBooking.total_room_price}').value")

    def price_per_night(self):
        return self.driver.execute_script(f"return document.getElementById('{QuickBooking.per_night_price}').value")

    def type_of_room_price(self):
        return self.driver.execute_script(f"return document.getElementById('{QuickBooking.price_type}').value")

    def added_vat(self):
        return self.driver.execute_script(f"return document.getElementById('{QuickBooking.vat_tax}').value")

    def added_b2c_markup(self):
        return self.driver.execute_script(f"return document.getElementById('{QuickBooking.b2c_markup_pct}').value")

    def select_adults(self, adults_count):
        self.select_option_by_text(QuickBooking.total_adults, adults_count)

    def select_children(self, child_count):
        self.select_option_by_text(QuickBooking.total_children, child_count)

    def total_to_pay(self):
        return self.driver.execute_script(f"return document.getElementById('{QuickBooking.deposit_amt}').value")

    def select_pay_method(self, payment_mode):
        self.select_option_by_text(QuickBooking.payment_method, payment_mode)

    def click_btn_book_now(self):
        self.click_element(QuickBooking.btn_book_now)
        self.wait_for(QuickBooking.bookings_view_page)

    def redirect_to_dashboard_page(self):
        return self.get_element_text(QuickBooking.bookings_view_page)






