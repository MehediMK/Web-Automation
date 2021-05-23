import re

class SearchProducts:

    def __init__(self,Driver):
        self.driver = Driver
        # list_the_city
        self.city_div_xpath = '/html/body/div[2]/div[2]/div/div[1]/div[2]/div/div[1]'
        self.city_parent_tag_name = 'ul'
        self.city_child_tag_name = 'li'
        self.city_href_link_tag_name = 'a'
        # lowest_product_price
        self.product_parent_class = 'normal--2QYVk'
        self.product_price_class = 'price--3SnqI'
        self.product_title_tag = 'h2'
        self.product_link_tag = 'a'
        self.product_link_href_tag = 'href'
        self.product_lowest_price_link = 'link'
        # post_date_location
        self.post_date_time_class = 'sub-title--37mkY'
        # check_description
        self.post_description_class = 'description-section--oR57b'
        # click_phone_number
        self.product_number_class_name = 'contact-section--1qlvP'
        self.product_get_number_class = 'contact-section--1qlvP'
        # check_phone_valid
        self.phone_location_class = 'contact-section--1qlvP'

    def list_the_city(self):
        city_list = []
        cities_area = self.driver.find_elements_by_xpath(self.city_div_xpath)
        for citycitie_area in cities_area:
            city_ul = citycitie_area.find_elements_by_tag_name(self.city_parent_tag_name)
            for citys_ul in city_ul:
                cities_li = citys_ul.find_elements_by_tag_name(self.city_child_tag_name)
                for citis_a in cities_li:
                    city_list.append(citis_a.find_element_by_tag_name(self.city_href_link_tag_name).text)
        return city_list

    def lowest_product_price(self):
        # this is used for product row
        products = self.driver.find_elements_by_class_name(self.product_parent_class)
        product_title = []
        product_price = []
        product_link = []
        product_list = {}

        # get all product from list: title,price and link
        for product in products:
            p_price = product.find_element_by_class_name(self.product_price_class).text
            price = ''.join(re.findall("[0-9]", p_price[3:].replace(',', '')))
            if price:
                product_title.append(product.find_element_by_tag_name(self.product_title_tag).text)
                product_price.append(int(price))
                product_link.append(product.find_element_by_tag_name(self.product_link_tag).get_attribute(self.product_link_href_tag))
            else:
                pass
        # get all product title,price,link in dictionary
        for i in range(len(product_title)):
            product_list[i] = {'title': product_title[i], 'price': product_price[i], 'link': product_link[i]}

        lowest_price_product = product_price.index(min(product_price))
        self.driver.get(product_list[lowest_price_product][self.product_lowest_price_link])

    def post_date_location(self):
        # Posted on 22 May 8:26 pm, Farmgate, Dhaka or not
        data_time_location = self.driver.find_element_by_class_name(self.post_date_time_class).is_displayed()
        assert data_time_location == True

    def check_description(self):
        # here checked description or not
        post_desc = self.driver.find_element_by_class_name(self.post_description_class).is_displayed()
        assert post_desc == True

    def click_phone_number(self):
        # here click to show phone number
        phone = self.driver.find_element_by_class_name(self.product_number_class_name).is_displayed()
        if phone:
            phone_no = self.driver.find_element_by_class_name(self.product_get_number_class)
            phone_no.click()
        else:
            pass

    def check_phone_valid(self):
        phone_check = self.driver.find_element_by_class_name(self.phone_location_class).is_displayed()
        assert phone_check == True

