from soundex import soundex

def test_EkzampulIsE251 () :
    assert soundex("Ekzampul") == "E251"