from main import convert, get_headers

class TestConvert():
    def setup_class(self):
        self.packet = open("input2.txt").read().rstrip()


    def test_conversion(self):
        binary = convert(self.packet)

        assert( binary == '110100101111111000101000')

        version, type = get_headers(binary)

        assert( version == 6 )
        assert ( type == 4 )