from cli.test.test_series import TestSeries


class Task:

    def __init__(self, path: str, test_series: TestSeries):
        self.path = path
        self.test_series = test_series

    def test(self):
        self.test_series.execute_test_series()
