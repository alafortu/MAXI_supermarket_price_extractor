import requests
import json
import datetime

class MaxiAutocomplete:
    def __init__(self, store_id, term, lang, banner, offer_type):
        self.store_id = store_id
        self.term = term
        self.lang = lang
        self.banner = banner
        self.offer_type = offer_type
        self.url = "https://api.pcexpress.ca/product-facade/v4/products/type-ahead"
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'fr',
            'Business-User-Agent': 'PCXWEB',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'DNT': '1',
            'Origin': 'https://www.maxi.ca',
            'Origin_Session_Header': 'B',
            'Pragma': 'no-cache',
            'Referer': 'https://www.maxi.ca/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'Site-Banner': 'maxi',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'x-apikey': 'C1xujSegT5j3ap3yexJjqhOfELwGKYvz'
        }

    def get_todays_date(self):
        return datetime.datetime.now().strftime('%d%m%Y')

    def send_request(self):
        
        payload = json.dumps({
            "size": 10,
            "storeId": self.store_id,
            "term": self.term,
            "lang": self.lang,
            "date": self.get_todays_date(),
            "version": 1,
            "banner": self.banner,
            "offerType": self.offer_type,
            "displayCategoryFilters": False
        })

        response = requests.request("POST", self.url, headers=self.headers, data=payload)
        return response.text

if __name__ == "__main__":
    while True: 
        autocomplete = MaxiAutocomplete("8679", input("On cherche quoi? "), "fr", "maxi", "OG")
        print(autocomplete.send_request())
