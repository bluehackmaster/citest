import requests

def test():
    "GET request to url returns a 200"
    url = 'http://api-prod.stylelens.io/playgrounds/images/datasets/deepfashion/categories'
    payload = {'category': "Blouse", 'offset': 0, 'limit': 10}
    resp = requests.get(url, params=payload)


    assert resp.status_code == 200

    j = resp.json()

    print(j)
    data = j.get('data')
    assert data != None
    images = data.get('images')
    assert images != None


def test2():
    "GET request to url returns a 200"
    url = 'http://api-prod.stylelens.io/playgrounds/images/datasets/deepfashion/categories'
    payload = {'category': "Blouse", 'offset': 0, 'limit': 10}
    resp = requests.get(url, params=payload)
    assert resp.status_code == 200

    j = resp.json()

    print(j)
    data = j.get('data')
    assert data != None
    images = data.get('images')
    assert images != None

def test3():
    "GET request to url returns a 200"
    url = 'http://api-prod.stylelens.io/playgrounds/images/datasets/deepfashion/categories'
    payload = {'category': "Blouse", 'offset': 0, 'limit': 10}
    resp = requests.get(url, params=payload)
    assert resp.status_code == 300

    j = resp.json()

    print(j)
    data = j.get('data')
    assert data != None
    images = data.get('images')
    assert images != None
