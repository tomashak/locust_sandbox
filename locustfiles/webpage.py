import datetime
import os
import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def index_page(self):
        response = self.client.get("/")
        assert response.status_code == 200
        

    @task
    def search_item(self):
        response = self.client.get("/vyhledavani?controller=search&s=Shirt")
        time.sleep(1)
        assert response.status_code == 200
        #assert home_page_title.search(response.text) is not None, "Expected title has not been found!"

    @task
    def get_detail_product(self):
        response = self.client.get("/men/1-1-hummingbird-printed-t-shirt.html#/1-velikost-s/8-barva-bila")
        assert response.status_code == 200

    def on_start(self):
        self.client.post("/posts", json={"username":"foo", "password":"bar"})
        os.system('.\exif_example\exiftool.exe .\exif_example\example.jpg -json -textout .json')