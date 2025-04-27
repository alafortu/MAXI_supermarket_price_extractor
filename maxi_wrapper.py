import requests
import json
import datetime

class MaxiWrapper:
    def __init__(self):
        self.url = "https://api.pcexpress.ca/product-facade/v4/products/search"
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'fr',
            'Business-User-Agent': 'PCXWEB',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'DNT': '1',
            'Origin': 'https://www.maxi.ca',
            'Origin_Session_Header': 'B',
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

    def get_user_input(self):
        results_count = input("Combien de résultats voulez-vous? ")
        search_term = input("On cherche quoi? ")
        return results_count, search_term

    def get_todays_date(self):
        return datetime.datetime.now().strftime('%d%m%Y')

    def create_payload(self, results_count, search_term):
        return json.dumps({
            "pagination": {
                "from": 0,
                "size": results_count
            },
            "banner": "maxi",
            "cartId": "4a6f7b46-87a1-4010-87a0-c8e5c520c9d0",
            "lang": "fr",
            "date": self.get_todays_date(),
            "storeId": "8679",  # Repentigny
            "pcId": None,
            "pickupType": "STORE",
            "offerType": "ALL",
            "term": search_term,
            "userData": {
                "domainUserId": "4ca14af3-86ff-467e-8893-e568fb0a6533",
                "sessionId": "96b5dad4-d6af-496d-927b-c973e5f6c4b1"
            }
        })

    def fetch_data(self, payload):
        response = requests.request("POST", self.url, headers=self.headers, data=payload)
        return response.json()

    def print_items_table(self, items):
        header = "Brand | Name | Price "
        print(header)
        print("-" * 160)
        for item in items:
            brand = item.get('brand', 'N/A')
            name = item.get('name', 'N/A')
            price = item.get('prices', {}).get('price', {}).get('value', 'N/A')
            print(f"{brand} | {name:<50} | {str(price)}")


    def run(self):
        while True:
            results_count, search_term = self.get_user_input()
            payload = self.create_payload(results_count, search_term)
            response_data = self.fetch_data(payload)
            #print(response_data)
            items = response_data.get('results', [])
            self.print_items_table(items)

if __name__ == '__main__':
    maxi_wrapper = MaxiWrapper()
    maxi_wrapper.run()
