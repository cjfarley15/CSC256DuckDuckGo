import requests

url_ddg = "https://api.duckduckgo.com/?q=Presidents+Of+The+United+States&format=json&pretty=1"


def test_washington():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Washington" in rsp_data['RelatedTopics']:
        assert True


def test_adams():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Adams" in rsp_data['RelatedTopics']:
        assert True


def test_jefferson():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Jefferson" in rsp_data['RelatedTopics']:
        assert True


def test_madison():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Madison" in rsp_data['RelatedTopics']:
        assert True


def test_monroe():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Monroe" in rsp_data['RelatedTopics']:
        assert True


def test_jackson():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Jackson" in rsp_data['RelatedTopics']:
        assert True


def test_Buren():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Buren" in rsp_data['RelatedTopics']:
        assert True


def test_harrison():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Harrison" in rsp_data['RelatedTopics']:
        assert True


def test_Tyler():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Tyler" in rsp_data['RelatedTopics']:
        assert True


def test_polk():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Polk" in rsp_data['RelatedTopics']:
        assert True


def test_taylor():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Taylor" in rsp_data['RelatedTopics']:
        assert True


def test_fillmore():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Fillmore" in rsp_data['RelatedTopics']:
        assert True


def test_pierce():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Pierce" in rsp_data['RelatedTopics']:
        assert True


def test_buchanan():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Buchanan" in rsp_data['RelatedTopics']:
        assert True


def test_lincoln():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Lincoln" in rsp_data['RelatedTopics']:
        assert True


def test_johnson():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Johnson" in rsp_data['RelatedTopics']:
        assert True


def test_grant():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Grant" in rsp_data['RelatedTopics']:
        assert True


def test_hayes():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Hayes" in rsp_data['RelatedTopics']:
        assert True


def test_garfield():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Garfield" in rsp_data['RelatedTopics']:
        assert True


def test_arthur():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Arthur" in rsp_data['RelatedTopics']:
        assert True


def test_cleveland():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Cleveland" in rsp_data['RelatedTopics']:
        assert True


def test_mckinley():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "McKinley" in rsp_data['RelatedTopics']:
        assert True


def test_taft():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Taft" in rsp_data['RelatedTopics']:
        assert True


def test_wilson():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Wilson" in rsp_data['RelatedTopics']:
        assert True


def test_harding():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Harding" in rsp_data['RelatedTopics']:
        assert True


def test_coolidge():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Coolidge" in rsp_data['RelatedTopics']:
        assert True


def test_hoover():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Hoover" in rsp_data['RelatedTopics']:
        assert True


def test_roosevelt():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Roosevelt" in rsp_data['RelatedTopics']:
        assert True


def test_truman():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Truman" in rsp_data['RelatedTopics']:
        assert True


def test_eisenhower():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Eisenhower" in rsp_data['RelatedTopics']:
        assert True


def test_kennedy():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Kennedy" in rsp_data['RelatedTopics']:
        assert True


def test_nixon():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Nixon" in rsp_data['RelatedTopics']:
        assert True


def test_ford():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Ford" in rsp_data['RelatedTopics']:
        assert True


def test_carter():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Carter" in rsp_data['RelatedTopics']:
        assert True


def test_reagan():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Reagan" in rsp_data['RelatedTopics']:
        assert True


def test_bush():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Bush" in rsp_data['RelatedTopics']:
        assert True


def test_clinton():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Clinton" in rsp_data['RelatedTopics']:
        assert True


def test_obama():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Obama" in rsp_data['RelatedTopics']:
        assert True


def test_trump():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    if "Trump" in rsp_data['RelatedTopics']:
        assert True




