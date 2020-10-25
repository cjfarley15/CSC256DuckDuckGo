import requests

url_ddg = "https://api.duckduckgo.com"


def test_true():
    assert True


# def test_false():
#   assert False


def test_ddg0():
    resp = requests.get(url_ddg + "/?q=Presidents of the United States&format=json")
    rsp_data = resp.json()
    assert "Presidents of the United States" in rsp_data["RelatedTopics"]

