from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
from utilities.BaseClass import BaseClass
from pages.blog_page import BlogPage
from pages.home_page import HomePage
import pytest 

class TestBlogPage(BaseClass):
    
    @pytest.fixture(autouse=True)
    def blogPage_setup(self):
        # Initialize HomePage object before each test
        self.blogPage = BlogPage(self.driver)
        self.log = self.getLogger()
        
    def test_view_blog(self):
        homePage=HomePage(self.driver)
        homePage.blog_one().click()
        curr_url = self.blogPage.driver.current_url
        self.log.info(f"Blog Url is : {curr_url}")
        assert "the-true-benefit-of-a-good-education-2" in curr_url
        
    def test_validate_blog_page(self):
        homePage=HomePage(self.driver)
        homePage.blog_one().click()
        blog_header = self.blogPage.blog_header()
        self.log.info(f"Blog header is present : {blog_header}")
        assert self.is_element_present(blog_header)
        blog_content = self.blogPage.blog_content()
        self.log.info(f"Blog content is present : {blog_content}")
        assert self.is_element_present(blog_content)
        blog_image = self.blogPage.blog_image()
        self.log.info(f"Blog image is present : {blog_image}")
        assert self.is_element_present(blog_image)
        blog_content_below_image = self.blogPage.blog_content_below_image()
        self.log.info(f"Blog content below image is present : {blog_content_below_image}")
        assert self.is_element_present(blog_content_below_image)
        blog_email = self.blogPage.blog_email()
        self.log.info(f"Blog email input is present : {blog_email}")
        assert self.is_element_present(blog_email)
        blog_subscribe_btn = self.blogPage.blog_subscribe_btn()
        blog_subscribe_btn_text =blog_subscribe_btn.text
        self.log.info(f"Blog SUBSCRIBE btn text is : {blog_subscribe_btn_text}")
        assert blog_subscribe_btn_text == 'SUBSCRIBE'
        time.sleep(5)
    
    
    def test_navigation_home_page(self):
        homePage=HomePage(self.driver)
        homePage.blog_one().click()
        self.wait_for_element_to_be_visible(homePage.sj_logo)
        self.wait_for_element_to_be_visible(self.blogPage.sj_blog_header)
        homePage.logo().click()
        curr_url = homePage.driver.current_url
        self.log.info(f"Navigated to home page : {curr_url}")
        assert "https://suniljindal.com" in curr_url
        
        
    def test_navigation_blog_menu(self):
        homePage=HomePage(self.driver)
        homePage.blog_one().click()
        self.wait_for_element_to_be_visible(homePage.sj_menu_blog)
        self.wait_for_element_to_be_visible(self.blogPage.sj_blog_header)
        homePage.menu_blog().click()
        curr_url = homePage.driver.current_url
        self.log.info(f"Navigated to blog page : {curr_url}")
        assert "https://suniljindal.com/#blog" in curr_url
        
        
    def test_navigation_contact_menu(self):
        homePage=HomePage(self.driver)
        homePage.blog_one().click()
        self.wait_for_element_to_be_visible(homePage.sj_menu_contact)
        self.wait_for_element_to_be_visible(self.blogPage.sj_blog_header)
        homePage.menu_contact().click()
        curr_url = homePage.driver.current_url
        self.log.info(f"Navigated to contact url : {curr_url}")
        assert "https://suniljindal.com/#contact" in curr_url
        
        
        