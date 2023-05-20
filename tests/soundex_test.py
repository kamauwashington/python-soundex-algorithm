from soundex import soundex

def test_inputMustNotBeNone () :
    assert soundex(None) == None

def test_inputMustBe2orMoreChars () :
    assert soundex("T") == None

def test_trailingZeros () :
    assert soundex("Sam") == "S500"