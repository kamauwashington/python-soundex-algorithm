from soundex import soundex

def test_RobertIsR163 () :
    assert soundex("Robert") == "R163"