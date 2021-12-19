import pytest

from ConfigurationData.config_reader import read_config
from Pages.admin import Admin
from Pages.dashboard_page import DasboardPage
from Pages.quick_booking_page import QuickBooking
from Tests.base_test import BaseTest
from Utils.logger_utliity import GenerateLog
import time


class TestAdmin(BaseTest):
    logger = GenerateLog.create_log()

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_login_to_admin(self):
        admin = Admin(self.driver)
        self.logger.info("test_login_to_admin: Test Begins")
        self.driver.get(read_config("basic info", "admin_url"))
        admin.admin_email()
        admin.admin_password()
        admin.admin_login_btn()
        admin.wait_for_dashboard()
        time.sleep(3)
        actual_title = self.driver.title
        expected_title = "Dashboard"
        assert actual_title == expected_title, "Not logged in"
        self.logger.info("test_login_to_admin: End of Test")

    @pytest.mark.regression
    def test_bookings_page(self):
        dashboard = DasboardPage(self.driver)
        self.logger.info("test_bookings_page: Test begins")
        dashboard.bookings()
        bookings_page_assert = dashboard.bookings_page().strip()
        assert bookings_page_assert == 'Add Booking', "Not in the Bookings page"
        self.logger.info("test_bookings_page: End of Test")

    @pytest.mark.regression
    def test_add_booking(self):
        dasboard = DasboardPage(self.driver)
        self.logger.info("test_add_bookinge: Test begins")
        self.logger.info("test_add_bookinge: clicking on Add Booking button")
        dasboard.click_add_bookings_btn()
        self.logger.info("test_add_bookinge: clicked on Add Booking button")
        quick_booking_assert = dasboard.quick_bookings_page().strip()
        assert quick_booking_assert == "QUICK BOOKING", "Not in Quick Booking page"
        self.logger.info("test_add_bookinge: End of Test")

    @pytest.mark.regression
    def test_quick_booking(self):
        quick_booking = QuickBooking(self.driver)
        self.logger.info("test_quick_booking: Test Begins")
        quick_booking.select_service_type("Hotels")
        quick_booking.booking_by_registered_customer("Registered")

        cust_email_txt = quick_booking.customer_email_id()
        self.logger.info(cust_email_txt)
        quick_booking.pick_from_date('21/12/2021')
        quick_booking.pick_to_date('22/12/2021')
        quick_booking.select_hotel_name('Rendezvous Hotels')
        quick_booking.select_room_type('One-Bedroom Apartment')
        quick_booking.select_required_rooms('2')
        total_room_price = quick_booking.price_for_rooms()
        self.logger.info('Total room price: %s', total_room_price)
        room_price_per_night = quick_booking.price_per_night()
        self.logger.info('Price of roo per night: %s', room_price_per_night)
        room_price_type = quick_booking.type_of_room_price()
        self.logger.info('Type of romm price: %s', room_price_type)
        with_vat = quick_booking.added_vat()
        self.logger.info('+ VAT: %s', with_vat)
        with_b2c_markup = quick_booking.added_b2c_markup()
        self.logger.info('+ b2c Markup: %s', with_b2c_markup)
        quick_booking.select_adults('2')
        quick_booking.select_children('2')
        price_to_pay = quick_booking.total_to_pay()
        self.logger.info('Price to pay: %s', price_to_pay)
        quick_booking.select_pay_method('Bank Transfer')
        self.logger.info('Booking now')
        quick_booking.click_btn_book_now()
        dashboard_page = quick_booking.redirect_to_dashboard_page()
        assert dashboard_page == 'BOOKINGS VIEW', 'Not in dashboard page'
        self.logger.info('Booking complete')

        self.logger.info("test_quick_booking: End of Test")
