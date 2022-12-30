import requests
def func(url):
    url_with_data = f"{url}/?key=test_project&date=2022-12-30"
    response = requests.get(url_with_data)

func("https://webhook.site/b817cb4f-bc7e-4e25-909d-6153bee928ad")