from nato import String

class TestString:
    def test_convert_alphabet_single(self):
        assert String('f').to_nato() == 'foxtrot'

    def test_convert_alphabet_multiple(self):
        assert String('abc').to_nato() == 'alfa bravo charlie'

    def test_convert_numeric_single(self):
        assert String('9').to_nato() == 'nin-er'

    def test_convert_numeric_multiple(self):
        assert String('123').to_nato() == 'wun too tree'
