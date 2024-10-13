from selenium.webdriver.common.by import By


class BlogPage:
    sj_blog_header = (By.CSS_SELECTOR,"div.et_pb_text_0 div.et_pb_text_inner h1")
    sj_blog_text = (By.CSS_SELECTOR,"div.et_pb_text_1 div.et_pb_text_inner p")
    sj_blog_text2 = (By.CSS_SELECTOR,"div.et_pb_text_2 div.et_pb_text_inner p")
    sj_blog_image = (By.CSS_SELECTOR,"div.et_pb_image")
    sj_email_field = (By.CSS_SELECTOR,"input#et_pb_signup_email")
    sj_subscribe_btn = (By.CSS_SELECTOR,"a.et_pb_button")
    
    
    def __init__(self, driver) -> None:
        self.driver = driver

    def blog_header(self):
        return self.driver.find_element(*BlogPage.sj_blog_header)
    
    def blog_content(self):
        return self.driver.find_element(*BlogPage.sj_blog_text)
    
    def blog_image(self):
        return self.driver.find_element(*BlogPage.sj_blog_image)
    
    def blog_content_below_image(self):
        return self.driver.find_element(*BlogPage.sj_blog_text2)
    
    def blog_email(self):
        return self.driver.find_element(*BlogPage.sj_email_field)
    
    def blog_subscribe_btn(self):
        return self.driver.find_element(*BlogPage.sj_subscribe_btn)
    