from .. import funcs
import pytest

""" def test_create_todays_path():
    assert funcs.create_todays_path(pth = "https://corona.duesseldorf.de/news/die-aktuellen-coronazahlen-vom-") == "https://corona.duesseldorf.de/news/die-aktuellen-coronazahlen-vom-7-oktober"
    assert funcs.create_todays_path(pth = "https://corona.duesseldorf.de/news/die-aktuellen-coronazahlen-vom-") != "https://corona.duesseldorf.de/news/die-aktuellen-coronazahlen-vom"
 """
def test_create_path():
    test11, test12 = funcs.create_path(asof="blabla", pth = "https://corona.duesseldorf.de/news/die-aktuellen-coronazahlen-vom-") 
    assert test11 == "https://corona.duesseldorf.de/news/die-aktuellen-coronazahlen-vom-blabla"
    assert test12 == "blabla"

    test21, test22 = funcs.create_path(pth = "xzy", asof = "123")
    assert test21 == "xzy123"
    assert test22 == "123"

    test31, test32 = funcs.create_path(pth = "xyz", asof = "2012-01-01")
    assert test31 == "xyz2012-01-01"
    assert test32 == "2012-01-01"

def test_date():
    assert funcs.create_date(date = "2020-01-01") == "1-januar"
    assert funcs.create_date(date = "2020-01-10") == "10-januar"
    with pytest.raises(Exception) as e_info: 
        funcs.create_date(date = "2012-01-01") 