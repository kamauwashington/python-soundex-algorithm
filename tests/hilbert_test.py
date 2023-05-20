from soundex import soundex

def test_HilbertIsH416 () :
    assert soundex("Hilbert") == "H416"