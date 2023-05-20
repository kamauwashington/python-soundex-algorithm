from soundex import soundex

def test_HoneymanIsH555 () :
    assert soundex("Honeyman") == "H555"