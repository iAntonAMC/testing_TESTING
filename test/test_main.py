from main import Mayor as m

class TestMayor:
    def test_1(self):
        assert m.mayor(self, 2, 1) == 2

    def test_2(self):
        assert m.mayor(self, 1, 2) == 2

    def test_3(self):
        assert m.mayor(self, 2, 2) == None
        
    def test_4(self):
        assert m.mayor(self, 1, -1) == 1

    def test_5(self):
        assert m.mayor(self, -1, 1) == 1

    def test_6(self):
        assert m.mayor(self, -1, -1) == None

    def test_7(self):
        assert m.mayor(self, -1, -2) == -1

    def test_8(self):
        assert m.mayor(self, -2, -1) == -1
