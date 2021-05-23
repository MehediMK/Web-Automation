
class OpenLinkPage:

    def __init__(self,Driver):
        self.driver = Driver
        self.page_scroll_script = "window.scrollTo(0, document.body.scrollHeight);"
        # assert_copyright
        self.copyright_xpath = '//*[@id="app-wrapper"]/div[1]/div[6]/div/div/div/div[3]/div[1]'
        self.copyright_text = 'Copyright Not Found'
        # open_link
        self.link_li_tag = 'li'
        self.link_a_tag = 'a'
        self.link_href_attribute = 'href'


    def scrollDown(self):
        self.driver.execute_script(self.page_scroll_script)

    def assert_copyright(self):
        copyright = self.driver.find_element_by_xpath(self.copyright_xpath).is_displayed()
        assert copyright == True, self.copyright_text

    def open_all_link(self,xpath):
        link_list = []
        links_ul = self.driver.find_elements_by_xpath(xpath)
        for links in links_ul:
            links_li = links.find_elements_by_tag_name(self.link_li_tag)
            for link_a in links_li:
                link = link_a.find_element_by_tag_name(self.link_a_tag).get_attribute(self.link_href_attribute)
                link_list.append(link)

        for link_open in link_list:
            self.driver.get(link_open)

