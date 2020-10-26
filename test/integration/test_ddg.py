import requests

url_ddg = "https://api.duckduckgo.com"


def test_pres():
    resp = requests.get(url_ddg + "/?q=Presidents+Of+The+United+States&format=json&pretty=1&skip")
    rsp_data = resp.json()
    assert "Washingon" in rsp_data {
        Abstract: ""
        AbstractText: ""
        AbstractSource: ""
        AbstractURL: ""
        Image: ""
        Heading: ""
        Answer: ""
        Redirect: ""
        AnswerType: ""
        Definition: ""
        DefinitionSource: ""
        DefinitionURL: ""
        RelatedTopics: [ ]
        Results: [ ]
        Type: ""
    }
        
    



