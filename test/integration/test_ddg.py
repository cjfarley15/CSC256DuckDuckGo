import requests

url_ddg = "https://api.duckduckgo.com"


def test_true():
    assert True


# def test_false():
#   assert False

def test_pres():
    resp = requests.get(url_ddg + "/?q=Presidents+Of+The+United+States&format=json&pretty=1")
    rsp_data = resp.json()
    assert "George Washingon" in rsp_data["RelatedTopics"]
    

def test_ddg0():
    resp = requests.get(url_ddg + "/?q=DuckDuckGo&format=json")
    rsp_data = resp.json()
    assert "DuckDuckGo" in rsp_data["Heading"]

