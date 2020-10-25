import requests

url_ddg = "https://api.duckduckgo.com"


def test_true():
    assert True


# def test_false():
#   assert False


def test_ddg0():
    resp = requests.get(url_ddg + "/?q=PresidentsoftheUnitedStates&format=json")
    rsp_data = resp.json()
    assert "PresidentsoftheUnited States" in rsp_data["RelatedTopics"]

