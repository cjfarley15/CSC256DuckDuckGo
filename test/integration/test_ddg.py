import requests

url_ddg = "https://api.duckduckgo.com"


def test_pres():
    resp = requests.get(url_ddg + "/?q=Presidents+Of+The+United+States&format=json&pretty=1")
    rsp_data = resp.json()
    assert "Washingon" in rsp_data ["RelatedTopics"]
        
    



