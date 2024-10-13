from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
from utilities.BaseClass import BaseClass
from pages.home_page import HomePage
import pytest 

class TestHomePage(BaseClass):
    
    @pytest.fixture(autouse=True)
    def homepage_setup(self):
        # Initialize HomePage object before each test
        self.homePage = HomePage(self.driver)
        
    def test_logo(self):
        logo = self.homePage.logo()
        assert self.is_element_present(logo)
        
    def test_menu_buttons(self):
        
        blog_text = self.homePage.menu_blog().text 
        assert blog_text == "Blog"
        
        contact_text = self.homePage.menu_contact().text 
        assert contact_text == "Contact"
        
    def test_menu_buttons_div(self):
        
        blog_ele = self.homePage.div_blog() 
        assert self.is_element_present(blog_ele)
        
        contact_ele = self.homePage.div_contact() 
        assert self.is_element_present(contact_ele)
        
    def test_hero_header(self):
        # time.sleep(1)
        self.wait_for_element_to_be_visible(self.homePage.sj_hero_header)
        header_text = self.homePage.hero_header().text
        print('header_text', header_text)
        assert header_text =="Jack of All Trades. Master of Some."
        
    def test_contact_me_btn(self):
        self.wait_for_element_to_be_visible(self.homePage.sj_contact_me_btn)
        contact_me_btn_ele = self.homePage.contact_me_btn()
        contact_me_text = contact_me_btn_ele.text
        assert contact_me_text == 'CONTACT ME'
        contact_me_href = contact_me_btn_ele.get_attribute('href')
        assert contact_me_href == "/#contact"
        
    def test_read_blog_btn(self):
        # Wait for the element to be visible
        self.wait_for_element_to_be_visible(self.homePage.sj_read_blog_btn)

        # Locate the 'Read Blog' button element
        read_blog_btn_ele = self.homePage.read_blog_btn()

        # Get the text of the 'Read Blog' button and assert it
        read_blog_text = read_blog_btn_ele.text
        assert read_blog_text == 'READ BLOG'

        # Get the 'href' attribute of the 'Read Blog' button and assert its value
        read_blog_href = read_blog_btn_ele.get_attribute('href')
        assert read_blog_href == "/#blog"

    def test_header_row_one(self):
        self.wait_for_element_to_be_visible(self.homePage.sj_blog_header_row_one)
        self.scroll_to_element(self.homePage.sj_blog_header_row_one)
        header_row_one_ele = self.homePage.header_row_one()
        header_row_one_text = header_row_one_ele.text
        assert header_row_one_text == 'Read All About It'
        
    def test_header_row_three(self):
        self.wait_for_element_to_be_visible(self.homePage.sj_blog_header_row_three)
        self.scroll_to_element(self.homePage.sj_blog_header_row_three)
        header_row_three_ele = self.homePage.header_row_three()
        header_row_three_text = header_row_three_ele.text
        assert header_row_three_text == 'Read All About It'
        
    def test_iframe_board(self):
        original_window = self.homePage.driver.current_window_handle
        print("original_window", original_window)
        # Step 1: Switch to the iframe containing the board
        iframe = self.explicit_wait(By.CLASS_NAME, "trello-board")
        self.homePage.driver.switch_to.frame(iframe)
        
        board_element = self.wait_for_element_to_be_clickable((By.CSS_SELECTOR,"div#board-container trello-board-tile"))
        # board_element.click()
        
        # Step 2: Wait for the board element to be visible
        self.wait_for_element_to_be_visible(self.homePage.sj_board)

        # Step 3: Scroll to the board element if necessary
        self.scroll_to_element(self.homePage.sj_board)

        # Step 4: Retrieve the board element
        board_ele = self.homePage.board()  # Assuming this method returns the board WebElement
        board_ele.click()
        self.homePage.driver.switch_to.default_content()
        # time.sleep(5)
        
        print("driver.window_handles", self.homePage.driver.window_handles)
        new_window = [window for window in self.homePage.driver.window_handles if window != original_window][0]

        # Switch to the new tab
        self.homePage.driver.switch_to.window(new_window)

        # Check if the URL contains 'trello.com'
        if 'trello.com' in self.homePage.driver.current_url:
            print("Successfully navigated to Trello:", self.homePage.driver.current_url)
        else:
            print("Failed to navigate to Trello. Current URL:", self.homePage.driver.current_url)

        # Optionally, switch back to the original tab
        self.homePage.driver.switch_to.window(original_window)
        