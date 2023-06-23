
from functools import reduce

from cli.list import List
from cli.test.test import Test


class TestSeries(List):

    def __init__(self, collection: List):
        self.collection = collection

    def execute_test_series(self):
        reduce(lambda incomplete_list, test_result: incomplete_list.append(test_result),
               map(lambda test: test.check(), ),
               initial=list()
               )


