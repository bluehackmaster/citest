import requests

    def test():
        "GET request to url returns a 200"
        # url = 'http://api-prod.stylelens.io/playgrounds/images/datasets/deepfashion/categories'
        url = 'http://www.naver.com'
        payload = {}
        # payload = {'category': "Blouse", 'offset': 0, 'limit': 10}
        resp = requests.get(url, params=payload)
        # j = resp.json()
        assert resp.status_code == 200