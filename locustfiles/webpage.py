import datetime
import requests
import re
import mysql.connector
import json
from lxml import html
import os
import time
from locust import HttpUser, task, between
from locustfiles import csvLibrary
from locustfiles.csvLibrary import CsvLibrary


class QuickstartUser(HttpUser):
    csv_reader = CsvLibrary('./csv_example/mysql.csv', './csv_example/test_variables.csv')
    mysql_data = csv_reader.read_mysql_csv()
    data = csv_reader.read_test_variable(1)

    wait_time = between(1, 2)

    HEADER_SEARCH_RESULT_PAGE_XPATH = data[1]
    FIRST_ITEM_LINK_IN_SEARCH_RESULT_XPATH = data[2]
    LINK_TO_PRODUCT = data[3]
    product_name = data[4]
    id_product = data[5]
    id_customization = data[6]
    token = ""
    url_image = data[7]
    conn = mysql.connector.connect(user='root', password='admin', host="127.0.0.1", port=3307, database='prestashop', ssl_disabled = True)
    cursor = conn.cursor()    

    @task
    def index_page(self):
        response = self.client.get(self.data[0])
        assert response.status_code == 200
        assert response.elapsed < datetime.timedelta(seconds = 3), "Request took more than 3 seconds"
        

    @task
    def search_item(self):
        response = self.client.get("/vyhledavani?controller=search&s=Shirt")
        time.sleep(1)
        assert response.status_code == 200
        assert response.elapsed < datetime.timedelta(seconds = 3), "Request took more than 3 seconds"
        tree = html.fromstring(response.text)        
        # print(tree.xpath(self.HEADER_SEARCH_RESULT_PAGE_XPATH))
        assert tree.xpath(self.HEADER_SEARCH_RESULT_PAGE_XPATH)[0] == "Výsledek hledání" , "Check header in search result"
        # print(tree.xpath(self.FIRST_ITEM_LINK_IN_SEARCH_RESULT_XPATH)[0])
        #TODO dynamic get URL for first product in search result,  xpath:         

    @task
    def get_detail_product(self):
        response = self.client.get(self.LINK_TO_PRODUCT)
        assert response.status_code == 200
        assert response.elapsed < datetime.timedelta(seconds = 3), "Request took more than 3 seconds"
        tree = html.fromstring(response.text)
        assert tree.xpath('//h1/text()')[0] == "Hummingbird printed t-shirt", "H1 text on product detail"
        self.product_name = tree.xpath('//h1/text()')[0]
        self.url_image = tree.xpath('//div[@class="product-cover"]/img/@src')[0]
        print(self.url_image)
        self.token = tree.xpath('//form[@id="add-to-cart-or-refresh"]/input[@name="token"]/@value')[0]
        self.id_product = tree.xpath('//form[@id="add-to-cart-or-refresh"]/input[@name="id_product"]/@value')[0]
        self.id_customization = tree.xpath('//form[@id="add-to-cart-or-refresh"]/input[@name="id_customization"]/@value')[0]

    @task
    def check_detail_image(self):
        r = requests.get(self.url_image, allow_redirects=True)
        open('detail.jpg', 'wb').write(r.content)
        os.system('.\exif_example\exiftool.exe .\detail.jpg -json -textout .json')
        with open('./detail.json') as f:
            data = json.load(f)
        image_size = data[0]['ImageSize']
        # print(image_size)
        assert image_size=="458x458", "Check EXIF information from downloaded image"

    @task
    def add_to_cart(self):
        payload = {
            "token": self.token,
            "id_product": self.id_product,
            "id_customization": self.id_customization,
            "group[1]": 1,
            "group[2]": 8,
            "qty": 1,
            "add": 1,
            "action": "update"
        }
        #print("Payload: " + payload)
        response = self.client.post("/kosik", data=payload)

    @task
    def check_cart_SQL(self):
        sql = '''select * from ps_cart order by id_cart desc'''
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        # print(result[0])
        # print("ID cart:" + str(result[0][0]))
        sql = """
            select ps_product_lang.name,ps_product_lang.description_short,ps_cart_product.*,ps_product.price 
            from ps_cart_product 
            join ps_product ON ps_cart_product.id_product=ps_product.id_product
            join ps_product_lang ON ps_cart_product.id_product=ps_product_lang.id_product
            where ps_cart_product.id_cart=""" + str(result[0][0])
        # print(sql)
        cursor2 = self.conn.cursor()
        cursor2.execute(sql)
        result = cursor2.fetchone()
        # print(result)
        # print("Name product: " + result[0])
        assert result[0]==self.product_name, "Check product name from DB from cart"

    def on_start(self):        
        print('Start of testing ...')
 

    def on_stop(self):
        # print('End of testing ...')
        self.conn.close()