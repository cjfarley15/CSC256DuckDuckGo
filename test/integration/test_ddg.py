import requests

url_ddg = "https://api.duckduckgo.com"


def test_pres():
    resp = requests.get(url_ddg + "/?q=Presidents+Of+The+United+States&format=json&pretty=1&skip")
    rsp_data = resp.json()
    assert "Lincoln" in rsp_data ["RelatedTopics"] 
    



