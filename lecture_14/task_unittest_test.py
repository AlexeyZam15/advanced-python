import unittest


def func(data: dict, first=True):
    data = sorted(data.items(), key=lambda x: x, reverse=not first)
    return data[0][1]


class TestSample(unittest.TestCase):
    def setUp(self) -> None:
        self.data = {'one': 1, 'two': 2, 'three': 3, 'four': 4}

    def test_step_1(self):
        self.assertEqual(func(self.data), 4)

    def test_step_2(self):
        self.assertEqual(func(self.data, first=False), 2)


if __name__ == '__main__':
    unittest.main()
