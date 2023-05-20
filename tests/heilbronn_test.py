from soundex import soundex

def test_HeilbronnIsH416 () :
    assert soundex("Heilbronn") == "H416"