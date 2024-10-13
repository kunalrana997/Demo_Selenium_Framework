from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class HomePage:
    
    sj_logo = (By.CSS_SELECTOR,"header#main-header img[src*='logo.png']")
    sj_menu_blog = (By.CSS_SELECTOR,"ul#top-menu a[href='/#blog']")
    sj_div_blog = (By.CSS_SELECTOR,"div#blog")
    sj_div_contact = (By.CSS_SELECTOR,"div#contact")
    sj_menu_contact = (By.CSS_SELECTOR,"ul#top-menu a[href='/#contact']")
    sj_hero_header = (By.CSS_SELECTOR,"div.header-content h1")
    sj_read_blog_btn = (By.CSS_SELECTOR,"a.et_pb_button_one")
    sj_contact_me_btn = (By.CSS_SELECTOR,"a.et_pb_button_two")
    sj_blog_header_row_one = (By.CSS_SELECTOR,"div#blog div.et_pb_row_1 div h1")
    sj_blog_header_row_three = (By.CSS_SELECTOR,"div#blog div.et_pb_row_3 div h1")
    sj_iframe_board = (By.CSS_SELECTOR,"iframe.trello-board")
    sj_board = (By.CSS_SELECTOR,"div#board-container trello-board-tile")
    sj_board_anchor = (By.CSS_SELECTOR,"div#board-container trello-board-tile a")
    sj_article_one = (By.CSS_SELECTOR,"article#post-343")
    
    def __init__(self, driver) -> None:
        self.driver = driver
        
    def logo(self):
        return self.driver.find_element(*HomePage.sj_logo)
    
    def menu_blog(self):
        return self.driver.find_element(*HomePage.sj_menu_blog)
    
    def menu_contact(self):
        return self.driver.find_element(*HomePage.sj_menu_contact)
    
    def div_blog(self):
        return self.driver.find_element(*HomePage.sj_div_blog)
    
    def div_contact(self):
        try: 
            self.driver.find_element(*HomePage.sj_div_contact)
            # self.driver.find_element(*locator)
            print("div_contact True")
            return True
        except NoSuchElementException as e:
            print("div_contact False")
            print(f"Error: {e}")

        # return self.driver.find_element(*HomePage.sj_div_contact)
    
    def hero_header(self):
        return self.driver.find_element(*HomePage.sj_hero_header)
    
    def read_blog_btn(self):
        return self.driver.find_element(*HomePage.sj_read_blog_btn)
    
    def contact_me_btn(self):
        return self.driver.find_element(*HomePage.sj_contact_me_btn)
    
    def header_row_one(self):
        return self.driver.find_element(*HomePage.sj_blog_header_row_one)
    
    def header_row_three(self):
        return self.driver.find_element(*HomePage.sj_blog_header_row_three)
    
    def blog_overview(self):
        return self.driver.find_element(HomePage.sj_article_one)
    
    def board(self):
        return self.driver.find_element(*HomePage.sj_board)
    
    def blog_one(self):
        return self.driver.find_element(*HomePage.sj_article_one)
    
    
    