# -*- coding: utf-8 -*-
"""Shallins_Grocery_Webscrapping.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hv7Nt-uoOIVnepq_hWPSL_BeiyOH5eKn
"""

#from bs4 import BeautifulSoup
# import requests
# page = requests.get("https://www.shaalis.com/product-category/fresh-fruit-vegetable-herbs/")
# soup = BeautifulSoup(page.content, 'html.parser')
# productlist = soup.find_all("div",{"class":"product-grid-item"})

# import json
# data = []
# for p in productlist:
#     d = {}
#     d['Product_img_url'] = p.find("a",{"class":"product-image-link"}).img.get('src')
#     d['Product_name'] = p.find("h3",{"class":"product-title"}).a.string
#     d['Product_url'] = p.find("a",{"class":"product-image-link"}).get('href')
#     d['Product_Price'] = p.find("span",{"class":"woocommerce-Price-amount"}).bdi.text
    
#     data.append(d)

# print(json.dumps(data,separators=(',',':')))

# df = pd.DataFrame(data)
# print(df)

#  df.to_csv(r'C:/Users/lenovo/Desktop/fresh_fruit_vegetable.csv', index = False)





"""### Slenium

"""

import time
from selenium.webdriver.common.action_chains import ActionChains
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver_path  = 'C:/Users/lenovo/chromedriver.exe'
browser = webdriver.Chrome(driver_path)

from bs4 import BeautifulSoup
import requests

#changes

# Feature added by joy

soup = BeautifulSoup(browser.page_source, 'html.parser')



import pandas as pd

# df.to_csv(r'C:/Users/lenovo/Desktop/All_fresh_fruit_vegetable.csv', index = False)

# def get_all_Fresh_Fruits:
#     browser.get("https://www.shaalis.com/product-category/fresh-fruit-vegetable-herbs/")
#     time.sleep(1)
#     elem = browser.find_element_by_tag_name("body")

#     no_of_pagedowns = 20
#     browser.find_element_by_class_name('mfp-close').click()
#     while no_of_pagedowns:
#         elem.send_keys(Keys.PAGE_DOWN)
#         time.sleep(0.2)
#         no_of_pagedowns-=1
    
        
#     productlist = soup.find_all("div",{"class":"product-grid-item"})
#     import json
#     data = []
#     for p in productlist:
#         d = {}
#         d['Product_img_url'] = p.find("a",{"class":"product-image-link"}).img.get('src')
#         d['Product_name'] = p.find("h3",{"class":"product-title"}).a.string
#         d['Product_url'] = p.find("a",{"class":"product-image-link"}).get('href')
#         d['Product_Price'] = p.find("span",{"class":"woocommerce-Price-amount"}).bdi.text
#         data.append(d) 
        
#     return data

class Categories:
    def __init__(self):
        self.categories = []
        self.cat()
    def cat(self):
        browser.get("https://www.shaalis.com/")
        time.sleep(1)                                                                                                            #  Ek sec ka delay for loading website
        elem = browser.find_element_by_tag_name("body")                                     

        browser.find_element_by_class_name('mfp-close').click()
        
        element_to_hover_over = browser.find_element_by_class_name("menu-opener")

        hover = ActionChains(browser).move_to_element(element_to_hover_over)
        hover.perform()
        time.sleep(1)
        categorylist = browser.find_element_by_id("menu-testmenu")
        items = categorylist.find_elements_by_tag_name("li")
        for i in items:
            url = i.find_elements_by_tag_name("a")[0].get_attribute('href')
            self.categories.append(url) if url != None else None
        print(self.categories)
        
    def goToCategory(self):
        for _c in self.categories:
            print(_c,"\n")
            if "product-category" in _c:
                print(self.getProductCategory(_c))
            elif "product" in _c:
                self.getProduct(_c)
            time.sleep(3)
            
    def getProduct(self,path):
        print("Product")
    def getProductCategory(self,path):
        page = requests.get(path)
        soup = BeautifulSoup(page.content, 'html.parser')
        browser.get(path)
        time.sleep(1)
        elem = browser.find_element_by_tag_name("body")

        no_of_pagedowns = 20
#         browser.find_element_by_class_name('mfp-close').click()
        while no_of_pagedowns:
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.2)
            no_of_pagedowns-=1


        productlist = soup.find_all("div",{"class":"product-grid-item"})
        data = []
        for p in productlist:
            d = {}
            d['Product_img_url'] = p.find("a",{"class":"product-image-link"}).img.get('src')
            d['Product_name'] = p.find("h3",{"class":"product-title"}).a.string
            d['Product_url'] = p.find("a",{"class":"product-image-link"}).get('href')
            d['Product_Price'] = p.find("span",{"class":"woocommerce-Price-amount"}).bdi.text
            data.append(d) 
        
        df = pd.DataFrame(data)
        name = 'C:/Users/lenovo/Desktop/All_Category_Products_Shallins/{fileName}.csv'
        df.to_csv(name.format(fileName = path[41:].replace('/','')), index = False)
        return "Added in csv file"

        
c = Categories()
c.goToCategory()



