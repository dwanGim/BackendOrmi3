import unittest

def add(x, y):
    return x + y

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(add(2, 2), 3)

    def test_mul(self):
        self.assertEqual(add(3, 2), 3)

    def test_namename(self):
        self.assertEqual(add(4, 2), 3)
        '''
        테스트 이름을 마음대로 정할 수 있는지 체크
        '''
if __name__ == '__main__':
    unittest.main()