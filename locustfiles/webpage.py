import datetime
import requests
import re
import mysql.connector
import json
from lxml import html
import os
import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)
    FIRST_ITEM_IN_SEARCH_RESULT_XPATH = '//div[@id="js-product-list"]/div/article[1]//h2/a'
    #conn = mysql.connector.connect(user='root', password='admin', host='127.0.0.1:3306', database='prestashop')
    #cursor = conn.cursor()    

    @task
    def index_page(self):
        response = self.client.get("/")
        assert response.status_code == 200
        assert response.elapsed < datetime.timedelta(seconds = 3), "Request took more than 3 seconds"
        

    @task
    def search_item(self):
        response = self.client.get("/vyhledavani?controller=search&s=Shirt")
        time.sleep(1)
        assert response.status_code == 200
        tree = html.fromstring(response.text)
        #open('detail.html', 'wb').write(tree)
        #assert tree.xpath('//section[@id="main"]/h2[@id="js-product-list-header"]').text == "Výsledek hledání" , "Kontrola nadpisu"
        #assert home_page_title.search(response.text) is not None, "Expected title has not been found!"
        #TODO dynamic get URL for first product in search result,  xpath:         

    @task
    def get_detail_product(self):
        response = self.client.get("/men/1-1-hummingbird-printed-t-shirt.html#/1-velikost-s/8-barva-bila")
        assert response.status_code == 200
        tree = html.fromstring(response.text)
        #assert tree.xpath('//h1').text == "Hummingbird printed t-shirt", "H1 text on product detail"
        #assert tree.xpath('//div[@class="product-cover"]/img/@src')
        
    @task
    def check_detail_image(self):
        url = 'http://localhost:8085/2-large_default/hummingbird-printed-t-shirt.jpg'
        r = requests.get(url, allow_redirects=True)
        open('detail.jpg', 'wb').write(r.content)
        os.system('.\exif_example\exiftool.exe .\detail.jpg -json -textout .json')
        with open('.\detail.json') as f:
            data = json.load(f)
        print(data)
        data_json = json.loads(data)
        print(data_json['ImageSize'])

    def on_start(self):        
        #self.client.post("/posts", json={"username":"foo", "password":"bar"})
        sql = '''select * from ps_cart order by id_cart desc'''
        #self.cursor.execute(sql)
        #result = self.cursor.fetchone();
        #print(result)

        os.system('.\exif_example\exiftool.exe .\exif_example\example.jpg -json -textout .json')

    def on_stop(self):
        print('End of testing ...')
        self.conn.close()