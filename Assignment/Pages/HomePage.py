
class Homepage:

    def __init__(self,Driver):
        self.driver = Driver
        self.scrollDown_execute_script = "window.scrollTo(0, document.body.scrollHeight);"
        self.scrollUp_execute_script = "window.scrollTo(document.body.scrollHeight,0);"
        self.copyright_class_name = 'copyright'
        self.add_post_btn_xpath = '/html/body/nav/div/ul[3]/li[5]/a/span'

    def scroll_Down(self):
        self.driver.execute_script(self.scrollDown_execute_script)

    def check_copyright(self):
        self.driver.find_element_by_class_name(self.copyright_class_name)

    def assert_copyright(self):
        find_copyright = self.driver.find_element_by_class_name(self.copyright_class_name).is_displayed()
        assert find_copyright == True

    def scroll_Up(self):
        self.driver.execute_script(self.scrollUp_execute_script)

    def find_Post_Your_Add_btn(self):
        self.driver.find_element_by_xpath(self.add_post_btn_xpath)

    def assert_Post_Your_Add_btn(self):
        find_post = self.driver.find_element_by_xpath(self.add_post_btn_xpath).is_displayed()
        assert find_post == True

