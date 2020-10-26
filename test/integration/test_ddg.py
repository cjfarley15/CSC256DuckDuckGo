import requests

url_ddg = "https://api.duckduckgo.com/?q=Presidents+Of+The+United+States&format=json&pretty=1"


def test_pres():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Lincoln" in rsp_data ['RelatedTopics']:
        assert True
    



